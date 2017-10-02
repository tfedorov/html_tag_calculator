from urllib.request import urlopen


def read_content(target_url):
    normalized_url = _normalize_url(target_url)
    opener = urlopen(normalized_url)
    content_bytes = opener.read()
    return str(content_bytes)


def _normalize_url(target_url):
    if target_url.startswith("http://") or target_url.startswith("https://"):
        return target_url
    else:
        return "http://" + target_url
