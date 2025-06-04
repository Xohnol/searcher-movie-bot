import asyncio
import logging
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters

from utils.config import TELEGRAM_BOT_TOKEN
from handlers.commands import start, help_command, search_command
from handlers.messages import gestisci_messaggio, gestisci_callback

# Configura logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def main():
    """Funzione principale del bot"""
    
    # Controlla che il token sia configurato
    if not TELEGRAM_BOT_TOKEN:
        print("❌ ERRORE: Token Telegram non configurato!")
        print("Assicurati di aver creato il file .env con il tuo TELEGRAM_BOT_TOKEN")
        return
    
    # Crea l'applicazione
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    
    # Aggiungi handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("search", search_command))
    
    # Handler per messaggi di testo
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, gestisci_messaggio))
    
    # Handler per callback query (bottoni inline)
    application.add_handler(CallbackQueryHandler(gestisci_callback))
    
    print("🤖 Bot avviato! Premi Ctrl+C per fermare.")
    
    # Avvia il bot
    application.run_polling()

if __name__ == '__main__':
    main()