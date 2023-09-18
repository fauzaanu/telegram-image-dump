from pyrogram import Client
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access environment variables
api_id= os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
# print(api_id)
app = Client("dumper", api_id=api_id, api_hash=api_hash)

async def main():
    async with app:
        async for dialog in app.get_dialogs():
            print(dialog.chat.title or dialog.chat.first_name)
            print(dialog.chat.id)
            # -1001974716829
app.run(main())
