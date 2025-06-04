def format_message(title, link):
    return f"🎬 Ecco il link per '{title}': {link}"

def handle_error(error_message):
    return f"❌ Si è verificato un errore: {error_message}"

def extract_title_from_message(message):
    # Assuming the title is the entire message for simplicity
    return message.strip()