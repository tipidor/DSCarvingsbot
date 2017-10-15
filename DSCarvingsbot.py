# This example show how to write an inline mode telegramt bot use pyTelegramBotAPI.

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Simple Bot to reply to Telegram messages
# This program is dedicated to the public domain under the CC0 license.
"""
This Bot uses the Updater class to handle the bot.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic inline bot example. Applies different text transformations.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""
from uuid import uuid4

import re

from telegram import InlineQueryResultArticle, ParseMode, \
    InputTextMessageContent, InlineQueryResultVoice
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    update.message.reply_text('Hi!')


def help(bot, update):
    update.message.reply_text('Help!')


def escape_markdown(text):
    """Helper function to escape telegram markup symbols"""
    escape_chars = '\*_`\['
    return re.sub(r'([%s])' % escape_chars, r'\\\1', text)


def inlinequery(bot, update):
    query = update.inline_query.query
    results = list()

    results.append(InlineQueryResultVoice(id=uuid4(),
    										voice_url='/carvings_files/Hello.opus', title='abcd'))

    results.append(InlineQueryResultArticle(id=uuid4(),
                                            title="Bold",
                                            input_message_content=InputTextMessageContent(
                                                "*%s*" % escape_markdown(query),
                                                parse_mode=ParseMode.MARKDOWN)))

    results.append(InlineQueryResultArticle(id=uuid4(),
                                            title="Italic",
                                            input_message_content=InputTextMessageContent(
                                                "_%s_" % escape_markdown(query),
                                                parse_mode=ParseMode.MARKDOWN)))

    update.inline_query.answer(results)


def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"' % (update, error))


def main():
    # Create the Updater and pass it your bot's token.
    TOKEN = "415385670:AAHc8pwuCSmZDwVIY4Vm75w7jnrCJgiT_m8"
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(InlineQueryHandler(inlinequery))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Block until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
	main()

# import telebot
# import time
# import sys
# import logging
# from telebot import types

# TOKEN = "415385670:AAHc8pwuCSmZDwVIY4Vm75w7jnrCJgiT_m8"

# bot = telebot.TeleBot(TOKEN)
# telebot.logger.setLevel(logging.DEBUG)


# @bot.inline_handler(lambda query: query.query == 'text')
# def query_text(inline_query):
#     try:
#         r = types.InlineQueryResultArticle('1', 'Result1', types.InputTextMessageContent('hi'))
#         r2 = types.InlineQueryResultArticle('2', 'Result2', types.InputTextMessageContent('hi'))
#         bot.answer_inline_query(inline_query.id, [r, r2])
#     except Exception as e:
#         print(e)


# @bot.inline_handler(lambda query: query.query == 'photo1')
# def query_photo(inline_query):
#     try:
#         r = types.InlineQueryResultPhoto('1',
#                                          'https://raw.githubusercontent.com/eternnoir/pyTelegramBotAPI/master/examples/detailed_example/kitten.jpg',
#                                          'https://raw.githubusercontent.com/eternnoir/pyTelegramBotAPI/master/examples/detailed_example/kitten.jpg',
#                                          input_message_content=types.InputTextMessageContent('hi'))
#         r2 = types.InlineQueryResultPhoto('2',
#                                           'https://raw.githubusercontent.com/eternnoir/pyTelegramBotAPI/master/examples/detailed_example/rooster.jpg',
#                                           'https://raw.githubusercontent.com/eternnoir/pyTelegramBotAPI/master/examples/detailed_example/rooster.jpg')
#         bot.answer_inline_query(inline_query.id, [r, r2], cache_time=1)
#     except Exception as e:
#         print(e)


# @bot.inline_handler(lambda query: query.query == 'video')
# def query_video(inline_query):
#     try:
#         r = types.InlineQueryResultVideo('1',
#                                          'https://github.com/eternnoir/pyTelegramBotAPI/blob/master/tests/test_data/test_video.mp4?raw=true',
#                                          'video/mp4', 'Video',
#                                          'https://raw.githubusercontent.com/eternnoir/pyTelegramBotAPI/master/examples/detailed_example/rooster.jpg',
#                                          'Title'
#                                          )
#         bot.answer_inline_query(inline_query.id, [r])
#     except Exception as e:
#         print(e)


# @bot.inline_handler(lambda query: len(query.query) is 0)
# def default_query(inline_query):
#     try:
#         r = types.InlineQueryResultArticle('1', '1st choice', types.InputTextMessageContent('Hello'))

#         hell = types.InlineQueryResultPhoto('2', 'https://raw.githubusercontent.com/eternnoir/pyTelegramBotAPI/master/examples/detailed_example/kitten.jpg','https://raw.githubusercontent.com/eternnoir/pyTelegramBotAPI/master/examples/detailed_example/rooster.jpg')
#         #hello = types.InlineQueryResultVoice('3', 'opus.ogg','Written case',"1000",'10')

#         # vi = types.InlineQueryResultVideo('3',
#         #                                  'https://github.com/eternnoir/pyTelegramBotAPI/blob/master/tests/test_data/test_video.mp4?raw=true',
#         #                                  'video/mp4', 'Video',
#         #                                  'https://raw.githubusercontent.com/eternnoir/pyTelegramBotAPI/master/examples/detailed_example/rooster.jpg',
#         #                                  'Title'
#         #                                  )
#         # thankyou = types.InlineQueryResultAudio('3',
#         #                                  'carving_files/ThankYou.mp3',
#         #                                  'https://raw.githubusercontent.com/eternnoir/pyTelegramBotAPI/master/examples/detailed_example/kitten.jpg',
#         #                                  input_message_content=types.InputTextMessageContent('thankyou'))
#         # helpme = types.InlineQueryResultAudio('4',
#         #                                  'carving_files/HelpMe.mp3',
#         #                                  'https://raw.githubusercontent.com/eternnoir/pyTelegramBotAPI/master/examples/detailed_example/kitten.jpg',
#         #                                  input_message_content=types.InputTextMessageContent('HelpMe'))
#         # imsorry = types.InlineQueryResultAudio('5',
#         #                                  'carving_files/Hello.mp3',
#         #                                  'https://raw.githubusercontent.com/eternnoir/pyTelegramBotAPI/master/examples/detailed_example/kitten.jpg',
#         #                                  input_message_content=types.InputTextMessageContent('hello'))
#         # verygood = types.InlineQueryResultAudio('6',
#         #                                  'carving_files/Hello.mp3',
#         #                                  'https://raw.githubusercontent.com/eternnoir/pyTelegramBotAPI/master/examples/detailed_example/kitten.jpg',
#         #                                  input_message_content=types.InputTextMessageContent('hello'))
#         bot.answer_inline_query(inline_query.id, [r,hell], cache_time=2)
#     except Exception as e:
#         print(e)


# def main_loop():
#     bot.polling(True)
#     while 1:
#         time.sleep(3)


# if __name__ == '__main__':
#     try:
#         main_loop()
#     except KeyboardInterrupt:
#         print >> sys.stderr, '\nExiting by user request.\n'
# sys.exit(0)