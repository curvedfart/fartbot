# FartBot

A simple AI-powered Discord bot.

## Setup

To get started run one of the camands to make a venv and install the requierd packages, run the corect one for your distro:


linux:
python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt



windows:
venv\Scripts\activate
pip install -r requirements.txt



mac:
python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt



## Adding Your Discord Bot Token

Before running the bot, you need to add your Discord bot token.

Open `main.py` and go to the bottom of the file. Find this line:

client.run('your_token')

Replace `your_token` with your actual Discord bot token.

## Running the Bot

After installing the requirements and adding your token, start the server and bot:

python server.py
python main.py

## Using Your Own AI Model

To use your own AI model, replace the default model.py file.

also make a folder caled model and put your .pt in there

## Notes

Make sure your virtual environment is activated before running the bot:

source venv/bin/activate

Then start the server and bot normally.

Enjoy using FartBot!
