import logging
import time

from tags_extractor import yaml_reader as yaml, PersistenceStorage, tags_utils as tags, page_reader as pr


class MainFacade:
    def __init__(self):
        self._storage = PersistenceStorage()
        self._synonyms = yaml.read_file('synonyms.yaml')
        logging.basicConfig(filename='./special_file.log')

    def synonym_keys(self):
        """Return a list of all synonyms (from synonyms.yaml)."""
        return [*self._synonyms]

    def get_command(self, input_site):
        """Get command method. Resolved logic:
            1. Resolved url according to 'synonyms.yaml'
            2. Load url content
            3. Calculate tags
            4. Save to SqlLite
            5. Return result
            """
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
        """View command method. Resolved logic:
            1. Resolved url according to 'synonyms.yaml'
            2. Load from SqlLite
            3. Return result
            """
        try:
            resolved_url = self._synonyms.get(input_site, input_site)
            extracted_result = self._storage.load(resolved_url)
            return extracted_result
        except Exception as e:
            msg = "Url error: " + str(e)
            logging.error(time.strftime("%c") + msg)
        return [msg]
