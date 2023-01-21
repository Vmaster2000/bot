import discord

intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)



@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))

 
@client.event
async def on_message(message):
    role = discord.utils.get(message.guild.roles, name="react")
    role2 = discord.utils.get(message.guild.roles, name="babe")
    if message.author == client.user:
        return
    if role in message.author.roles:
        await message.add_reaction("<:lgbt:1064583005680697426>")
        return
    elif role2 in message.author.roles:
        await message.channel.send("babe")
    else:
        #await message.channel.send('Hello!')
        print(message.author.id, "no role" )
        
client.run('MTA2MzY0NjM1NDc3OTQyMjg0MQ.GPoXWU.vEAwcR3TLun8N0p6c1CXSfjav-3InbsQiBhr8Q')


