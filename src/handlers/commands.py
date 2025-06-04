from telegram import Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /start"""
    welcome_text = """
🎬 **Benvenuto nel Movie Bot!** 🎬

Inviami il nome di un film o serie TV e ti troverò il link per guardarlo!

**Esempi:**
• Blue Beetle
• La Casa di Carta
• I Griffin
• Avengers

**Comandi disponibili:**
/help - Mostra questo messaggio
/search <titolo> - Cerca un titolo specifico

Basta scrivere il nome del titolo che vuoi cercare! 🍿
    """
    
    await update.message.reply_text(welcome_text, parse_mode='Markdown')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /help"""
    help_text = """
🆘 **Aiuto Movie Bot** 🆘

**Come usare il bot:**
1. Scrivi semplicemente il nome del film/serie che vuoi vedere
2. Il bot cercherà il titolo su TMDB
3. Ti verranno mostrate le opzioni disponibili
4. Scegli cosa vuoi guardare e riceverai il link!

**Esempi di ricerca:**
• `Blue Beetle` - Film del 2023
• `La Casa di Carta` - Serie TV completa
• `Avengers Endgame` - Film Marvel

**Note:**
• Per le serie TV, puoi scegliere stagioni ed episodi specifici
• I link possono richiedere qualche secondo per essere estratti
• Se non trovi quello che cerchi, prova con titoli diversi

Buona visione! 🎭
    """
    
    await update.message.reply_text(help_text, parse_mode='Markdown')

async def search_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /search"""
    if not context.args:
        await update.message.reply_text("❌ Devi specificare un titolo da cercare!\n\nEsempio: `/search Blue Beetle`", parse_mode='Markdown')
        return
    
    titolo = " ".join(context.args)
    # Importa qui per evitare import circolari
    from handlers.messages import gestisci_ricerca_media
    await gestisci_ricerca_media(update, context, titolo)