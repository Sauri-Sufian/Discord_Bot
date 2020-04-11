import pyjokes
import discord
import time
import requests

token='tokenhere'
class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        name = []
        name = str(message.author) #initializing
        command = str(message.content)
        name = name[:(name.find('#'))]


        print(message.author, ':', message.content)
        message.content = message.content.lower()


        if message.author == client.user:
            return
        if message.content.startswith('<@!696193896073396285>') or message.content.startswith('hello'):
            await message.channel.send(f'Hellooo!! <@!{message.author.id}>') #greetings

        elif '-' in command: #gets command
            reply = command[command.find('-') + 1:]
            if('joke' in command):
                joke =pyjokes.get_joke()
                await message.channel.send(f'{joke} [<@!{message.author.id}>]') #sends joke
            elif 'time' in command:
                cTime = time.localtime()
                await  message.channel.send(f"{cTime[3] % 12}:{cTime[4]}")#tells time

            else:
                await message.channel.send(f'{reply}')





client = MyClient()
client.run(token)
#client.on_message('hi')




'''
    
'''


