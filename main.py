import discord
from search import search

client = discord.Client()

commands = ['!help -> Escrevo uma lista com meus comandos',
            '!wiki "algo" -> Busco algo na wikipedia para você!',
            '!salve -> Te mando um salve!']


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
        await message.channel.send(f'Salve {author[0]} =)')

    if message.content.startswith('!wiki'):
        query = message.content[8:]
        if query == ''*len(query):
            await message.channel.send('A busca não pode ser vazia.')
        else:
            answer = search(query)
            await message.channel.send(answer + '.')

with open('keys/disc_api_key') as archive:
    for key in archive:
        disc_key = key

client.run(disc_key)
