import yaml


def read_file(file_name):
    synonyms = {}
    with open(file_name, 'r') as f:
        synonyms = yaml.load(f)
    return synonyms
