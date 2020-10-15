import requests
from bs4 import BeautifulSoup
from helper import inner_html


def get_coordinates(place):
    url = f"https://www.gps-latitude-longitude.com/gps-coordinates-of-{place}"
    headers = {
        "Accept":
            "text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, * / *;q = 0.8"
    }
    response = requests.get(url=url, headers=headers)
    print(response.status_code)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        longitude = soup.select(
            'div.inputfield:nth-child(5) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(2) '
            '> td:nth-child(2)')
        latitude = soup.select(
            'div.inputfield:nth-child(5) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(1) > '
            'td:nth-child(2)')
        return [float(inner_html(longitude)), float(inner_html(latitude))]
