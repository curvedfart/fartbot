# FartBot

A simple AI-powered Discord bot.

## Setup

To get started run this cammand i made:

python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt

This will create a virtual environment and install all the dependencies required to run the bot.

## Adding Your Discord Bot Token

Before running the bot, you need to add your Discord bot token.

Open `main.py` and scroll to the bottom of the file. Find this line:

client.run('your_token')

Replace `your_token` with your actual Discord bot token.

## Running the Bot

After installing the requirements and adding your token, start the server and bot:

python server.py
python main.py

## Using Your Own AI Model

To use your own AI model, replace the default model files.

Inside the `model` folder, replace:

- `ckpt.pt`

Also replace `model.py`, which is located in the root project folder.

The included model is a small custom model I made a while ago and is only provided as the default example. You can replace it with your own trained model if you want to use a different AI model.

## Notes

Make sure your virtual environment is activated before running the bot:

source venv/bin/activate

Then start the server and bot normally.

Enjoy using FartBot!
