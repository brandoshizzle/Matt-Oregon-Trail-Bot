# bot.py
import os
import random
import discord
from discord.ext import tasks
from dotenv import load_dotenv
import pickle
import asyncio
from pynput.keyboard import Key, Controller

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
client = discord.Client()

keyboard = Controller()

user_data = {}
game_started = False
input_time = 5
cooldown_time = 10
input_array = []
hunt = False

# Load data (deserialize)
if os.path.exists("data.pickle"):
    with open("data.pickle", "rb") as handle:
        user_data = pickle.load(handle)


@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    content = message.content.lower()

	# Start all commands with Matt or matt
    if content.startswith("matt"):
        content = content[4:].strip()
    	username = message.author.name
	
	if content.startswith("start") or content.startswith("begin"):
		await message.channel.send(
			"Hey there travellers!"
		) 
		await message.channel.send(
			"A new game of Oregon Trail starts in 10 seconds. Make sure the host has the Oregon Trail window in focus."
		)
		await asyncio.sleep(10)
		await message.channel.send(
			"The game has begun. Good luck to all!"
		)
	if content.startswith("cooldown"):
		m_array = content.split()
		if isnumeric(m_array[1]):
			cooldown_time = int(m_array[1])
			await message.channel.send(
				"Cooldown time set to " + m_array[1] + "."
			)
		else:
			await message.channel.send(
				"Woah there, I don't understand. Set cooldown time by typing 'matt cooldown 20'"
			)
	if content.startswith("input"):
		m_array = content.split()
		if isnumeric(m_array[1]):
			cooldown_time = int(m_array[1])
			await message.channel.send(
            			"Input time set to " + m_array[1] + "."
        		)
		else:
			await message.channel.send(
            			"Woah there, I don't understand. Set input time by typing 'matt input 20'"
        		)
		


async def process_input():
	await client.wait_until_ready()
	if game_started:
		await message.channel.send(
        		"What do you want to do travellers?"
        	)
		chosen_input = ""
		await asyncio.sleep(input_time)

		# DO STUFF WITH INPUTS

		await message.channel.send(
			"Alright, you chose **" + chosen_input + "**"
		)
		await asyncio.sleep(cooldown_time)
	else:
		await asyncio.sleep(5)

	
def update_user_data(user, key, value):
    if user not in user_data:
        user_data[user] = {}
    user_data[user][key] = value
    store_user_data()


def store_user_data():
    # Store data (serialize)
    with open("data.pickle", "wb") as handle:
        pickle.dump(user_data, handle, protocol=pickle.HIGHEST_PROTOCOL)

client.loop.create_task(process_input())
client.run(TOKEN)
