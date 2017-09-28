import custom_logger as clog
import page_reader as pr
import persistent_storage as ps
import tags_calculator as tags


def get(url):
    page_content = pr.read_content(url)
    clog.log(url)
    tags_num = tags.calculate(page_content)
    print(tags_num)

    ps.save(url, tags_num)


def view(url):
    for r in ps.load(url):
        print(r)


def init():
    ps.init()


init()
get("http://google.com")
get("http://google.com")
view("http://google.com")
