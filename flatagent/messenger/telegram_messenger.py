from telegram import Bot, ParseMode, Document
from tools.settings import settings

msg_template = """{expose_title}

- Gesamtmiete: {total_rent}
- Kaltimiete: {cold_rent}
- Fläche: {area}
- Straße: {street}
- Stadtteil: {city_district}
- Link: {expose_link}
"""


class TelegramMessenger:

    def __init__(self):
        self.token = settings.TELEGRAM_TOKEN
        self.chat_id = settings.CHAT_ID
        self.bot = Bot(self.token)

    def send_message(self, text):
        self.bot.send_message(self.chat_id, text=text, parse_mode=ParseMode.HTML)

    @staticmethod
    def create_text_msg(expose_details):
        text_msg = msg_template.format(expose_title=expose_details["expose_title"],
                                       total_rent=expose_details["total_rent"],
                                       cold_rent=expose_details["cold_rent"],
                                       area=expose_details["area"],
                                       street=expose_details["street"],
                                       city_district=expose_details["city_district"],
                                       expose_link=expose_details["expose_link"],
                                       )
        return text_msg
