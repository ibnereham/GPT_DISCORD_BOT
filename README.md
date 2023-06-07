# INFO
This is a Discord Bot code. It utilizes OpenAI's GPT-3.5 Turbo model.
## Note:
I am new to programming. This is a simple code which should be mostly understandable by beginners.
# FEATURES
## /gpt3

Main command for the normal GPT model.
## /gpx3
GPT with the custom "Mongo Tom" prompt as system prompt

## /img3 
Uses DALL-E to generate an Image. The image is currently set to 256x256. You can change that by changing the "SIZE" in "im_response" in the OPENAI.PY file. You can also change the number of images by changing the "n" value in the same place. 

# HOW_TO_USE

## Get The Required keys
1. Get the OpenAI API key from their website
2. Get the Discord Token for your bot
## Setting_Up_The Keys
### In the .env,
#### DISCORD_API
replace the "YOUR DISCORD BOT TOKEN" With your token.
#### OpenAI_API
Replace the "YOUR OPENAI API KEY" With your API key.
## INSTALLING REQUIREMENTS.
 GOTO YOUR PROJECT DIRECTORY IN TERMINAL, THEN RUN THE FOLLOWING COMMMAND:
 ```bash
 pip install -r requirements.txt
```
# RUNNING_THE_CODE
## RUN THE FOLLOWING COMMAND
 ```bash
 python3 run.py
 ```
