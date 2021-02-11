import discord

client = discord.Client()

commands = ['!help -> Escrevo uma lista com meus comandos',
            '!buscar "algo" -> Busco no Google e escrevo aqui para você!',
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
        await message.channel.send('Salve')

    if message.content.startswith('!buscar'):
        search = message.content[8:]
        print(search)
        # parei aqui (integrar 'new search engine')

with open('keys/disc_api_key') as archive:
    for key in archive:
        disc_key = key

client.run(disc_key)
