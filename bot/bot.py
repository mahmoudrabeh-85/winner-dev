#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rabeh Consultant Bot — Telegram Chatbot
Handles: Services info, Quran memorization, Consultation booking, Admin confirmations
"""

import json
import os
import logging
import tempfile
from datetime import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application, CommandHandler, MessageHandler, CallbackQueryHandler,
    ConversationHandler, ContextTypes, filters
)

# --- Voice Recognition ---
import speech_recognition as sr
from pydub import AudioSegment

# --- Configuration ---
# Read the token from the environment (or bot/.env) — NEVER hardcode it in code
def _load_token():
    token = os.environ.get("BOT_TOKEN")
    if token:
        return token.strip()
    # Fallback: try bot/.env file (gitignored, local only)
    env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
    if os.path.exists(env_path):
        with open(env_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    if k.strip() == "BOT_TOKEN":
                        return v.strip().strip('"').strip("'")
    raise SystemExit(
        "❌ BOT_TOKEN not found!\n"
        "Create bot/.env with:\n"
        "BOT_TOKEN=your_token_here\n"
        "or set the BOT_TOKEN environment variable."
    )

BOT_TOKEN = _load_token()
ADMIN_CHAT_ID = 184519943

# --- Load Knowledge Base ---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(SCRIPT_DIR, "knowledge.json"), "r", encoding="utf-8") as f:
    KB = json.load(f)

# --- Bookings File ---
BOOKINGS_FILE = os.path.join(SCRIPT_DIR, "bookings.json")

def load_bookings():
    if os.path.exists(BOOKINGS_FILE):
        with open(BOOKINGS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_bookings(bookings):
    with open(BOOKINGS_FILE, "w", encoding="utf-8") as f:
        json.dump(bookings, f, ensure_ascii=False, indent=2)

# --- Voice Recognition ---
async def transcribe_voice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Download voice message → convert OGG to WAV → transcribe with Google Speech"""
    voice = update.message.voice or update.message.audio
    if not voice:
        return None
    
    # Download the voice file
    file = await context.bot.get_file(voice.file_id)
    with tempfile.NamedTemporaryFile(suffix=".ogg", delete=False) as ogg_file:
        ogg_path = ogg_file.name
        await file.download_to_drive(ogg_path)
    
    try:
        # Convert OGG to WAV
        audio = AudioSegment.from_ogg(ogg_path)
        wav_path = ogg_path.replace(".ogg", ".wav")
        audio.export(wav_path, format="wav")
        
        # Transcribe with Google Speech Recognition
        recognizer = sr.Recognizer()
        with sr.AudioFile(wav_path) as source:
            audio_data = recognizer.record(source)
        
        # Try Arabic first, then English, then auto-detect
        try:
            text = recognizer.recognize_google(audio_data, language="ar-EG")
        except sr.UnknownValueError:
            try:
                text = recognizer.recognize_google(audio_data, language="en-US")
            except sr.UnknownValueError:
                text = recognizer.recognize_google(audio_data)
        
        return text
    except Exception as e:
        logger.error(f"Voice transcription error: {e}")
        return None
    finally:
        # Cleanup temp files
        for f in [ogg_path, wav_path if 'wav_path' in locals() else None]:
            if f and os.path.exists(f):
                os.unlink(f)

# --- Logging ---
LOG_FILE = os.path.join(SCRIPT_DIR, "bot.log")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# --- Conversation States ---
IDLE, AWAITING_NAME, AWAITING_PHONE, AWAITING_DATE, AWAITING_TIME, AWAITING_DETAILS, AWAITING_CONFIRM = range(7)

# --- User Language Detection ---
def get_lang(update: Update) -> str:
    """Detect user language from message"""
    text = update.message.text if update.message else ""
    arabic_chars = sum(1 for c in text if '\u0600' <= c <= '\u06FF')
    return "ar" if arabic_chars > len(text) * 0.3 else "en"

def t(lang, ar_text, en_text):
    """Return text based on language"""
    return ar_text if lang == "ar" else en_text

