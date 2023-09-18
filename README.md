# telegram-image-dump

In my case I had a meme template folder with 800+ templates and I wanted to create a channel with them so the telegram editor could do the meme editing on mobile. Besides stickers are quite fun to place over the images and speak volumes. (lol)

## My Meme Template channel
The channel is [MEMESFATHER](https://t.me/memesfather) inspired by bot father


## Usage
Install the requirements
```bash
pip install -r requirements.txt
```

Create a `.env` file with the following variables:
```bash
API_KEY=""
API_HASH=""
```
> These values can be obtained from [my.telegram.org](https://my.telegram.org/) after creating an app.


Run the get-info.py script to get the chat_id of the channel you want to dump the images to.
```bash
python get-info.py
```
Once you have the chat_id go to the run.py file and change the chat_id variable to the one you got from the previous step.

## General Info
- Always use a virtual environment when installing python packages.
- the .session file could be used to automate your telegram id without login in the future say if it were to be used by someone not very nice
- so treat it with care
- If your account gets automated without your consent you can just revoke the session from devices from telegram and that will invalidate the session file