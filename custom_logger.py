import logging
import time

logging.basicConfig(filename='special_file.log',level=logging.DEBUG)


def log(url):
    now = time.strftime("%c")
    logging.debug(f"{now} {url}")
