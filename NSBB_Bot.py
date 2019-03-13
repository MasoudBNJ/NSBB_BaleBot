#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Enable logging
import logging

from telegram import LabeledPrice, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, ConversationHandler, RegexHandler

import BotConfigs

import Strings
import json

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)

logger = logging.getLogger(__name__)

users_queue = []
PLACE_RESERVING_STATE = 0


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Started :)')


def help(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Need Help?!')


def echo(bot, update):
    """Echo the user message."""
    update.message.reply_text(update.message.text + " to yourself :D")


def error(bot, update):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, update.message)


def money_request(bot, update, title, description, pan, amount):
    bot.send_invoice(chat_id=update.message.chat_id, title=title, description=description, payload="payload",
                     provider_token=pan, start_parameter="", currency="IRR",
                     prices=[LabeledPrice(title, int(amount))])


def payment_receipt(bot, update):
    successful_payment = update.message.successful_payment
    logger.info("SuccessfulPayment with payload: %s", successful_payment.invoice_payload)
    invoice_payload = json.loads(successful_payment.invoice_payload)
    update.message.reply_text(Strings.receipt_success_message.format(invoice_payload.get('traceNo')))


def send_template_message(bot, update, message, buttons):
    update.message.reply_text(message,
                              reply_markup=ReplyKeyboardMarkup(keyboard=buttons))


def show_main_menu(bot, update):
    send_template_message(bot=bot,
                          update=update,
                          message=Strings.reserve_place_title,
                          buttons=[Strings.reserve_place_buttons])
    return PLACE_RESERVING_STATE


def reserve_place(bot, update):
    user_id = update.effective_user.id
    if user_id in users_queue:
        message = Strings.exist_in_queue_message.format(users_queue.index(user_id) + 1)
    else:
        users_queue.append(user_id)
        message = Strings.added_to_queue_message.format(len(users_queue))

    update.message.reply_text(message)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(token=BotConfigs.token,
                      base_url="https://tapi.bale.ai/")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', show_main_menu)],

        states={
            PLACE_RESERVING_STATE: [RegexHandler(pattern='^(' + Strings.reserve_place_buttons[0] + ')$',
                                                 callback=reserve_place)]
        },

        fallbacks=[]
    )

    dp.add_handler(conv_handler)

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling(poll_interval=2)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()