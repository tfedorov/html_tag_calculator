import yaml


def resolve(url_or_synoynm):
    synonyms = {}
    with open('synonyms.yaml', 'r') as f:
        synonyms = yaml.load(f)

    url = synonyms.get(url_or_synoynm, url_or_synoynm)
    if url.startswith("http://"):
        return url
    else:
        return "http://" + url
