import custom_logger as cust_log
import page_reader as pr
import persistent_storage as storage
import tags_calculator as tags
import url_synonyms_resolver as syn


def get(url_or_synonym):
    valid_url = syn.resolve(url_or_synonym)

    page_content = pr.read_content(valid_url)
    cust_log.log(valid_url)

    tags_num = tags.calculate(page_content)

    storage.save(valid_url, tags_num)

    return tags_num


def view(url):
    return [r for r in storage.load(url)]


def init():
    storage.init()


init()
get("http://google.com")
get("ggl")
print(view("http://google.com"))
