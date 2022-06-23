import os
import discord
from discord.ext import commands
from tz_manager import *
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

print(BOT_TOKEN)

bot = commands.Bot(command_prefix=">", description="This is a Helper Bot")


@bot.command()
async def tz(ctx, ins=None, *tmzs):

    # try to add to timezone
    if ins == None:
        result = ""
        timezs = return_tzs_for_stored()
        for tzs, times in timezs.items():
            tzs += "-" * (20 - len(tzs))
            result += tzs + "--------" + times + "\n"

        await ctx.send(result)
    elif ins.lower() =="a":
        await ctx.send("is not a timezone")
    # elif ins.lower() == "a":
    #     for tmz in tmzs:
    #         if is_timezone(tmz):
    #             with open("timezone_list.txt", "a") as f:
    #                 f.write(str(tmz) + "\n")

    #         else:
    #             await ctx.send(tmz + "is not a timezone")

    # elif ins.lower() == "n":
    #     for tmz in tmzs:
    #         if is_timezone(tmz):
    #             with open("timezone_list.txt", "w") as f:
    #                 f.write(str(tmz) + "\n")

    #         else:
    #             await ctx.send(tmz + "is not a timezone")


@bot.command()
async def ping(ctx):
    await ctx.send("pong")


# Events
@bot.event
async def on_ready():
    await bot.change_presence(
        activity=discord.Streaming(
            name="Tutorials", url="http://www.twitch.tv/accountname"
        )
    )
    print("Im ready")


@bot.listen()
async def on_message(message):
    if "tutorial" in message.content.lower():
        # in this case don't respond with the word "Tutorial" or you will call the on_message event recursively
        await message.channel.send("This is that you want http://youtube.com/fazttech")
        await bot.process_commands(message)


bot.run(BOT_TOKEN)
