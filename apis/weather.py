import requests
import json


def creates_formatted_string(response: dict) -> str:

    if response['cod'] == '404':
        return 'Cidade não encontrada.'

    if response['cod'] == 401:
        print('Invalid API Key!')
        return 'Algo não está certo, tente novamente mais tarde.'

    if response['cod'] == 429:
        print('Limit of requisition exceeded!')
        return 'Estou cansado de tantas buscas, tente novamente mais tarde.'

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


def weather(query: str, token: str) -> str:

    try:

        if query == '' or query == ' ' * len(query):
            return 'A cidade não pode ser vazia.'

        if isinstance(query, (int, float)):
            return 'A cidade não pode ser um número.'

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


if __name__ == '__main__':
    print(weather('guarapuava', 'not_a_key'))
