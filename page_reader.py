from urllib.request import urlopen


def read_content(url):
    try:
        opener = urlopen(url)
        content_bytes = opener.read()
        return str(content_bytes)
    except Exception as e:
        print("Unexpected error:" + e)
        return ""
