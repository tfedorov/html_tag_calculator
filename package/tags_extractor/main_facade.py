import logging
import time

from tags_extractor import synonyms_reader as syn, PersistenceStorage, tags_utils as tags, page_reader as pr


class MainFacade:
    def __init__(self):
        self._storage = PersistenceStorage()
        self._synonyms = syn.read_synonyms('synonyms.yaml')
        logging.basicConfig(filename='./special_file.log')

    def synonym_keys(self):
        return [*self._synonyms]

    def get_command(self, input_site):

        resolved_url = self._synonyms.get(input_site, input_site)
        try:
            page_content = pr.read_content(resolved_url)

            logging.debug(time.strftime("%c") + resolved_url)
            tags_num = tags.calculate(page_content)

            self._storage.save(resolved_url, tags_num)
            result_str = tags.print_pr(tags_num)
            return result_str
        except Exception as e:
            msg = str(resolved_url) + " " + str(e)
            logging.error(time.strftime("%c") + msg)
        return msg

    def view_command(self, input_site):
        try:
            resolved_url = self._synonyms.get(input_site, input_site)
            result_str = self._storage.load(resolved_url)
            return result_str
        except Exception as e:
            msg = "Url error: " + str(e)
            logging.error(time.strftime("%c") + msg)
        return [msg]
