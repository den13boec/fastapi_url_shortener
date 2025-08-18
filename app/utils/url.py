from urllib.parse import urlparse

ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def is_valid_http_url(url: str) -> bool:
    try:
        p = urlparse(url.strip())
        # check if the scheme is http or https and if netloc is present
        return p.scheme in {"http", "https"} and bool(p.netloc)
    except Exception:
        return False
