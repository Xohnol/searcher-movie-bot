def genera_url_vixsrc(media_info, stagione=None, episodio=None):
    """Genera URL Vixsrc basato sul tipo di media"""
    media_id = media_info["id"]
    
    if media_info["media_type"] == "movie":
        return f"https://vixsrc.to/movie/{media_id}"
    elif media_info["media_type"] == "tv" and stagione and episodio:
        return f"https://vixsrc.to/tv/{media_id}/{stagione}/{episodio}"
    
    return None