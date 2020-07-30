import os
from tools.decorators import singleton


@singleton
class Settings:
    BASE_PATH = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    LOG_FILE_PATH = os.path.join(BASE_PATH, "logs", "flat_agent.log")
    JSON_FILE_PATH = os.path.join(BASE_PATH, "data", "real_estate.json")

    def __init__(self):
        # Load Mail settings
        self.EMAIL_HOST = os.environ["EMAIL_HOST"]
        self.EMAIL_HOST_PORT = os.environ["EMAIL_PORT"]
        self.EMAIL_HOST_USER = os.environ["EMAIL_USER"]
        self.EMAIL_HOST_PASSWORD = os.environ["EMAIL_PASSWORD"]
        self.DEFAULT_FROM_EMAIL = os.environ["DEFAULT_FROM_EMAIL"]
        self.DEFAULT_TO_EMAIL = os.environ["DEFAULT_TO_EMAIL"]

        # Load Immobilienscout24 settings
        self.SEARCH_URL = os.environ["SEARCH_URL"]
        self.ATTACHMENT = os.environ.get("ATTACHMENT", False)


settings = Settings()
