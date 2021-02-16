import discord
from search import search
from weather import weather

client = discord.Client()

commands = ['!help -> Escrevo uma lista com meus comandos',
            '!wiki "algo" -> Busco algo na wikipedia para você!',
            '!salve -> Te mando um salve!',
            '!tempo "cidade" -> Te informo o tempo em uma cidade']


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
        if query == ''*len(query):
            await message.channel.send('A cidade não pode ser vazia.')
        else:
            response = weather(query)
            string = f'{query.upper()}:\n' \
                     f'Condição: {response["description"]}\n' \
                     f'Temperatura atual: {response["temp"]}ºC    Sensação Térmica: {response["feels_like"]}ºC\n' \
                     f'Humidade: {response["humidity"]}%'

            await message.channel.send(string)

with open('keys/disc_api_key') as archive:
    for key in archive:
        disc_token = key

client.run(disc_token)
