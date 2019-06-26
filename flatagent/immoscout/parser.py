import os
import requests
import datetime
from bs4 import BeautifulSoup

from tools.settings import settings


class ImmoScoutParser:

    def __init__(self):
        self.template_path = os.path.join(settings.BASE_PATH, "flatagent", "messenger", "body_template.html")

    def query_expose_links(self, search_url):
        r = requests.get(search_url)

        soup = BeautifulSoup(r.content, 'html.parser')

        # get search results from html as list
        results = soup.find_all("li", class_="result-list__listing")

        # get the expose links
        expose_links = []
        for result in results:
            link = result.find_all("a", href=True)[0]
            expose_link = link["href"]
            expose_link = "https://www.immobilienscout24.de{}".format(
                expose_link)

            expose_links.append(expose_link)

        return expose_links

    def query_expose_details(self, expose_link):
        time_stamp = datetime.datetime.now()
        time_stamp = datetime.datetime.strftime(time_stamp, "%Y-%m-%d %H:%M")

        r = requests.get(expose_link)
        encoded_text = r.text.encode("utf8")
        soup = BeautifulSoup(encoded_text, 'html.parser')

        # parse expose details from html
        expose_title = soup.find("h1", attrs={"data-qa": "expose-title"})
        cold_rent = soup.find("div", class_="is24qa-kaltmiete is24-value font-semibold")
        room_no = soup.find("div", class_="is24qa-zi is24-value font-semibold")
        area = soup.find("div", class_="is24qa-flaeche is24-value font-semibold")
        total_rent = soup.find("dd", class_="is24qa-gesamtmiete grid-item three-fifths font-bold")
        street = soup.find("span", class_="block font-nowrap print-hide")
        city_district = soup.find("span", class_="zip-region-and-country")
        text = soup.find("pre", class_="is24qa-lage text-content short-text")
        other_text = soup.find("pre", class_="is24qa-sonstiges text-content short-text")

        expose_details = {"expose_link": expose_link,
                          "expose_title": self.get_soup_text(expose_title),
                          "total_rent": self.get_soup_text(total_rent),
                          "cold_rent": self.get_soup_text(cold_rent),
                          "area": self.get_soup_text(area),
                          "room_no": self.get_soup_text(room_no),
                          "street": self.get_soup_text(street),
                          "city_district": self.get_soup_text(city_district),
                          "text": self.get_soup_text(text),
                          "request_date": time_stamp,
                          }

        return expose_details

    def get_soup_text(self, soup_match):
        try:
            soup_match = soup_match.text
        except:
            soup_match = None

        return soup_match

    def create_subject(self):
        return "Neues Angebot auf Immobilienscout24 gefunden"

    def create_mail_body(self, expose_details):
        expose_title = expose_details["expose_title"]
        total_rent = expose_details["total_rent"]
        cold_rent = expose_details["cold_rent"]
        area = expose_details["area"]
        street = expose_details["street"]
        city_district = expose_details["city_district"]
        expose_link = expose_details["expose_link"]

        with open(self.template_path) as fp:
            mail_body = fp.read()

        mail_body = mail_body.format(expose_title=expose_title,
                                     total_rent=total_rent,
                                     cold_rent=cold_rent,
                                     area=area,
                                     street=street,
                                     city_district=city_district,
                                     expose_link=expose_link,
                                     )

        return mail_body
