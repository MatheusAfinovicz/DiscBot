import discord
import json

client = discord.Client()

commands = ['!help -> returns a command list',
            '!google "word" -> returns the meaning of the word',
            '!coe -> returns "coé"']


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

    if message.content.startswith('!coe'):
        await message.channel.send('Coé')

    if message.content.startswith('!pessoa'):
        search = message.content[8:]
        print(search)

with open('keys/disc_api_key') as disc_key:
    for word in disc_key:
        key = word

client.run(key)
