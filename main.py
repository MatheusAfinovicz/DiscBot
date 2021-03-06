import discord
from apis.search import search
from apis.weather import weather


commands = ['!help -> Escrevo uma lista com meus comandos',
            '!wiki "algo" -> Busco algo na wikipedia para você!',
            '!salve -> Te mando um salve!',
            '!tempo "cidade" -> Te informo o tempo de uma cidade']


client = discord.Client()


@client.event
async def on_ready():
    print(f'I logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!help'):
        await message.channel.send('Lista de comandos:')
        for command in commands:
            await message.channel.send(command)

    if message.content.startswith('!salve'):
        author = str(message.author).split('#')
        await message.channel.send(f'Salve {author[0]}   =)')

    if message.content.startswith('!wiki'):
        query = message.content[6:]
        response = search(query)
        await message.channel.send(response)

    if message.content.startswith('!tempo'):
        query = message.content[7:]

        with open('keys/weather_api_key') as key_archive:
            for token in key_archive:
                weather_token = token

        response = weather(query, weather_token)

        await message.channel.send(response)


with open('keys/disc_api_key') as archive:
    for key in archive:
        disc_token = key

client.run(disc_token)
