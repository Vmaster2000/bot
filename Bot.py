import discord

intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)
value = 'NUB3N{Z1OkN2OEd4PURzNkh1NR/HQpYXV/wFBxdS4UMvo9O1q7d2DYTgkbw.4JoctRjCis9R'
token = ''.join(chr(ord(letter)-1) for letter in value)
print(token)


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
        
client.run(token)

