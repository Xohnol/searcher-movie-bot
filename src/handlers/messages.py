import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from services.tmdb_service import cerca_media, ottieni_dettagli_serie, ottieni_episodi_stagione
from services.vixsrc_service import genera_url_vixsrc

async def gestisci_messaggio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Gestisce i messaggi di testo degli utenti"""
    titolo = update.message.text.strip()
    
    if not titolo:
        await update.message.reply_text("❌ Scrivi il nome di un film o serie TV che vuoi cercare!")
        return
    
    await gestisci_ricerca_media(update, context, titolo)

async def gestisci_ricerca_media(update: Update, context: ContextTypes.DEFAULT_TYPE, titolo: str):
    """Gestisce la ricerca di un titolo"""
    # Mostra messaggio di ricerca
    messaggio_ricerca = await update.message.reply_text(f"🔍 Cercando: **{titolo}**...", parse_mode='Markdown')
    
    # Cerca il media
    risultato = cerca_media(titolo)
    
    if not risultato:
        await messaggio_ricerca.edit_text(f"❌ Nessun risultato trovato per: **{titolo}**\n\nProva con un titolo diverso!", parse_mode='Markdown')
        return
    
    tipo = risultato["media_type"]
    nome = risultato.get("title") or risultato.get("name", "Sconosciuto")
    anno = (risultato.get("release_date") or risultato.get("first_air_date", ""))[:4]
    
    await messaggio_ricerca.edit_text(f"✅ Trovato: **{nome}** ({anno})\nTipo: {'Film' if tipo == 'movie' else 'Serie TV'}", parse_mode='Markdown')
    
    if tipo == "movie":
        await gestisci_film(update, context, risultato)
    elif tipo == "tv":
        await gestisci_serie_tv(update, context, risultato)

async def gestisci_film(update: Update, context: ContextTypes.DEFAULT_TYPE, film_info):
    """Gestisce la richiesta di un film"""
    nome = film_info["title"]
    anno = film_info.get("release_date", "????")[:4]
    
    try:
        # Genera URL Vixsrc diretto
        url_vixsrc = genera_url_vixsrc(film_info)
        
        testo_risposta = f"""
🎬 **{nome}** ({anno})

🔗 **Link streaming:**
{url_vixsrc}

📝 **Istruzioni:**
• Clicca sul link sopra
• Aspetta che la pagina carichi
• Premi play per guardare il film! 🍿
        """
        
        await update.message.reply_text(testo_risposta, parse_mode='Markdown')
        
    except Exception as e:
        await update.message.reply_text(f"❌ Errore nella generazione del link per **{nome}**\n\nRiprova più tardi!", parse_mode='Markdown')

async def gestisci_serie_tv(update: Update, context: ContextTypes.DEFAULT_TYPE, serie_info):
    """Gestisce la richiesta di una serie TV"""
    nome = serie_info["name"]
    serie_id = serie_info["id"]
    anno = serie_info.get("first_air_date", "????")[:4]
    
    # Ottieni dettagli serie
    dettagli = ottieni_dettagli_serie(serie_id)
    numero_stagioni = dettagli.get("number_of_seasons", 0)
    
    if numero_stagioni == 0:
        await update.message.reply_text(f"❌ Nessuna stagione trovata per **{nome}**", parse_mode='Markdown')
        return
    
    # Crea bottoni per le stagioni
    keyboard = []
    for stagione in range(1, min(numero_stagioni + 1, 21)):  # Max 20 stagioni per limitare
        keyboard.append([InlineKeyboardButton(f"Stagione {stagione}", callback_data=f"stagione_{serie_id}_{stagione}")])
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    testo = f"""
📺 **{nome}** ({anno})

Seleziona una stagione:
🔢 Stagioni disponibili: {numero_stagioni}
    """
    
    await update.message.reply_text(testo, reply_markup=reply_markup, parse_mode='Markdown')

async def gestisci_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Gestisce i callback dei bottoni inline"""
    query = update.callback_query
    await query.answer()
    
    data = query.data
    
    if data.startswith("stagione_"):
        parti = data.split("_")
        serie_id = int(parti[1])
        numero_stagione = int(parti[2])
        
        await mostra_episodi_stagione(query, context, serie_id, numero_stagione)
    
    elif data.startswith("episodio_"):
        parti = data.split("_")
        serie_id = int(parti[1])
        numero_stagione = int(parti[2])
        numero_episodio = int(parti[3])
        
        await fornisci_link_episodio(query, context, serie_id, numero_stagione, numero_episodio)
    
    elif data.startswith("torna_serie_"):
        serie_id = int(data.split("_")[2])
        # Simula info serie per tornare indietro
        serie_info = {"id": serie_id, "name": "Serie TV", "first_air_date": "2023"}
        await gestisci_serie_tv_callback(query, context, serie_info)

async def mostra_episodi_stagione(query, context, serie_id, numero_stagione):
    """Mostra gli episodi di una stagione"""
    episodi = ottieni_episodi_stagione(serie_id, numero_stagione)
    
    if not episodi:
        await query.edit_message_text(f"❌ Nessun episodio trovato per la stagione {numero_stagione}")
        return
    
    # Crea bottoni per episodi (max 20 per pagina)
    keyboard = []
    for episodio in episodi[:20]:  # Limita a 20 episodi
        num_ep = episodio["episode_number"]
        nome_ep = episodio.get("name", f"Episodio {num_ep}")
        
        # Accorcia il nome se troppo lungo
        if len(nome_ep) > 25:
            nome_ep = nome_ep[:22] + "..."
        
        keyboard.append([InlineKeyboardButton(
            f"E{num_ep:02d}: {nome_ep}", 
            callback_data=f"episodio_{serie_id}_{numero_stagione}_{num_ep}"
        )])
    
    # Bottone per tornare indietro
    keyboard.append([InlineKeyboardButton("⬅️ Torna alle stagioni", callback_data=f"torna_serie_{serie_id}")])
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    testo = f"""
📺 **Stagione {numero_stagione}**

Seleziona un episodio:
📋 Episodi disponibili: {len(episodi)}
    """
    
    await query.edit_message_text(testo, reply_markup=reply_markup, parse_mode='Markdown')

async def fornisci_link_episodio(query, context, serie_id, numero_stagione, numero_episodio):
    """Fornisce il link per un episodio specifico"""
    try:
        # Simula info episodio
        episodio_info = {
            "id": serie_id,
            "media_type": "tv"
        }
        
        # Genera URL Vixsrc diretto
        url_vixsrc = genera_url_vixsrc(episodio_info, numero_stagione, numero_episodio)
        
        testo_risposta = f"""
📺 **Stagione {numero_stagione} - Episodio {numero_episodio}**

🔗 **Link streaming:**
{url_vixsrc}

📝 **Istruzioni:**
• Clicca sul link sopra
• Aspetta che la pagina carichi  
• Premi play per guardare l'episodio! 🍿
        """
        
        await query.edit_message_text(testo_risposta, parse_mode='Markdown')
        
    except Exception as e:
        await query.edit_message_text(f"❌ Errore nella generazione del link per S{numero_stagione:02d}E{numero_episodio:02d}\n\nRiprova più tardi!")

async def gestisci_serie_tv_callback(query, context, serie_info):
    """Gestisce il ritorno alla selezione stagioni"""
    # Reimposta la selezione stagioni
    await gestisci_serie_tv(query, context, serie_info)