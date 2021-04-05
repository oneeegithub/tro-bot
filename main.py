import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import os
from keep_alive import keep_alive
import time
import sys
import os,sys
import subprocess
import glob
from os import path
from datetime import datetime

client = discord

client = discord.Client()

now = datetime.now()

PREFIX = ("tro")

bot = commands.Bot(command_prefix='tro ')

bot = commands.Bot(command_prefix=PREFIX, description='Hi')





@client.event
async def on_ready():
	await client.change_presence(activity=discord.Streaming(
	    name='tro help', url='https://www.twitch.tv/therealone_tv'))
	print("TheRealOne Bot ist online!")



@client.event
async def on_message(message):
	if message.author == client.user:
		return



	if message.content.startswith('tro 100')and str(message.channel) == "100-test":
		await message.channel.send(':100:')
		with open("log_cmd.txt", "a") as f:
			pass
			current_time = now.strftime("%H:%M:%S")
			f.write("tro 100: " + str(message.author) + "  " + "\n") 


	if message.content.startswith('tro ip'):
		await message.channel.send('Die IP vom Minecraft Server: ||coming soon||')
		with open("log_cmd.txt", "a") as f:
			pass
			current_time = now.strftime("%H:%M:%S")
			f.write("tro ip: " + str(message.author) + "  " + "\n")		



	if message.content.startswith('tro twitch'):
		embedVar = discord.Embed(
		    title="Twitch",
		    description="Hier kannst du uns auf Twitch finden:",
		    color=discord.Colour.dark_purple())
		embedVar.add_field(name="Link:",
		                   value="https://therealone.me/twitch",
		                   inline=False)
		await message.channel.send(embed=embedVar)
		with open("log_cmd.txt", "a") as f:
			pass
			current_time = now.strftime("%H:%M:%S")
			f.write("tro twitch: " + str(message.author) + "  " + "\n")

	if message.content.startswith('tro youtube'):
		embedVar = discord.Embed(
		    title="YouTube",
		    description="Hier kannst du uns auf YouTube finden:",
		    color=discord.Colour.dark_red())
		embedVar.add_field(name="Link:",
		                   value="https://therealone.me/yt",
		                   inline=False)
		await message.channel.send(embed=embedVar)
		with open("log_cmd.txt", "a") as f:
			pass
			current_time = now.strftime("%H:%M:%S")
			f.write("tro youtube: " + str(message.author) + "  " + "\n")

	if message.content.startswith('tro links'):
		embedVar = discord.Embed(
		    title="Links",
		    description="Hier findest du alle unsere Links:",
		    color=discord.Colour.blue())
		embedVar.add_field(name="Link:",
		                   value="https://therealone.me",
		                   inline=False)
		await message.channel.send(embed=embedVar)
		with open("log_cmd.txt", "a") as f:
			pass
			current_time = now.strftime("%H:%M:%S")
			f.write("tro links: " + str(message.author) + "  " + "\n")


	if str(message.content) == ('tro help'):
		await message.channel.send('Hilfe kommt per DM')
		await message.author.send('Hilfe TheRealOne Bot:\nWenn du Probleme hast melde dich bei @one#3440\nHier sind ein paar Grundinfos:\nPrefix: tro\nDeveloper: one#3440\nInfos, Source, Issues usw: ||https://github.com/oneeegithub/tro-bot/issues||\nHier noch eine Liste der Commands: ||https://therealone.me/bot||')
		await message.add_reaction('🚀')
		with open("log_help.txt", "a") as f:
			pass
			f.write("Der Benutzer " + str(message.author) + " hat Hilfe gebraucht\n")


	if message.content.startswith('tro video'):
		await message.channel.send(' Hier findest du unser neuestes Video: https://therealone.me/neuesvideo')

	if message.content.startswith('tro devmode'):
		await message.channel.send('DevMode: ON\nWenn der DevMode an ist musst du dich nicht über Bugs wundern')







	if message.content.startswith('') and str(message.channel) == "autoclear" :
		await message.channel.purge(limit=100)
		with open("log_autoclear.txt", "a") as f:
			pass
			current_time = now.strftime("%H:%M:%S")
			f.write("TRO AUTOCLEARER: Die Nachricht[" + (message.content) + "] von: " + str(message.author) + " wurde entfernt " + (current_time) + "\n")


	if str(message.content) == ('tro clear') and message.author.permissions_in(message.channel).manage_messages:
		await message.channel.send('Alle Nachrichten werden innerhalb 2 Sekunden gelöscht')
		time.sleep(2)
		await message.channel.purge(limit=1000000)
		with open("log_clear.txt", "a") as f:
			pass
			current_time = now.strftime("%H:%M:%S")
			f.write("tro clear: " + str(message.author) + "  " + "\n")


	if str(message.content) == ('tro clear 1') and message.author.permissions_in(message.channel).manage_messages:
		await message.channel.send('1 Nachricht wird gelöscht')
		time.sleep(1)
		await message.channel.purge(limit=3)


	if str(message.content) == ('tro clear 5') and message.author.permissions_in(message.channel).manage_messages:
		await message.channel.send('5 Nachrichten werden gelöscht')
		time.sleep(1)
		await message.channel.purge(limit=7)


	if str(message.content) == ('tro clear 10') and message.author.permissions_in(message.channel).manage_messages:
		await message.channel.send('10 Nachrichten werden gelöscht')
		time.sleep(1)
		await message.channel.purge(limit=12)


	if str(message.content) == ('tro clear 50') and message.author.permissions_in(message.channel).manage_messages:
		await message.channel.send('50 Nachrichten werden gelöscht')
		time.sleep(1)
		await message.channel.purge(limit=52)


	if str(message.content) == ('tro clear 100') and message.author.permissions_in(message.channel).manage_messages:
		await message.channel.send('100 Nachrichten werden gelöscht')
		time.sleep(1)
		await message.channel.purge(limit=102)


	if str(message.content) == ('tro clear 200') and message.author.permissions_in(message.channel).manage_messages:
		await message.channel.send('200 Nachrichten werden gelöscht')
		time.sleep(1)
		await message.channel.purge(limit=202)


	if str(message.content) == ('tro clear 1000') and message.author.permissions_in(message.channel).manage_messages:
		await message.channel.send('1000 Nachrichten werden gelöscht')
		time.sleep(1)
		await message.channel.purge(limit=1002)

	if message.content.startswith('hamster'):
		await message.channel.send('🐹')


	
    








keep_alive()
client.run(os.getenv('TOKEN'))