def message_text(update, context):
    """Return message text — typed directly OR transcribed from voice (one-shot)"""
    vt = context.user_data.pop("_voice_text", None)
    if vt:
        return vt
    return (update.message.text or "") if update.message else ""

# --- Keyboard Builders ---
def main_menu_keyboard(lang):
    buttons = [
        [InlineKeyboardButton(t(lang, "📦 الخدمات", "📦 Services"), callback_data="services")],
        [InlineKeyboardButton(t(lang, "📅 حجز موعد", "📅 Book Appointment"), callback_data="book")],
        [InlineKeyboardButton(t(lang, "❓ أسئلة شائعة", "❓ FAQ"), callback_data="faq")],
        [InlineKeyboardButton(t(lang, "📞 تواصل معي", "📞 Contact"), callback_data="contact")],
    ]
    return InlineKeyboardMarkup(buttons)

def services_keyboard(lang):
    buttons = []
    for s in KB["services"]:
        buttons.append([InlineKeyboardButton(s[f"name_{lang}"], callback_data=f"svc_{s['id']}")])
    buttons.append([InlineKeyboardButton(t(lang, "🔙 رجوع", "🔙 Back"), callback_data="back")])
    return InlineKeyboardMarkup(buttons)

def book_type_keyboard(lang):
    buttons = [
        [InlineKeyboardButton(t(lang, "💼 استشارة", "💼 Consultation"), callback_data="book_consultation")],
        [InlineKeyboardButton(t(lang, "📖 تحفيظ قرآن", "📖 Quran Memorization"), callback_data="book_quran")],
        [InlineKeyboardButton(t(lang, "🎓 تدريب", "🎓 Training"), callback_data="book_training")],
        [InlineKeyboardButton(t(lang, "🔙 رجوع", "🔙 Back"), callback_data="back")],
    ]
    return InlineKeyboardMarkup(buttons)

def confirm_keyboard(lang):
    buttons = [
        [InlineKeyboardButton(t(lang, "✅ تأكيد الحجز", "✅ Confirm Booking"), callback_data="confirm_yes")],
        [InlineKeyboardButton(t(lang, "❌ إلغاء", "❌ Cancel"), callback_data="confirm_no")],
    ]
    return InlineKeyboardMarkup(buttons)

def admin_confirm_keyboard(booking_id):
    buttons = [
        [InlineKeyboardButton("✅ تأكيد", callback_data=f"admin_yes_{booking_id}")],
        [InlineKeyboardButton("❌ رفض", callback_data=f"admin_no_{booking_id}")],
    ]
    return InlineKeyboardMarkup(buttons)

async def _notify_admin(context, text: str):
    """Instant admin alert — the owner always knows what visitors are doing."""
    try:
        await context.bot.send_message(chat_id=ADMIN_CHAT_ID, text=text)
    except Exception as e:
        logger.error(f"Admin notify failed: {e}")

def _sender_label(update: Update) -> str:
    u = update.effective_user
    name = (u.first_name or "") + (" " + u.last_name if getattr(u, "last_name", None) else "")
    name = name.strip() or "زائر"
    if u.username:
        return f"{name} (@{u.username})"
    return name

# --- Command Handlers ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = get_lang(update)
    context.user_data["lang"] = lang
    # Alert the owner: a new visitor started a conversation
    await _notify_admin(
        context,
        f"👋 محادثة جديدة بدأت!\n👤 {_sender_label(update)}\n🆔 {update.effective_user.id}"
    )
    welcome = KB[f"welcome_{lang}"]
    await update.message.reply_text(welcome, reply_markup=main_menu_keyboard(lang))
    return IDLE

