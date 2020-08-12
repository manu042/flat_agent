import time
import random
import logging.config
from tools.settings import settings
from tools.log_config import LOG_CONFIG_DICT
from immoscout.parser import ImmoScoutParser
from tools.save_expose import save_expose_details
from messenger.mail_messenger import MailMessenger

logging.config.dictConfig(LOG_CONFIG_DICT)
logger = logging.getLogger("default")


class FlatAgent:

    def __init__(self):
        self.parser = ImmoScoutParser()
        self.mail_messenger = MailMessenger()
        self.from_email = settings.DEFAULT_FROM_EMAIL
        self.to_email = settings.DEFAULT_TO_EMAIL

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
            self.send_error_msg(e)

    def agent(self):
        expose_links = self.parser.query_expose_links(settings.SEARCH_URL)

        new_results = 0
        for link in expose_links:
            expose_details = self.parser.query_expose_details(link)

            if isinstance(expose_details, dict):
                new_expose = save_expose_details(expose_details)

                if settings.ATTACHMENT:
                    attachment = self.parser.get_attachment(link)
                else:
                    attachment = None

                if new_expose:
                    new_results += 1

                    subject = self.parser.create_subject()
                    mail_body = self.parser.create_mail_body(expose_details)
                    msg = self.mail_messenger.create_message(self.from_email, self.to_email, subject, mail_body, attachment)
                    self.mail_messenger.send_mail(self.from_email, self.to_email, msg)
            else:
                logger.warning("HTTP status codes: " + expose_details)

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

    def send_error_msg(self, error_msg):
        subject = "FlatAgent - Fehlermeldung"
        mail_body = "FlatAgent wurde unerwartet beendet:\n{}".format(error_msg)
        msg = self.mail_messenger.create_message(self.from_email, self.to_email, subject, mail_body)
        self.mail_messenger.send_mail(self.from_email, self.to_email, msg)


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
