import time
import random
import logging.config
from tools.settings import settings
from tools.log_config import LOG_CONFIG_DICT
from immoscout.parser import ImmoScoutParser
from tools.save_expose import save_expose_details
from messenger.telegram_messenger import TelegramMessenger

logging.config.dictConfig(LOG_CONFIG_DICT)
logger = logging.getLogger("default")


class FlatAgent:

    def __init__(self):
        self.parser = ImmoScoutParser()
        self.telegram_messenger = TelegramMessenger()

    def run_agent(self):
        try:
            while True:
                logger.info("Scrap new results")
                self.agent()
                sleep_time = self.__calc_sleep_time()
                logger.info("Sleep for {} seconds.".format(sleep_time))
                time.sleep(sleep_time)
        except Exception as e:
            logger.error("Programm failed with the following error:\n{}".format(e))

    def agent(self):
        expose_links = self.parser.query_expose_links(settings.SEARCH_URL)

        new_results = 0
        for link in expose_links:
            expose_details = self.parser.query_expose_details(link)
            new_expose = save_expose_details(expose_details)

            if new_expose:
                new_results += 1
                msg = self.telegram_messenger.create_text_msg(expose_details)
                self.telegram_messenger.send_message(msg)

        if new_results > 1:
            print("Es wurden {} neue Immobilien gefunden".format(new_results))
        elif new_results == 1:
            print("Es wurde eine neue Immobilie gefunden")
        else:
            print("Keine neue Immobilie gefunden")

    def __calc_sleep_time(self):
        mul = random.randint(3, 6)
        add = random.randint(0, 20)
        sec = 60 * mul + add

        return sec


def main():
    while True:
        try:
            agent = FlatAgent()
            agent.run_agent()
        except KeyboardInterrupt:
            break
        except Exception as e:
            time.sleep(60)


if __name__ == '__main__':
    main()
