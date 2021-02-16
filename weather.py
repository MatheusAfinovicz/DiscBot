import requests
import json


def weather(query):
    with open('keys/weather_api_key') as archive:
        for token in archive:
            weather_token = token

    language = 'pt_br'

    url = f'http://api.openweathermap.org/data/2.5/weather?q={query}&appid={weather_token}&lang={language}'

    json_response = requests.request('GET', url).text
    response = json.loads(json_response)

    description = response['weather'][0]['description']
    temp = round(response['main']['temp'] - 273)
    feels_like = round(response['main']['feels_like'] - 273)
    humidity = response['main']['humidity']

    response = {'description': description,
                'temp': temp,
                'feels_like': feels_like,
                'humidity': humidity}

    return response


if __name__ == '__main__':
    print(weather('guarapuava'))
    print(weather('são paulo'))
    print(weather('sla'))
