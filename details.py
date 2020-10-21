from helper import inner_html, remove_tags


def hourly_forecast(soup):
    temp_map = {}
    for i in range(1, 6):
        time = inner_html(soup.select(
            f'.HourlyWeatherCard--TableWrapper--2kboH > ul:nth-child(1) > li:nth-child({i}) > a:nth-child(1) > h3:nth-child(1) > span:nth-child(1)'))
        temp = inner_html(soup.select(
            f'.HourlyWeatherCard--TableWrapper--2kboH > ul:nth-child(1) > li:nth-child({i}) > a:nth-child(1) > div:nth-child(2) > span:nth-child(1)'))
        precipitation = remove_tags(str(soup.select(
            f'.HourlyWeatherCard--TableWrapper--2kboH > ul:nth-child(1) > li:nth-child({i}) > a:nth-child(1) > div:nth-child(4)')[0]))
        temp_map[i] = {

            "time": time,
            "highest_temp": temp,
            "precipitation": precipitation
        }
    return temp_map


def daily_forecast(soup):
    temp_map = {}
    for i in range(1, 6):
        time = inner_html(soup.select(
            f".DailyWeatherCard--TableWrapper--12r1N > ul:nth-child(1) > li:nth-child({i}) > a:nth-child(1) > "
            f"h3:nth-child(1) > span:nth-child(1)"))
        highest_temp = inner_html(soup.select(
            f".DailyWeatherCard--TableWrapper--12r1N > ul:nth-child(1) > li:nth-child({i}) > a:nth-child(1) > "
            f"div:nth-child(2) > span:nth-child(1)"))
        lowest_temp = inner_html(soup.select(
            f".DailyWeatherCard--TableWrapper--12r1N > ul:nth-child(1) > li:nth-child({i}) > a:nth-child(1) > "
            f"div:nth-child(3) > span:nth-child(1)"))
        precipitation = remove_tags(str(soup.select(
            f".DailyWeatherCard--TableWrapper--12r1N > ul:nth-child(1) > li:nth-child({i}) > a:nth-child(1) > "
            f"div:nth-child(5)")[0]))
        temp_map[i] = {
            "time": time,
            "highest_temp": highest_temp,
            "lowest_temp": lowest_temp,
            "precipitation": precipitation
        }
    return temp_map


def today_forecast(soup):
    time = ["morning", "afternoon", "evening", "night"]
    temp_map = {}
    i = 1
    for t in time:
        precip_selector = f'.WeatherTable--wide--YogM9 > li:nth-child({i}) > a:nth-child(1) > div:nth-child(4)'
        try:
            temp_map[t] = {
                "temperature": inner_html(soup.select(
                    f'.WeatherTable--wide--YogM9 > li:nth-child({i}) > a:nth-child(1) > div:nth-child(2) > '
                    f'span:nth-child(1)')),
                "precipitation": remove_tags(str(soup.select(precip_selector)[0])),
            }
        except IndexError:
            precip_selector = f'li.Column--active--FeXwd:nth-child({i}) > a:nth-child(1) > div:nth-child(4)'
            temp_map[t] = {
                "temperature": inner_html(soup.select(
                    f'.WeatherTable--wide--YogM9 > li:nth-child({i}) > a:nth-child(1) > div:nth-child(2) > '
                    f'span:nth-child(1)')),
                "precipitation": remove_tags(str(soup.select(precip_selector)[0]))
            }

        finally:
            i += 1
    return temp_map


def today_weather_details(soup):
    weather_type = inner_html(soup.select('.CurrentConditions--phraseValue--2xXSr'))
    avg_temperature = inner_html(soup.select('.TodayDetailsCard--feelsLikeTempValue--2aogo'))
    wind_speed = remove_tags(inner_html(soup.select('.Wind--windWrapper--1Va1P')))
    humidity = inner_html(
        soup.select('div.ListItem--listItem--1r7mf:nth-child(3) > div:nth-child(3) > span:nth-child(1)'))
    pressure = remove_tags(inner_html(soup.select('.Pressure--pressureWrapper--3olKd')))
    uv_index = inner_html(
        soup.select('div.ListItem--listItem--1r7mf:nth-child(6) > div:nth-child(3) > span:nth-child(1)'))
    visibility = inner_html(
        soup.select('div.ListItem--listItem--1r7mf:nth-child(7) > div:nth-child(3) > span:nth-child(1)'))
    moon_phase = inner_html(soup.select('div.ListItem--listItem--1r7mf:nth-child(8) > div:nth-child(3)'))
    temp_map = {
        "weather_type": weather_type,
        "avg_temperature": avg_temperature,
        "wind_speed": wind_speed,
        "humidity": humidity,
        "pressure": pressure,
        "uv_index": uv_index,
        "visibility": visibility,
        "moon_phase": moon_phase,
    }
    return temp_map
