# import telebot
from pytube import YouTube
from telebot.async_telebot import AsyncTeleBot
from pytube import YouTube

API_TOKEN = ''

bot = AsyncTeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    await bot.reply_to(message, 'привет. Я могу скачать видео с YouTube - Просто пришли мне ссылку')


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    if 'youtu' in message.text:
        yt = YouTube(message.text).streams.filter(res='360p').first().download(filename=f'name.mp4')
        file = open('name.mp4','rb')
        await bot.send_video(message.from_user.id, file)


import asyncio
asyncio.run(bot.polling())