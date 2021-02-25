from discord.ext import commands
import discord
import time
import uuid
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

print("boot")

bot = commands.Bot(command_prefix="℅", self_bot=True)

@bot.event
async def on_ready():
	print("Connected!")
	print(f"Logged in with account {bot.user}.")
	print("Github: https://github.com/kairusds/eidolonrp")
	
	ms = time.time() * 1000
	timestamp = dict(start=ms)
	assets = dict(
		large_image=config["assets"]["largeimage"],
		large_text=config["assets"]["largetext"],
		small_image=config["assets"]["smallimage"],
		small_text=config["assets"]["smalltext"]
	)
	
	activity_args = dict(
		application_id=config.getint("activity", "appid"),
		name=config["activity"]["name"],
		state=config["activity"]["state"],
		details=config["activity"]["details"],
		assets=assets,
		timestamps=timestamp,
		type=config.getint("activity", "type")
	)
	
	if config.getint("activity", "type") == 1:
		activity_args["url"] = config["activity"]["url"]
	
	if config.getboolean("party", "enabled"):
		partysize = config.getint("party", "size")
		partymax = config.getint("party", "maxsize")
		activity_args["party"] = dict(id=str(uuid.uuid4()), size=[partysize, partymax])
	
	activity = discord.Activity(**activity_args)
	await bot.change_presence(activity=activity, status=config["activity"]["status"])
	print("Changed rich presence.")

bot.run(config["user"]["token"], bot=False)