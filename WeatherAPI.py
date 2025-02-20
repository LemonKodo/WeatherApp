import requests

class WeatherAPI:
    def __init__(self, api_key):
        self._api_key = api_key
        self._base_url = "https://api.openweathermap.org/data/2.5/weather"

    def _get_request(self, params):
        try:
            response = requests.get(self._base_url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Ошибка запроса: {e}")
            return None

    def get_weather_by_city(self, city_name):
        params = {"q": city_name, "units": "metric", "lang": "ru", "appid": self._api_key}
        data = self._get_request(params)
        return self._parse_weather_data(data) if data else None

    def get_weather_by_coords(self, lat, lon):
        params = {"lat": lat, "lon": lon, "units": "metric", "lang": "ru", "appid": self._api_key}
        data = self._get_request(params)
        return self._parse_weather_data(data) if data else None

    def _parse_weather_data(self, data):
        return {
            "name": data.get("name", "Неизвестное место"),
            "temp": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "lat": data["coord"]["lat"],
            "lon": data["coord"]["lon"]
        }
