import os
import requests

NEWS_API_BASE = "https://newsapi.org/v2"
API_KEY = os.getenv("NEWSAPI_KEY")

class NewsAPIError(Exception):
    pass

def _auth_headers():
    if not API_KEY:
        raise NewsAPIError("NEWSAPI_KEY is not set")
    return {"X-Api-Key": API_KEY}

def get_top_headlines(country="us", page_size=20):
    url = f"{NEWS_API_BASE}/top-headlines"
    params = {"country": country, "pageSize": page_size}
    resp = requests.get(url, headers=_auth_headers(), params=params, timeout=10)
    if resp.status_code != 200:
        raise NewsAPIError(f"NewsAPI error {resp.status_code}: {resp.text}")
    return resp.json()

def search_everything(q, page_size=20, sort_by="publishedAt", language="en"):
    url = f"{NEWS_API_BASE}/everything"
    params = {
        "q": q,
        "pageSize": page_size,
        "sortBy": sort_by,
        "language": language
    }
    resp = requests.get(url, headers=_auth_headers(), params=params, timeout=10)
    if resp.status_code != 200:
        raise NewsAPIError(f"NewsAPI error {resp.status_code}: {resp.text}")
    return resp.json()
