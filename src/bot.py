import os
import discord
from discord.ext import commands
from tz_manager import *
from sc_manager import *
from dotenv import load_dotenv
import pyjokes
from random import randint
from random import choice
load_dotenv()
TIMEZONE = "EST5EDT"
BOT_TOKEN = os.getenv("BOT_TOKEN")



bot = commands.Bot(command_prefix=">", description="This is a Helper Bot")


@bot.command()
async def joke(ctx,add=None,task=None):
    joke_op = pyjokes.get_joke(language="en",category="neutral")
    await ctx.send(joke_op)

@bot.command()
async def sc(ctx,event=None,counter = 3):
    total = counter
    curr_time = datetime.now().astimezone(pytz.timezone(TIMEZONE))
    schedule_list = return_schedule_for_stored()
    result = ''
    def result_formatter(days_left,h,m,counter):
        colors = ['diff','css','fix',"bash"]
        if counter<4:
            color_chosen = colors[counter]
        else:
            color_chosen = colors[-1]
        time_left_formatted = (f"{days_left:02d} days {h:d} hours and {m:02d} minutes left")
        inside_text = schedule["name"].upper()+ " ::: "+ time_left_formatted
        if color_chosen=='diff':
            result_text = "-"+inside_text
        elif color_chosen=="css":
            result_text= '['+inside_text+"]"
        elif color_chosen =="fix":
            result_text=inside_text
        else:
            result_text='''"'''+inside_text+'''"'''
        
        padded_text = "```"+color_chosen+"\n"+result_text+"\n"+'```'+"\n"
        return padded_text

    for schedule in schedule_list:
        # print(schedule)
        if counter==0:
            break
        
        if((event=="event") and (schedule["event"]==True))or (((event=="main")or (event==None)) and (schedule["event"]==False)) or event=="all":
            
            if(schedule["datetime"]>curr_time):
                time_left = schedule["datetime"]-curr_time 
                seconds_left = time_left.seconds
                days_left = time_left.days
                m, s = divmod(seconds_left, 60)
                h, m = divmod(m, 60)
                
                result += result_formatter(days_left,h,m,total-counter)
                counter-=1
     
        
        # if event=="event":
    await ctx.send(result)




@bot.command()
async def tz(ctx, ins=None, *tmzs):

    if ins == None:
        result = ""
        timezs = return_tzs_for_stored()
        for tzs, times in timezs.items():
            
            tzs += "-" * (20 - len(tzs))
            result += "```"+tzs + times + "```"+"\n"

        await ctx.send(result)
        
    # Here in case you want to add tz yourself
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
async def hotel(ctx):
    await ctx.send("trivago")


# Events
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you suffer :)"))
    print("Im ready")


@bot.command()
async def pll(ctx):
    user = ctx.message.author
    if user.name == "Aaryan22":
        pitre = await bot.fetch_user(759433280235241512)
        joke = pyjokes.get_joke()
        await pitre.send(joke)
    

@bot.listen()
async def on_message(message):
    starter = ["jee bhai sunni","yo brother","eaa bituwa",'wadddacum bhaisahab','oi pitre sunna','Mr.Pitur, Id appreciate your attention',"kem cho ?","katti type gar6as rey","ya sunn"]
    if message.author.name == "Prashh":
        if randint(0,200)==69:
            user = message.author
            chosen_starter = choice(starter)
            result = chosen_starter+'\n'+"```"+pyjokes.get_joke(language="en",category="neutral")+"```"
            await user.send(result)
    

bot.run(BOT_TOKEN)
