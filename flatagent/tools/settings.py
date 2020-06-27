import os
import yaml
from tools.decorators import singleton


@singleton
class Settings:

    BASE_PATH = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    LOG_FILE_PATH = os.path.join(BASE_PATH, "logs", "flat_agent.log")
    JSON_FILE_PATH = os.path.join(BASE_PATH, "data", "real_estate.json")

    def __init__(self):
        # load config file
        config_path = os.path.join(self.BASE_PATH, "flatagent", "tools", "config.yaml")
        with open(config_path) as fp:
            config = yaml.load(fp, Loader=yaml.FullLoader)

        # Load Mail settings
        self.EMAIL_HOST = config["MAIL_SETTINGS"]["EMAIL_HOST"]
        self.EMAIL_HOST_PORT = config["MAIL_SETTINGS"]["EMAIL_HOST_PORT"]
        self.EMAIL_HOST_USER = config["MAIL_SETTINGS"]["EMAIL_HOST_USER"]
        self.EMAIL_HOST_PASSWORD = config["MAIL_SETTINGS"]["EMAIL_HOST_PASSWORD"]
        self.DEFAULT_FROM_EMAIL = config["MAIL_SETTINGS"]["DEFAULT_FROM_EMAIL"]
        self.DEFAULT_TO_EMAIL = config["MAIL_SETTINGS"]["DEFAULT_TO_EMAIL"]

        # Load Telegram settings
        self.TELEGRAM_TOKEN = config["TELEGRAM_SETTINGS"]["TOKEN"]
        self.CHAT_ID = config["TELEGRAM_SETTINGS"]["CHAT_ID"]

        # Load Immobilienscout24 settings
        self.SEARCH_URL = config["IMMO_SCOUT_24"]["SEARCH_URL"]
        self.ATTACHMENT = config["IMMO_SCOUT_24"]["ATTACHMENT"]


settings = Settings()
