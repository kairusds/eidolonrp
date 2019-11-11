from discord.ext import commands
from os import getenv
import discord
import time
import uuid

print("start")
bot = commands.Bot(command_prefix="℅", self_bot=True)

@bot.event
async def on_ready():
	print("Connected!")
	print(f"Logged in with account {bot.user}.")
	print("Github: https://github.com/kairusds/eidolonrp")

	ms = time.time() * 1000
	timestamp = dict(start=ms)
	assets = dict(
		large_image=getenv("largeimage"),
		large_text=getenv("largetext"),
		small_image=getenv("smallimage"),
		small_text=getenv("smalltext")
	)
	partysize = int(getenv("partysize"))
	partymax = int(getenv("partymax"))
	party = dict(id=str(uuid.uuid4()), size=[partysize, partymax])
	activity = discord.Activity(
		application_id=getenv("appid"),
		name=getenv("name"),
		state=getenv("state"),
		details=getenv("details"),
		assets=assets,
		party=party,
		timestamps=timestamp,
		type=int(getenv("type"))
	)
	await bot.change_presence(activity=activity, status=discord.Status.online)
	print("Changed rich presence.")

bot.run(getenv("token"), bot=False)