import discord
from discord.ext import commands
import random
import time

client = commands.Bot(command_prefix="!")


@client.event
async def on_ready():
    print("Bot is ready")


@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == 727210891048648808 or message_id == 727212808512471082:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)
        role = None

        if payload.emoji.name == "1️⃣":
            role = discord.utils.get(guild.roles, name="Deneyap Çalışma")

        elif payload.emoji.name == "2️⃣":
            role = discord.utils.get(guild.roles, name="Bilim Atölyeleri Çalışma")

        elif payload.emoji.name == "3️⃣":
            role = discord.utils.get(guild.roles, name="Uzaktan Öğretim Sistemi")

        elif payload.emoji.name == "4️⃣":
            role = discord.utils.get(guild.roles, name="Girişim Merkezi")

        elif payload.emoji.name == "5️⃣":
            role = discord.utils.get(guild.roles, name="Akran Eğitmeni")

        elif payload.emoji.name == "✅":
            role = discord.utils.get(guild.roles, name="Gönüllü")

        elif payload.emoji.name == "❌":
            role = discord.utils.get(guild.roles, name="Gönüllü")

        member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
        if member is not None and len(member.roles) < 9:
            await member.add_roles(role)
        else:
            print("")
            print("Role not found")


@client.event
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    if message_id == 727210891048648808 or message_id == 727212808512471082:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)
        role = None

        if payload.emoji.name == "1️⃣":
            role = discord.utils.get(guild.roles, name="Deneyap Çalışma")

        elif payload.emoji.name == "2️⃣":
            role = discord.utils.get(guild.roles, name="Bilim Atölyeleri Çalışma")

        elif payload.emoji.name == "3️⃣":
            role = discord.utils.get(guild.roles, name="Uzaktan Öğretim Sistemi")

        elif payload.emoji.name == "4️⃣":
            role = discord.utils.get(guild.roles, name="Girişim Merkezi")

        elif payload.emoji.name == "5️⃣":
            role = discord.utils.get(guild.roles, name="Akran Eğitmeni")

        elif payload.emoji.name == "✅":
            role = discord.utils.get(guild.roles, name="Gönüllü")

        elif payload.emoji.name == "❌":
            role = discord.utils.get(guild.roles, name="Gönüllü")

        member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
        await member.remove_roles(role)
    else:
        print("Role not found")


@client.command(aliases=["anladım"])
async def ready(ctx):
    role_list = []
    for role in ctx.author.roles:
        role_list.append(role.name)

    if "Gönüllü" in role_list and "Alanında Uzman Gönüllü" in role_list:
        await ctx.author.send("-----------------------------")
        await ctx.author.send("Çalışıyor musun? sorusuna sadece 1 yanıt vermelisin!")
        await ctx.author.send("Lütfen kurallara uyup tekrar dene!")
        await ctx.author.send("-----------------------------")
        time.sleep(2)
        await ctx.channel.purge(limit=1)

    elif "Gönüllü" not in role_list and "Alanında Uzman Gönüllü" not in role_list:
        await ctx.author.send("-----------------------------")
        await ctx.author.send("Çalışıyor musun? sorusuna yanıt vermelisin!")
        await ctx.author.send("Lütfen kurallara uyup tekrar dene!")
        await ctx.author.send("-----------------------------")
        time.sleep(2)
        await ctx.channel.purge(limit=1)

    elif len(role_list) == 4:
        await ctx.author.send("-----------------------------")
        await ctx.author.send("Discord sunucumuza başarıyla kaydoldun!")
        await ctx.author.send("Hoşgeldin! Diğer gönüllülerle mesajlaşmadan önce kuralları okumayı unutma!")
        await ctx.author.send("-----------------------------")
        id2 = client.get_guild() # Güvenlik sebebi ile token kaldırılmıştır.
        role = discord.utils.get(id2.roles, name="Kayıt  Ol")
        await ctx.author.remove_roles(role)
        time.sleep(2)
        await ctx.channel.purge(limit=1)

    elif len(role_list) == 2:
        await ctx.author.send("-----------------------------")
        await ctx.author.send("Lütfen her iki soruya da cevap ver!")
        await ctx.author.send("-----------------------------")
        time.sleep(2)
        await ctx.channel.purge(limit=1)

    elif len(role_list) > 4:
        await ctx.author.send("-----------------------------")
        await ctx.author.send("Lütfen her iki soruya da birer kez cevap ver!")
        await ctx.author.send("Tekrar dene!")
        await ctx.author.send("-----------------------------")
        time.sleep(2)
        await ctx.channel.purge(limit=1)

#
# @client.command()
# async def clear(ctx, number=5):
#     await ctx.channel.purge(limit=number)

#
# @client.event
# async def on_message(message):
#     id = client.get_guild()
#     channels = ["bot-deneme"]
#
#     if str(message.channel) in channels and message.content != "!anladım":
#         time.sleep(2)
#         await message.channel.purge(limit=1)

client.run("") #Güvenlik sebebi ile buradaki adres kaldırılmıştır.