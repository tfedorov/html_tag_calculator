import logging
import time

from logic import synonyms_reader as syn, PersistenceStorage, tags_utils as tags, page_reader as pr


class MainFacade:
    def __init__(self):
        self._storage = PersistenceStorage()
        self._synonyms = syn.read_synonyms('synonyms.yaml')
        logging.basicConfig(filename='./special_file.log')

    def synonym_keys(self):
        return [*self._synonyms]

    def get_command(self, url_or_synonym):

        resolved_url = self._synonyms.get(url_or_synonym)
        try:
            page_content = pr.read_content(resolved_url)

            logging.debug(time.strftime("%c") + resolved_url)
            tags_num = tags.calculate(page_content)

            self._storage.save(resolved_url, tags_num)
            return tags_num
        except Exception as e:
            msg = resolved_url + " " + str(e)
            logging.error(time.strftime("%c") + msg)
        return msg

    def view_command(self, url_or_synonym):
        try:
            resolved_url = self._synonyms.get(url_or_synonym)
            return self._storage.load(resolved_url)
        except Exception as e:
            msg = "Url error: " + str(e)
            print(msg)
        return [msg]
