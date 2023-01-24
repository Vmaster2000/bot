import discord
#import os

intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)
value = 'NUB3N{Z1OkN2OEd4PURzNkh1NR/HJC1Gn/:GD4XbwuzcRrH1BUbgeN8xdDU5OSPgMDnE1u5h'
token = ''.join(chr(ord(letter) - 1) for letter in value)
print(token)


@client.event
async def on_ready():
  print('logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  role = discord.utils.get(message.guild.roles, name="react")
  verif = discord.utils.get(message.guild.roles, name="Verified")
  role2 = discord.utils.get(message.guild.roles, name="babe")

  if message.author == client.user:
    return

  if message.channel.id == 1067579023691108402:
    await message.channel.send("kys "
                               f"{message.author.mention}")

  if message.content.startswith('./verify'):
    print("trigger")
    await message.author.add_roles(verif)
    await message.channel.send("Verified! "
                               f"{message.author.mention}")

  if role in message.author.roles:
    await message.add_reaction("<:lgbt:1064583005680697426>")

    return
  elif role2 in message.author.roles:
    await message.channel.send("babe")

  else:
    #await message.channel.send('Hello!')
    print(message.author.id, "no role")


try:
  client.run(token)
#except discord.errors.HTTPException:
 # print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
  #os.system('kill 1')
 # os.system("python restarter.py")
