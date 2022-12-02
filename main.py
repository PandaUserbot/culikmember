import os
import asyncio

from pyrogram import filters, enums
from pyrogram.errors import ChatAdminRequired, RPCError, FloodWait

from pyrogram import Client, errors

app = Client(
    session_string=os.getenv("SESSION"),
    api_id=int(os.getenv("API_ID")), 
    api_hash=os.getenv("API_HASH"),
    name="main.py",
    in_memory=True
)
PREFIX = "."

def get_arg(message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])


bangke = [-1001277950257]

@app.on_message(filters.command("inviteall", PREFIX) & filters.me & ~filters.private)
async def inviteall(client, message):
    kentot = await message.edit_text(f"Berikan saya username group.\ncontoh: {PREFIX}inviteall @testing")
    text = message.text.split(" ", 1)
    queryy = text[1]
    chat = await app.get_chat(queryy)
    tgchat = message.chat
    kontol = 0
    gagal = 0
    await kentot.edit_text(f"Menambahkan members dari {chat.username}")
    if chat.id in bangke:
        await app.send_message(-1001277950257, "**Maaf telah mencuri members sini**")
        return
    async for member in app.get_chat_members(chat.id):
        user = member.user
        zxb = [enums.UserStatus.ONLINE, enums.UserStatus.OFFLINE, enums.UserStatus.RECENTLY, enums.UserStatus.LAST_WEEK]
        if user.status in zxb:
            try:
                await app.add_chat_members(tgchat.id, user.id, forward_limit=60)
                kontol = kontol + 1
                await asyncio.sleep(2)
            except FloodWait as e:
                mg = await app.send_message(LOG_CHAT, f"error-   {e}")
                gagal = gagal + 1
                await asyncio.sleep(0.3)
                await mg.delete()
                
    return await app.send_message(tgchat.id, f"**Invite All Members** \n\n**Berhasil:** `{kontol}`\n**Gagal:** `{gagal}`"
    )

from pyrogram import idle
app.start()
print(
    f"Aktif."
)
idle()

