import requests
from utils.config import TMDB_API_KEY, TMDB_BASE_URL, TMDB_HEADERS

def cerca_tmdb(titolo):
    """Cerca film o serie TV su TMDB (compatibilità)"""
    return cerca_media(titolo)

def cerca_media(titolo):
    """Cerca film o serie TV su TMDB"""
    params = {"api_key": TMDB_API_KEY, "query": titolo}
    url = f"{TMDB_BASE_URL}/search/multi"
    
    try:
        risposta = requests.get(url, params=params, headers=TMDB_HEADERS)
        risultati = risposta.json().get("results", [])
        
        if not risultati:
            return None
        
        # Logica di selezione migliorata
        migliore_risultato = None
        
        # Per "la casa di carta"
        if "casa di carta" in titolo.lower():
            for risultato in risultati:
                nome = risultato.get("name", "").lower()
                if "money heist" in nome and "berlin" not in nome and "korea" not in nome:
                    migliore_risultato = risultato
                    break
        
        # Per "i Griffin"
        elif "griffin" in titolo.lower():
            for risultato in risultati:
                nome = (risultato.get("name") or "").lower()
                titolo_alt = (risultato.get("title") or "").lower()
                if "family guy" in nome or "family guy" in titolo_alt:
                    migliore_risultato = risultato
                    break
        
        # Se non trovato con logica specifica, prendi il primo
        if not migliore_risultato:
            migliore_risultato = risultati[0]
        
        return migliore_risultato
    
    except Exception as e:
        print(f"Errore nella ricerca TMDB: {e}")
        return None

def ottieni_dettagli_serie(serie_id):
    """Ottiene dettagli completi di una serie TV"""
    url = f"{TMDB_BASE_URL}/tv/{serie_id}"
    params = {"api_key": TMDB_API_KEY}
    
    try:
        risposta = requests.get(url, params=params, headers=TMDB_HEADERS)
        if risposta.status_code == 200:
            return risposta.json()
        return {}
    except Exception as e:
        print(f"Errore dettagli serie: {e}")
        return {}

def ottieni_episodi_stagione(serie_id, numero_stagione):
    """Ottiene episodi di una stagione specifica"""
    url = f"{TMDB_BASE_URL}/tv/{serie_id}/season/{numero_stagione}"
    params = {"api_key": TMDB_API_KEY}
    
    try:
        risposta = requests.get(url, params=params, headers=TMDB_HEADERS)
        if risposta.status_code == 200:
            dati_stagione = risposta.json()
            return dati_stagione.get("episodes", [])
        return []
    except Exception as e:
        print(f"Errore episodi stagione: {e}")
        return []