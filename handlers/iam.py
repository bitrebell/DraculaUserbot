from telethon import  events
photo1 = "https://graph.org/file/2859343230b36f959f24e.jpg"

@events.register(events.NewMessage(outgoing=True , pattern=r'\.iam'))
async def iamHandler(event):
    client = event.client
    me = await client.get_me()
    await client.edit_message(event.message , "[.](photo1)Hey My name is Aadil Shiekh \nBut sometime my friends call Me {}.\n\n**Want to know More About me?**\nGo [Here](https://devil-shiva.github.io/lucifer.github.io/)".format(me.username) , link_preview=False )
