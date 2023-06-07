import discord
from discord import Webhook
from discord.ext import commands
from discord import Intents,app_commands
from googletrans import Translator
import asyncio
from dotenv import load_dotenv
import os
from app.ai.openai import chatgpt_response, chatgpx_response, gf_response, dan_response, im_response

intents = discord.Intents.default()
intents.message_content = True
intents.all()

activity=discord.Activity(type=discord.ActivityType.playing, name="/help")
status = discord.Status.idle

translator1 = Translator(service_urls=[
      'translate.google.com'
    ])
translator2 = Translator(service_urls=[
      'translate.google.com'
    ])

load_dotenv()
discord_token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix="/ ",intents=intents,status=status,activity=activity)
bot.remove_command("help")

helpcmd =  "\n I. /gpt - for main gpt. \n II. /gpx - for a cultured response. \n III. /gf - for using gpt as your GF. \n IV. /helpgpt - TO SHOW THIS. \n\n\n APPLICATION CMDs \n\n1./gpt3 for main gpt \n2./gpx3 - for cultured response.\n3./gf3 - for GF response.\n /help - SHOW THIS "

@bot.event
async def on_ready():
    print("bot is on")
    try:
        synced = await bot.tree.sync()
        print(f"SYNCED{len(synced)} command(s) ")
    except Exception as e:
        print(e)

@bot.tree.command(name="help")
async def test1(interaction: discord.Interaction):
    await interaction.response.send_message(f"hello {interaction.user.mention} \n {helpcmd}", ephemeral=True)

@bot.tree.command(name="gpt3", description="gives ans to almost any question")
@app_commands.describe(prompt = "Prompt")
async def gpt3(interaction: discord.Interaction, prompt:str):      
    try:
        await interaction.response.defer()
        bot_response = chatgpt_response(prompt=prompt, chat_history=None)
        await interaction.followup.send(f"{interaction.user.mention}, {bot_response}")
    except Exception as e:
        await interaction.followup.send(
            f"{interaction.user.mention}, The model is currently full of requests"
        )

@bot.tree.command(name="gpx3",description="Gives a cultured response.")
@app_commands.describe(prompt = "Prompt")
async def gpx3(interaction: discord.Interaction, prompt:str):
    try:
        await interaction.response.defer()
        botx_response = chatgpx_response(prompt=prompt, chat_history=None)
        await interaction.followup.send(f"{interaction.user.mention}, {botx_response}")
    except Exception as e:
        await interaction.followup.send(
            f"{interaction.user.mention}, There was an error processing your request. Please try again later."
        )

@bot.tree.command(name="gf3",description="acts as a girlfriend")
@app_commands.describe(prompt = "Prompt")
async def gf3(interaction: discord.Interaction, prompt:str):
    try:
        await interaction.response.defer()
        girl_response = gf_response(prompt=prompt, chat_history=None)
        await interaction.followup.send(f"{interaction.user.mention}, {girl_response}")
    except Exception as e:
        await interaction.followup.send(
            f"{interaction.user.mention}, There was an error processing your request. Please try again later."
        )   
        
@bot.tree.command(name="dan3",description="acts as a DAN")
@app_commands.describe(prompt = "Prompt")
async def gf3(interaction: discord.Interaction, prompt:str):
    try:
        await interaction.response.defer()
        danx_response = dan_response(prompt=prompt)
        await interaction.followup.send(f"{interaction.user.mention}, {danx_response}")
    except Exception as e:
        await interaction.followup.send(
            f"{interaction.user.mention}, There was an error processing your request. Please try again later."
        )   

@bot.tree.command(name="img3",description="IMAGE")
@app_commands.describe(prompt = "Prompt")
async def img3(interaction: discord.Interaction, prompt:str):
    try:
        await interaction.response.defer()
        img_response = im_response(prompt=prompt,)
        await interaction.followup.send(f"{interaction.user.mention},Your Image Link: --> {img_response}")
    except Exception as e:
        await interaction.followup.send(
            f"{interaction.user.mention}, There was an error processing your request. Please try again later."
        )        
        print(e)
 
    

@bot.tree.command(name="bang3", description="gives ans to almost any question in Bangla")
@app_commands.describe(prompt = "Prompt")
async def gpt3(interaction: discord.Interaction, prompt: str):
    try:
        await interaction.response.defer()

        # Detect the language of the prompt
        detected_lang = translator1.detect(prompt).lang

        # Check if the detected language is English
        if detected_lang != 'en':
            # Translate the prompt from Bangla to English
            translated_prompt = translator1.translate(prompt, dest="en")

            # Get the bot response in English
            bot_response = chatgpt_response(prompt=str(translated_prompt), chat_history=None)

            # Translate the bot response from English to Bangla
            translated_response = translator1.translate(bot_response, src="en", dest="bn")
            translated_response_text = translated_response.text

            await interaction.followup.send(f"{interaction.user.mention}, {str(translated_response_text)}")
        else:
            # Prompt is already in English, return without further processing
            await interaction.followup.send(f"{interaction.user.mention}, Please provide a prompt in a language other than English.")

    except Exception as e:
        print(e)
        await interaction.followup.send(
            f"{interaction.user.mention}, There was an error processing your request. Please try again later.{e}"
        )
        

bot.run(discord_token)
