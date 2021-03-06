import requests
import json


def creates_formatted_string(response: dict) -> str:

    if response['cod'] == '404':
        return 'Cidade não encontrada.'

    city = response['name']
    description = response['weather'][0]['description']
    temp = round(response['main']['temp'] - 273)
    feels_like = round(response['main']['feels_like'] - 273)
    humidity = response['main']['humidity']

    response = f'{city.upper()}:\n' \
               f'Condição: {description}\n' \
               f'Temperatura atual: {temp}ºC    Sensação Térmica: {feels_like}ºC\n' \
               f'Humidade: {humidity}%'

    return response


def weather(query: str) -> str:

    try:

        if query == '' or query == ' ' * len(query):
            return 'A cidade não pode ser vazia.'

        if isinstance(query, (int, float)):
            return 'A cidade não pode ser um número.'

        with open('../keys/weather_api_key') as archive:
            for token in archive:
                weather_token = token

        language = 'pt_br'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={query}&appid={weather_token}&lang={language}'

        json_response = requests.request('GET', url).text
        response = json.loads(json_response)

        answer = creates_formatted_string(response)

        return answer

    except TypeError:
        return 'A cidade não pode ser um número.'

    except KeyError:
        return 'Cidade não encontrada.'
