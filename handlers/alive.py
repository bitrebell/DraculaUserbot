import os
from telethon import client, events



@events.register(events.NewMessage(outgoing=True , pattern=r'\.jinda'))
async def alivehandler(event):
    client = event.client
    me = await client.get_me()
    username =  me.username
    phtou = await client.download_profile_photo(username)
    await client.edit_message(event.message  ,
        "CONFIGURATION......"
    )
    await event.respond(
        "My Master @{}\nWant to make Your Own Bot??\n\n"
        "Bot Created by [bitrebell](t.me/bitrebell)"
        "\nBetter Watch My Bot or Jealous {}"
        
        .format(username , '@bitrebell_bot')
        ,file = phtou
        )
    await event.message.delete()
    os.remove(phtou)
    