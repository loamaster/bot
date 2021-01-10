import discord
import requests
import os


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('p!add '):
            data = message.content[6:]
            try:
                ans = int(data.split(" ")[0]) + int(data.split(" ")[1])
                await message.channel.send(ans)
            except:
                await message.channel.send("Please enter an integer")

        if message.content.startswith('p!yesno'):
            data = requests.get('https://yesno.wtf/api').json()
            await message.channel.send(data['image'])

        if message.content.startswith('p!xkcd'):
            data = requests.get('https://c.xkcd.com/random/comic/')
            data = requests.get("https://xkcd.com/" + data.url[17:-1] +
                                "/info.0.json").json()
            await message.channel.send(data['img'])


client = MyClient()
client.run(os.environ['DISCORD_TOKEN'])
