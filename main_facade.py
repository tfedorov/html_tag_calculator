import custom_logger as cust_log
import page_reader as pr
import persistent_storage as storage
import tags_calculator as tags
import url_resolver as syn


class MainFacade:
    def __init__(self):
        self._storage = storage.PersistenceStorage()

    def synonym_keys(self):
        return [*syn.read_synonyms()]

    def get_command(self, url_or_synonym):
        try:
            valid_url = syn.resolve(url_or_synonym)
            page_content = pr.read_content(valid_url)
            cust_log.log(valid_url)
            tags_num = tags.calculate(page_content)
            self._storage.save(valid_url, tags_num)
            return tags_num
        except Exception as e:
            msg = "Url error: " + str(e)
            print(msg)
        return msg

    def view_command(self, url_or_synonym):
        try:
            valid_url = syn.resolve(url_or_synonym)
            return self._storage.load(valid_url)
        except Exception as e:
            msg = "Url error: " + str(e)
            print(msg)
        return [msg]
