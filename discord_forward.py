
import os
import yaml
import sys
import logging
import discord


''' 
------------------------------------------------------------------------
    DISCORD CLIENT - Init the client
------------------------------------------------------------------------
'''
intents = discord.Intents.default()
intents.typing = False

discord_client = discord.Client(intents=intents)
with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)

''' 
------------------------------------------------------------------------
    MESSAGE, PHOTO_ID, VIDEO_ID AS WE RECIEVE FROM FORWARDGRAM SCRIPT
------------------------------------------------------------------------
'''
message = sys.argv[1]
photo_id = sys.argv[-2]
video_id = sys.argv[-1]

# Remove channel names from message
# words = ["@Channel_names", "@Channel_names"]
# for word in words:
#     if word in message:
#         message = message.replace(word, "")

''' 
------------------------------------------------------------------------
    DISCORD SERVER START EVENT - We will kill this immaturely
------------------------------------------------------------------------
'''
# when discord is initalized, it will trigger this event. 
# we quickly send messages to our discord channels and quit the script prematurely.
# this gets trigged again when a new message is sent on channel from telegram

@discord_client.event
async def on_ready():

    print('We have logged in as {0.user}'.format(discord_client))
    print('Awaiting Telegram Message')

    # My channels are for RTX card drops and PS5
    channel_1 = discord_client.get_channel(config["discord_1_channel"])

    # Uncomment below if you use more than one channel's id in config.yaml
    # channel_2 = discord_client.get_channel(config["discord_2_channel"])
    # channel_3 = discord_client.get_channel(config["discord_3_channel"])
    # channel_4 = discord_client.get_channel(config["discord_4_channel"])

    # print(f"Channel ID: {config['discord_1_channel']}")  # Debug
    # print(f"Resolved Channel: {channel_1}")  # Debug
    
    if message != "":
        if photo_id != 'None' and video_id != 'None':
            await channel_1.send(content=message, files=[discord.File(photo_id, 'photo.jpg'), discord.File(video_id, 'video.mp4')])
            os.remove(photo_id)
            os.remove(video_id)
        else:
            if photo_id != 'None':
                await channel_1.send(files=[discord.File(photo_id, 'photo.jpg')])
                os.remove(photo_id)
            elif video_id != 'None':
                await channel_1.send(files=[discord.File(video_id, 'video.mp4')])
                os.remove(video_id)
        await channel_1.send(content=message)
    else:
        if photo_id != 'None' and video_id != 'None':
            await channel_1.send(files=[discord.File(photo_id, 'photo.jpg'), discord.File(video_id, 'video.mp4')])
            os.remove(photo_id)
            os.remove(video_id)
        else:
            if photo_id != 'None':
                await channel_1.send(files=[discord.File(photo_id, 'photo.jpg')])
                os.remove(photo_id)
            elif video_id != 'None':
                await channel_1.send(files=[discord.File(video_id, 'video.mp4')])
                os.remove(video_id)

    await discord_client.close()

discord_client.run(config["discord_bot_token"])