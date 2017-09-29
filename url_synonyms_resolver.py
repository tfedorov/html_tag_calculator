import yaml


def read_synonyms():
    synonyms = {}
    with open('synonyms.yaml', 'r') as f:
        synonyms = yaml.load(f)
    return synonyms


def resolve(url_or_synoynm):
    synonyms = read_synonyms()

    url = synonyms.get(url_or_synoynm, url_or_synoynm)
    if url.startswith("http://") or url.startswith("https://"):
        return url
    else:
        return "http://" + url
