import os

from pyrogram import Client

app = Client("dumper")

## Chat id from get-info.py where you want to dump
chat_id = -1001974716829


async def main():
    async with app:
        for file in os.listdir("dump"):

            def make_caption_title(file_name):
                # remove special characters without the dot and space
                file_name = "".join(
                    [char for char in file_name if char.isalnum() or char == "." or char == " "]
                )

                # remove double space
                file_name = file_name.replace("  ", " ")


                caption_title = " ".join(file_name.split(".")[0].split("_")) + "\n\n"
                caption_tags = caption_title.split(" ")
                for tag in caption_tags:
                    caption_title += "#" + tag + " "
                return caption_title

            file = "dump/" + file

            with open(file, "rb") as dump_file:
                caption_file_name = file.split("/")[-1]
                caption = make_caption_title(caption_file_name)
                try:
                    await app.send_photo(chat_id, dump_file, caption=caption)
                    await app.send_document(chat_id, dump_file, caption=caption, file_name=caption_file_name)
                except Exception as e:
                    print(e)
                    continue


app.run(main())
