import requests

API_KEY = "153b805e21c7eeca1f6c1edda08e396d"


def get_data(city_name, forecast=None):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast
    filtered_data = filtered_data[:nr_values]
    return filtered_data


if __name__ == "__main__":
    print(get_data(city_name="Tokyo", forecast=3))
