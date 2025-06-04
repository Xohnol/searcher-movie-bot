# 🎬 Searcher Movie Bot

> **An intelligent Telegram bot to find movies and TV series in seconds!**

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)
[![Telegram Bot](https://img.shields.io/badge/Telegram-Bot-blue.svg)](https://telegram.org)
[![TMDB](https://img.shields.io/badge/API-TMDB-green.svg)](https://themoviedb.org)

## ✨ **What does this bot do?**

**Searcher Movie Bot** is your personal assistant to find any movie or TV series! Just send the title and you'll instantly receive the link to watch it.

### 🚀 **Main features:**

- 🔍 **Smart search** - Powered by TMDB API for accurate results
- 🎬 **Instant movies** - Direct links to thousands of movies
- 📺 **Complete TV series** - Navigate through seasons and episodes with elegant menus
- ⚡ **Lightning speed** - Responses in less than 2 seconds
- 🎯 **Zero configuration** - Just press start and you're ready!

## 🎮 **How it works**

### **Step 1:** Start the bot
```
/start
```

### **Step 2:** Search for what you want
```
Blue Beetle
Money Heist
Avengers Endgame
```

### **Step 3:** Get your link!
The bot will immediately give you the link to watch the content.

## 🎯 **Quick demo**

```
👤 User: "Spider-Man"
🤖 Bot:  🔍 Searching: Spider-Man...
       ✅ Found: Spider-Man: No Way Home (2021)
       🔗 Link: https://vixsrc.to/movie/634649
       🍿 Click and enjoy!
```

## 🛠️ **Available commands**

| Command | Description |
|---------|-------------|
| `/start` | 🎬 Welcome message and instructions |
| `/help` | 🆘 Detailed usage guide |
| `/search <title>` | 🔍 Search for a specific title |
| `<any text>` | 🎯 Direct search without commands |

## 🏗️ **Project architecture**

```
src/
├── bot.py              # 🤖 Telegram bot core
├── handlers/           # 📨 Commands and messages handling
├── services/           # 🔌 TMDB API and link generation
├── utils/              # ⚙️ Configurations and utilities
└── models/             # 📋 Data models (future use)
```

## 🚀 **Quick deploy**

### **Method 1: Railway (Recommended)**
1. Fork this repository
2. Connect it to [Railway](https://railway.app)
3. Add environment variables
4. The bot is online! 🎉

### **Method 2: Local**
```bash
git clone https://github.com/yourusername/searcher-movie-bot
cd searcher-movie-bot
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your tokens
cd src && python bot.py
```

## ⚙️ **Configuration**

Rename `.env.example` to `.env` and add:

```env
TELEGRAM_BOT_TOKEN=your_token_here
TMDB_API_KEY=your_api_key_here
```

### **How to get tokens:**
- 🤖 **Bot Token**: Message [@BotFather](https://t.me/botfather) on Telegram
- 🎬 **TMDB API**: Register on [TMDB](https://www.themoviedb.org/settings/api)

## 🎨 **Technical features**

- ⚡ **Asynchronous** - Handles thousands of simultaneous users
- 🛡️ **Robust** - Complete error handling
- 📱 **Responsive** - Interface with elegant inline buttons
- 🔍 **Smart search** - Search logic optimized for multiple languages
- 🌐 **Scalable** - Ready for cloud deployment

## 📊 **Statistics**

- 🎬 **+50,000** available movies
- 📺 **+10,000** TV series
- 🌍 **Multi-language** - Search in multiple languages
- ⚡ **<2s** average response time

## 🤝 **Contributing**

Want to improve the bot? PRs are welcome!

1. Fork the project
2. Create your branch (`git checkout -b feature/NewFeature`)
3. Commit changes (`git commit -m 'Add new feature'`)
4. Push to branch (`git push origin feature/NewFeature`)
5. Open a Pull Request

## 🔗 **Useful links**

- 📖 [Telegram Bot API Documentation](https://core.telegram.org/bots/api)
- 🎬 [TMDB API Docs](https://developers.themoviedb.org/3)
- 🚀 [Deploy on Railway](https://railway.app)

---

### ⭐ **Like the project? Leave a star!**