async def cmd_bookings(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Admin: View all bookings as formatted message"""
    if update.effective_user.id != ADMIN_CHAT_ID:
        await update.message.reply_text("❌ غير مصرح لك.")
        return
    from tracker import format_summary_message
    msg = format_summary_message("ar")
    await update.message.reply_text(msg)

async def cmd_export(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Admin: Export bookings as Excel file"""
    if update.effective_user.id != ADMIN_CHAT_ID:
        await update.message.reply_text("❌ غير مصرح لك.")
        return
    from tracker import create_excel_report, format_summary_message
    filepath = create_excel_report()
    # Always send the text summary first — works even if file download stalls
    await update.message.reply_text(format_summary_message("ar"))
    try:
        # Read the whole file into memory FIRST, then close it — clean & reliable upload
        with open(filepath, "rb") as f:
            data = f.read()
        name = os.path.basename(filepath)
        await update.message.reply_document(
            document=data,
            filename=name,
            caption="📊 تقرير الحجوزات — Rabeh Consultant"
        )
    except Exception as e:
        logger.error(f"Export failed: {e}")
        await update.message.reply_text(
            "❌ فشل إرسال الملف تيليجرامياً. لكن الشيت محفوظ محلياً:\n"
            "`bot/bookings_report_latest.xlsx` — افتحه مباشرة من الكمبيوتر."
        )

async def cmd_pending(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Admin: View only pending bookings"""
    if update.effective_user.id != ADMIN_CHAT_ID:
        await update.message.reply_text("❌ غير مصرح لك.")
        return
    from tracker import get_pending_bookings, format_booking_message
    pending = get_pending_bookings()
    if not pending:
        await update.message.reply_text("✅ لا توجد حجوزات قيد الانتظار.")
        return
    msg = f"⏳ **حجوزات قيد الانتظار: {len(pending)}**\n━━━━━━━━━━━━━━━━━━━━\n\n"
    for b in pending:
        msg += format_booking_message(b) + "\n"
    await update.message.reply_text(msg)

# --- Callback Handlers ---
async def callback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data
    lang = context.user_data.get("lang", "ar")

    if data == "back":
        await query.edit_message_text(
            t(lang, "اختر خياراً:", "Choose an option:"),
            reply_markup=main_menu_keyboard(lang)
        )
        return IDLE

    elif data == "services":
        await query.edit_message_text(
            t(lang, "اختر الخدمة للاطلاع على التفاصيل:", "Select a service for details:"),
            reply_markup=services_keyboard(lang)
        )

    elif data.startswith("svc_"):
        svc_id = data[4:]
        svc = next((s for s in KB["services"] if s["id"] == svc_id), None)
        if svc:
            text = f"**{svc[f'name_{lang}']}**\n\n{svc[f'desc_{lang}']}\n\n"
            text += t(lang, f"⏱ المدة: {svc['duration']}", f"⏱ Duration: {svc['duration']}")
            text += "\n\n" + t(lang, "هل تريد حجز موعد؟ اضغط 'حجز موعد' من القائمة.", "Want to book? Click 'Book Appointment' from the menu.")
            keyboard = InlineKeyboardMarkup([
                [InlineKeyboardButton(t(lang, "📅 حجز موعد", "📅 Book"), callback_data="book")],
                [InlineKeyboardButton(t(lang, "🔙 رجوع", "🔙 Back"), callback_data="back")]
            ])
            await query.edit_message_text(text, reply_markup=keyboard)

    elif data == "faq":
        text = t(lang, "❓ الأسئلة الشائعة:", "❓ Frequently Asked Questions:\n")
        for i, item in enumerate(KB["faq"], 1):
            text += f"\n**{i}. {item[f'q_{lang}']}**\n{item[f'a_{lang}']}\n"
        await query.edit_message_text(text, reply_markup=main_menu_keyboard(lang))

    elif data == "contact":
        text = t(lang,
            "📞 تواصل مع محمود رابح:\n\n"
            "📱 واتساب: +201006125478\n"
            "📱 تيليجرام: @mahmoudrabeh1\n"
            "🔗 لينكدإن: linkedin.com/in/mahmoud-rabeh-7102071a3\n"
            "📅 احجز موعداً مباشرة من القائمة الرئيسية\n\n"
            "⏰ ساعات العمل: الأحد-الخميس، 9 صباحاً - 6 مساءً",
            "📞 Contact Mahmoud Rabeh:\n\n"
            "📱 WhatsApp: +201006125478\n"
            "📱 Telegram: @mahmoudrabeh1\n"
            "🔗 LinkedIn: linkedin.com/in/mahmoud-rabeh-7102071a3\n"
            "📅 Book an appointment directly from the main menu\n\n"
            "⏰ Working Hours: Sun-Thu, 9AM - 6PM"
        )
        await query.edit_message_text(text, reply_markup=main_menu_keyboard(lang))
        return IDLE

    elif data == "book":
        await query.edit_message_text(
            t(lang, "اختر نوع الحجز:", "Select booking type:"),
            reply_markup=book_type_keyboard(lang)
        )

    elif data.startswith("book_"):
        booking_type = data[5:]
        context.user_data["booking_type"] = booking_type
        context.user_data["booking_data"] = {}
        
        type_name = {
            "consultation": t(lang, "💼 استشارة", "💼 Consultation"),
            "quran": t(lang, "📖 تحفيظ قرآن", "📖 Quran Memorization"),
            "training": t(lang, "🎓 تدريب", "🎓 Training")
        }.get(booking_type, t(lang, "خدمة", "Service"))
        
        await query.edit_message_text(
            t(lang, f"أحسنت! أنت تختار: {type_name}\n\nما اسمك الكريم؟", 
                      f"Great! You selected: {type_name}\n\nWhat is your name?")
        )
        context.user_data["awaiting"] = "name"
        return AWAITING_NAME

    elif data == "confirm_yes":
        # Save booking
        booking = context.user_data.get("booking_data", {})
        booking_id = f"BK{len(load_bookings()) + 1:04d}"
        booking["id"] = booking_id
        booking["status"] = "pending"
        booking["timestamp"] = datetime.now().isoformat()
        booking["user_id"] = update.effective_user.id
        booking["username"] = update.effective_user.username or ""
        
        bookings = load_bookings()
        bookings.append(booking)
        save_bookings(bookings)
        
        # Notify admin
        admin_msg = f"🔔 **حجز جديد!**\n"
        admin_msg += f"━━━━━━━━━━━━━━━━━━━━\n"
        admin_msg += f"📋 رقم الحجز: {booking_id}\n"
        admin_msg += f"👤 الاسم: {booking.get('name', 'N/A')}\n"
        admin_msg += f"📱 الهاتف: {booking.get('phone', 'N/A')}\n"
        admin_msg += f"📅 التاريخ: {booking.get('date', 'N/A')}\n"
        admin_msg += f"⏰ الوقت: {booking.get('time', 'N/A')}\n"
        admin_msg += f"💼 النوع: {booking.get('type_name', 'N/A')}\n"
        admin_msg += f"📝 التفاصيل: {booking.get('details', 'N/A')}\n"
        admin_msg += f"━━━━━━━━━━━━━━━━━━━━"
        
        await context.bot.send_message(
            chat_id=ADMIN_CHAT_ID,
            text=admin_msg,
            reply_markup=admin_confirm_keyboard(booking_id)
        )
        
        await query.edit_message_text(
            t(lang, 
                f"✅ تم استلام طلب الحجز بنجاح!\n\n📋 رقم الحجز: {booking_id}\n⏰ سيتم تأكيد الموعد خلال ساعات العمل الرسمية.\n\nشكراً لتواصلك!",
                f"✅ Booking request received!\n\n📋 Booking ID: {booking_id}\n⏰ Your appointment will be confirmed within working hours.\n\nThank you!"
            ),
            reply_markup=main_menu_keyboard(lang)
        )
        return IDLE

    elif data == "confirm_no":
        await query.edit_message_text(
            t(lang, "❌ تم إلغاء الحجز. هل تحتاج شيء آخر?", "❌ Booking cancelled. Need anything else?"),
            reply_markup=main_menu_keyboard(lang)
        )
        return IDLE

    elif data.startswith("admin_yes_"):
        if update.effective_user.id == ADMIN_CHAT_ID:
            bid = data[9:]
            bookings = load_bookings()
            for b in bookings:
                if b["id"] == bid:
                    b["status"] = "confirmed"
                    # Notify user
                    try:
                        await context.bot.send_message(
                            chat_id=b["user_id"],
                            text=t("ar",
                                f"✅ تم تأكيد حجزك!\n\n📋 رقم الحجز: {bid}\n📅 التاريخ: {b.get('date')}\n⏰ الوقت: {b.get('time')}\n\nنتطلع لرؤيتك!",
                                f"✅ Your booking is confirmed!\n\n📋 Booking ID: {bid}\n📅 Date: {b.get('date')}\n⏰ Time: {b.get('time')}\n\nLooking forward to seeing you!"
                            )
                        )
                    except Exception as e:
                        logger.error(f"Could not notify user: {e}")
                    break
            save_bookings(bookings)
            await query.edit_message_text(f"✅ تم تأكيد الحجز {bid} — تم إشعار العميل.")
        else:
            await query.answer("❌ غير مصرح لك بهذا الإجراء.", show_alert=True)

    elif data.startswith("admin_no_"):
        if update.effective_user.id == ADMIN_CHAT_ID:
            bid = data[8:]
            bookings = load_bookings()
            for b in bookings:
                if b["id"] == bid:
                    b["status"] = "rejected"
                    try:
                        await context.bot.send_message(
                            chat_id=b["user_id"],
                            text=t("ar",
                                f"❌ عذراً، لم يتم تأكيد حجزك رقم {bid}.\n\nيمكنك المحاولة مرة أخرى في وقت لاحق أو التواصل مباشرة.",
                                f"❌ Sorry, your booking {bid} was not confirmed.\n\nYou can try again later or contact directly."
                            )
                        )
                    except Exception as e:
                        logger.error(f"Could not notify user: {e}")
                    break
            save_bookings(bookings)
            await query.edit_message_text(f"❌ تم رفض الحجز {bid} — تم إشعار العميل.")
        else:
            await query.answer("❌ غير مصرح لك بهذا الإجراء.", show_alert=True)

    return IDLE

# --- Message Handlers ---
async def receive_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = context.user_data.get("lang", "ar")
    context.user_data["booking_data"]["name"] = message_text(update, context)
    context.user_data["booking_data"]["type"] = context.user_data.get("booking_type", "")
    type_names = {"consultation": "💼 استشارة", "quran": "📖 تحفيظ قرآن", "training": "🎓 تدريب"}
    context.user_data["booking_data"]["type_name"] = type_names.get(context.user_data.get("booking_type", ""), "خدمة")
    
    await update.message.reply_text(
        t(lang, "✅ ما رقم هاتفك / واتساب؟", "✅ What is your phone / WhatsApp number?")
    )
    context.user_data["awaiting"] = "phone"
    return AWAITING_PHONE

async def receive_phone(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = context.user_data.get("lang", "ar")
    context.user_data["booking_data"]["phone"] = message_text(update, context)
    
    await update.message.reply_text(
        t(lang, "📅 ما التاريخ المفضل لك؟ (مثلا: الأحد القادم، 15 سبتمبر)", 
                  "📅 What date do you prefer? (e.g., Next Sunday, Sep 15)")
    )
    context.user_data["awaiting"] = "date"
    return AWAITING_DATE

async def receive_date(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = context.user_data.get("lang", "ar")
    context.user_data["booking_data"]["date"] = message_text(update, context)
    
    await update.message.reply_text(
        t(lang, "⏰ ما الوقت المناسب لك؟ (مثلا: 2 مساءً، بعد الظهر)", 
                  "⏰ What time works for you? (e.g., 2 PM, after noon)")
    )
    context.user_data["awaiting"] = "time"
    return AWAITING_TIME

async def receive_time(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = context.user_data.get("lang", "ar")
    context.user_data["booking_data"]["time"] = message_text(update, context)
    
    await update.message.reply_text(
        t(lang, "📝 أضف أي تفاصيل إضافية (اختياري — أرسل '-' للتخطي)", 
                  "📝 Add any additional details (optional — send '-' to skip)")
    )
    context.user_data["awaiting"] = "details"
    return AWAITING_DETAILS

async def receive_details(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = context.user_data.get("lang", "ar")
    details = message_text(update, context)
    if details == "-":
        details = ""
    context.user_data["booking_data"]["details"] = details
    
    booking = context.user_data["booking_data"]
    summary = t(lang,
        f"📋 **ملخص الحجز:**\n\n"
        f"👤 الاسم: {booking.get('name')}\n"
        f"📱 الهاتف: {booking.get('phone')}\n"
        f"💼 النوع: {booking.get('type_name')}\n"
        f"📅 التاريخ: {booking.get('date')}\n"
        f"⏰ الوقت: {booking.get('time')}\n"
        f"📝 التفاصيل: {booking.get('details', 'لا توجد')}\n\n"
        f"هل تريد تأكيد هذا الحجز؟",
        f"📋 **Booking Summary:**\n\n"
        f"👤 Name: {booking.get('name')}\n"
        f"📱 Phone: {booking.get('phone')}\n"
        f"💼 Type: {booking.get('type_name')}\n"
        f"📅 Date: {booking.get('date')}\n"
        f"⏰ Time: {booking.get('time')}\n"
        f"📝 Details: {booking.get('details', 'None')}\n\n"
        f"Confirm this booking?"
    )
    
    await update.message.reply_text(summary, reply_markup=confirm_keyboard(lang))
    context.user_data["awaiting"] = None
    return AWAITING_CONFIRM

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = context.user_data.get("lang", "ar")
    await update.message.reply_text(
        t(lang, "❌ تم الإلغاء. اكتب /start للبدء من جديد.", "❌ Cancelled. Type /start to begin again.")
    )
    return ConversationHandler.END

async def voice_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle voice messages — transcribe then process as text"""
    lang = context.user_data.get("lang", "ar")
    
    # Alert the owner: voice message received
    await _notify_admin(context, f"🎤 رسالة صوتية من {_sender_label(update)}")
    
    # Show "typing" indicator
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")
    
    # Transcribe
    text = await transcribe_voice(update, context)
    
    if text:
        # Show transcription to user
        await update.message.reply_text(
            t(lang, f"🎤 سمعتك: \"{text}\"", f"🎤 I heard: \"{text}\"")
        )
        # Store transcribed text so message_handler can process it
        context.user_data["_voice_text"] = text
        return await message_handler(update, context)
    else:
        await update.message.reply_text(
            t(lang, 
                "❌ عذراً، لم أتمكن من فهم الرسالة الصوتية.\n\nيمكنك:\n• المحاولة مرة أخرى بصوت أوضح\n• كتابة رسالتك نصاً",
                "❌ Sorry, I couldn't understand the voice message.\n\nYou can:\n• Try again with clearer audio\n• Type your message instead")
        )
        return IDLE

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle regular text messages based on current state"""
    lang = context.user_data.get("lang", "ar")
    awaiting = context.user_data.get("awaiting")
    
    # Alert the owner about every free-text message (not booking-flow fields)
    if awaiting is None:
        raw_text = message_text(update, context)
        await _notify_admin(
            context,
            f"💬 رسالة من {_sender_label(update)}:\n\n{raw_text}"
        )
    
    if awaiting == "name":
        return await receive_name(update, context)
    elif awaiting == "phone":
        return await receive_phone(update, context)
    elif awaiting == "date":
        return await receive_date(update, context)
    elif awaiting == "time":
        return await receive_time(update, context)
    elif awaiting == "details":
        return await receive_details(update, context)
    else:
        # Free text — smart intent detection
        text = message_text(update, context).lower().strip()
        
        # Greetings
        if any(w in text for w in ["مرحبا", "أهلا", "اهلا", "هلا", "السلام", "صباح", "مساء", "هاي", "hello", "hi", "hey", "salam", "marhaba"]):
            await update.message.reply_text(
                t(lang,
                    "أهلاً وسهلاً بك! 👋\nكيف أقدر أخدمك اليوم؟ اختر من القائمة:",
                    "Welcome! 👋\nHow can I help you today? Choose from the menu:"),
                reply_markup=main_menu_keyboard(lang)
            )
        # Who is he / about
        elif any(w in text for w in ["من أنت", "من انت", "عني", "نبذة", "من هو", "من هو محمود", "who are you", "about you", "about me", "information", "سيرة"]):
            await update.message.reply_text(
                t(lang,
                    "👤 **محمود رابح**\n\n"
                    "مستشار مشتريات وسلاسل إمداد — أكثر من 18 عاماً خبرة في قطاع التوزيع والتجارة.\n"
                    "مبرمج ومطور مواقع وتطبيقات، ومحفظ قرآن ومعلم لغة عربية.\n\n"
                    "اختر من القائمة لمعرفة الخدمات أو حجز موعد:",
                    "👤 **Mahmoud Rabeh**\n\n"
                    "Procurement & Supply Chain Consultant — 18+ years in trading & distribution.\n"
                    "Developer & builder of websites and apps, Quran tutor and Arabic teacher.\n\n"
                    "Choose from the menu for services or to book:"),
                reply_markup=main_menu_keyboard(lang)
            )
        # Pricing
        elif any(w in text for w in ["سعر", "ثمن", "تكلفة", "بكام", "كام سعر", "اسعار", "أسعار", "مقابل", "price", "cost", "fee", "charge", "how much", "الأسعار"]):
            await update.message.reply_text(
                t(lang,
                    "💰 الأسعار تُحدد حسب المشروع وحجمه.\n"
                    "الأفضل: احجز استشارة قصيرة ونتفق على الأفضل لك.\n\n"
                    "اضغط 'حجز موعد' من القائمة:",
                    "💰 Pricing depends on the project scope.\n"
                    "Best approach: book a short consultation and we find the right fit.\n\n"
                    "Click 'Book Appointment' from the menu:"),
                reply_markup=book_type_keyboard(lang)
            )
        # Quran / memorization
        elif any(w in text for w in ["قرآن", "قران", "تحفيظ", "حفظ", "تجويد", "quran", "memorization", "تلقين"]):
            svc = next((s for s in KB["services"] if s["id"] == "quran"), None)
            if svc:
                await update.message.reply_text(
                    f"**{svc[f'name_{lang}']}**\n\n{svc[f'desc_{lang}']}\n\n"
                    + t(lang, "هل تريد حجز موعد تحفيظ؟", "Would you like to book a memorization session?"),
                    reply_markup=book_type_keyboard(lang)
                )
            else:
                await update.message.reply_text(
                    t(lang, "لدينا برنامج تحفيظ قرآن شامل — اختر حجز موعد للبدء!", 
                      "We have a full Quran memorization program — pick Book Appointment to start!"),
                    reply_markup=book_type_keyboard(lang)
                )
        # Contact
        elif any(w in text for w in ["تواصل", "هاتف", "رقم", "واتساب", "contact", "phone", "whatsapp", "رقمك"]):
            await update.message.reply_text(
                t(lang,
                    "📞 تواصل مع محمود رابح:\n\n"
                    "📱 واتساب: +201006125478\n"
                    "📱 تيليجرام: @mahmoudrabeh1\n"
                    "🔗 لينكدإن: linkedin.com/in/mahmoud-rabeh-7102071a3\n\n"
                    "أو احجز موعداً مباشرة من القائمة:", 
                    "📞 Contact Mahmoud Rabeh:\n\n"
                    "📱 WhatsApp: +201006125478\n"
                    "📱 Telegram: @mahmoudrabeh1\n"
                    "🔗 LinkedIn: linkedin.com/in/mahmoud-rabeh-7102071a3\n\n"
                    "Or book an appointment right from the menu:"),
                reply_markup=main_menu_keyboard(lang)
            )
        # Thanks
        elif any(w in text for w in ["شكرا", "شكراً", "تسلم", "يعطيك", "مشكور", "جزاك", "thank", "thanks", "thx", "nice", "great"]):
            await update.message.reply_text(
                t(lang,
                    "العفو! 😊 سعيد بخدمتك — لا تتردد في التواصل في أي وقت.",
                    "You're welcome! 😊 Happy to help — feel free to reach out anytime."),
                reply_markup=main_menu_keyboard(lang)
            )
        # Goodbye
        elif any(w in text for w in ["مع السلامة", "باي", "وداعا", "وداعاً", "تصبح", "bye", "goodbye", "see you"]):
            await update.message.reply_text(
                t(lang,
                    "وداعاً! 👋 نتمنى أن نراك قريباً.",
                    "Goodbye! 👋 Hope to see you soon."),
                reply_markup=main_menu_keyboard(lang)
            )
        # Book / appointment (existing)
        elif any(w in text for w in ["حجز", "موعد", "book", "appointment"]):
            await update.message.reply_text(
                t(lang, "اختر نوع الحجز:", "Select booking type:"),
                reply_markup=book_type_keyboard(lang)
            )
        # Services (existing)
        elif any(w in text for w in ["خدمة", "خدمات", "استشارة", "service", "services", "consulting"]):
            await update.message.reply_text(
                t(lang, "اختر الخدمة للاطلاع على التفاصيل:", "Select a service for details:"),
                reply_markup=services_keyboard(lang)
            )
        # FAQ (existing)
        elif any(w in text for w in ["شائع", "سؤال", "faq", "أسئلة"]):
            text_faq = t(lang, "❓ الأسئلة الشائعة:", "❓ Frequently Asked Questions:\n")
            for i, item in enumerate(KB["faq"], 1):
                text_faq += f"\n**{i}. {item[f'q_{lang}']}**\n{item[f'a_{lang}']}\n"
            await update.message.reply_text(text_faq, reply_markup=main_menu_keyboard(lang))
        else:
            await update.message.reply_text(
                t(lang, "كيف يمكنني مساعدتك؟ اختر من القائمة:", "How can I help you? Choose from the menu:"),
                reply_markup=main_menu_keyboard(lang)
            )
        return IDLE

# --- Main ---
def main():
    app = Application.builder().token(BOT_TOKEN).build()
    
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            IDLE: [
                CallbackQueryHandler(callback_handler),
                MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler)
            ],
            AWAITING_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, receive_name)],
            AWAITING_PHONE: [MessageHandler(filters.TEXT & ~filters.COMMAND, receive_phone)],
            AWAITING_DATE: [MessageHandler(filters.TEXT & ~filters.COMMAND, receive_date)],
            AWAITING_TIME: [MessageHandler(filters.TEXT & ~filters.COMMAND, receive_time)],
            AWAITING_DETAILS: [MessageHandler(filters.TEXT & ~filters.COMMAND, receive_details)],
            AWAITING_CONFIRM: [CallbackQueryHandler(callback_handler)],
        },
        fallbacks=[CommandHandler("start", start)],
        allow_reentry=True
    )
    
    app.add_handler(conv_handler)
    
    # Admin commands (outside conversation)
    app.add_handler(CommandHandler("bookings", cmd_bookings))
    app.add_handler(CommandHandler("export", cmd_export))
    app.add_handler(CommandHandler("pending", cmd_pending))
    
    # Voice message handler (outside conversation)
    app.add_handler(MessageHandler(filters.VOICE | filters.AUDIO, voice_handler))
    
    # Global fallback handlers — catch button clicks & text for users who never pressed /start
    app.add_handler(CallbackQueryHandler(callback_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))
    
    logger.info("Bot is running...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
