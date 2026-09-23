// api/telegram.js — Vercel Serverless Function
// Receives form data → forwards to Telegram bot
// Token comes from Vercel Environment Variables (dashboard → Settings → Environment Variables)

const BOT_TOKEN = process.env.BOT_TOKEN;
const CHAT_ID = process.env.CHAT_ID || '184519943';

module.exports = async (req, res) => {
  // CORS headers
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  if (!BOT_TOKEN) {
    return res.status(500).json({ error: 'Missing BOT_TOKEN env var — set it in Vercel dashboard.' });
  }

  try {
    const { name, phone, email, field, details } = req.body;

    if (!name || !phone) {
      return res.status(400).json({ error: 'Name and phone are required' });
    }

    // Build Telegram message
    const message = `🔔 New Consultation Request
━━━━━━━━━━━━━━━━━━━━
👤 Name: ${name}
📱 Phone: ${phone}
📧 Email: ${email || 'Not provided'}
🏷️ Field: ${field || 'Not specified'}
📝 Details: ${details || 'No details'}
━━━━━━━━━━━━━━━━━━━━
📅 ${new Date().toLocaleString('en-EG', { timeZone: 'Africa/Cairo' })}`;

    // Send to Telegram
    const telegramUrl = `https://api.telegram.org/bot${BOT_TOKEN}/sendMessage`;
    const response = await fetch(telegramUrl, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        chat_id: CHAT_ID || '@mahmoudagent26_bot', // Send to bot's own chat
        text: message,
        parse_mode: 'HTML'
      })
    });

    const result = await response.json();

    if (result.ok) {
      return res.status(200).json({ success: true, message: 'Sent to Telegram' });
    } else {
      console.error('Telegram error:', result);
      return res.status(500).json({ error: 'Failed to send to Telegram', details: result.description });
    }
  } catch (err) {
    console.error('Error:', err);
    return res.status(500).json({ error: 'Server error', details: err.message });
  }
};
