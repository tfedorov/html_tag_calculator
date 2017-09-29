from urllib.request import urlopen


def read_content(url):
    opener = urlopen(url)
    content_bytes = opener.read()
    return str(content_bytes)
