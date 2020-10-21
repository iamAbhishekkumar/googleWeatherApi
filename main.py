import requests
from bs4 import BeautifulSoup
from coordinates import get_coordinates
from helper import inner_html
from details import today_forecast, today_weather_details, daily_forecast,hourly_forecast
from flask import Flask, jsonify

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/place/<query>')
def get_weather(query):
    coordinates = get_coordinates(query)
    longitude = coordinates[0]
    latitude = coordinates[1]
    url = f"https://weather.com/en-IN/weather/today/l/{latitude},{longitude}?par=google&temp=c"
    headers = {
        "Accept":
            "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
    }
    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    current_temperature = inner_html(soup.select('.CurrentConditions--tempValue--3KcTQ'))
    place = inner_html(soup.select('.CurrentConditions--location--1Ayv3'))
    weather_map = {
        "current_temp": current_temperature,
        "place": place,
        "today_weather_details": today_weather_details(soup),
        "today_forecast": today_forecast(soup),
        "hourly_forecast": hourly_forecast(soup),
        "daily_forecast": daily_forecast(soup)

    }

    return jsonify(weather_map)


@app.route('/cr/<query>')
def get_coordinate(query):
    coordinates = get_coordinates(query)
    coordinate_map = {
        "longitude": coordinates[0],
        "latitude": coordinates[1],
    }
    return jsonify(coordinate_map)


if __name__ == '__main__':
    app.run()
