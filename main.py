import MazeHandling as mh

games_dict = {"":""}

import logging

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
# Best practice would be to replace context with an underscore,
# since context is an unused local variable.
# This being an example and not having context present confusing beginners,
# we decided to have it present as context.
def start(update: Update, context: CallbackContext) -> None:
    """Sends explanation on how to use the bot."""
    games_dict[update.message.chat_id] = mh.Maze(15, 15)
    update.message.reply_text("```\n" + games_dict[update.message.chat_id].mazeToString() + "\n```", parse_mode="MarkdownV2")
        
def go_up(update: Update, context: CallbackContext) -> None:
    """Add a job to the queue."""
    chat_id = update.message.chat_id
    games_dict[chat_id].movePlayer("w")
    if (games_dict[chat_id].player == games_dict[chat_id].exit):
        update.message.reply_text("You win\. Type `/start` to start again", parse_mode = "MarkdownV2")
        games_dict.pop(chat_id)
        return
    update.message.reply_text("```\n" + games_dict[update.message.chat_id].mazeToString() + "\n```", parse_mode="MarkdownV2")

def go_left(update: Update, context: CallbackContext) -> None:
    """Add a job to the queue."""
    chat_id = update.message.chat_id
    games_dict[chat_id].movePlayer("a")
    if (games_dict[chat_id].player == games_dict[chat_id].exit):
        update.message.reply_text("You win\. Type `/start` to start again", parse_mode = "MarkdownV2")
        games_dict.pop(chat_id)
        return
    update.message.reply_text("```\n" + games_dict[update.message.chat_id].mazeToString() + "\n```", parse_mode="MarkdownV2")

def go_down(update: Update, context: CallbackContext) -> None:
    """Add a job to the queue."""
    chat_id = update.message.chat_id
    games_dict[chat_id].movePlayer("s")
    if (games_dict[chat_id].player == games_dict[chat_id].exit):
        update.message.reply_text("You win\. Type `/start` to start again", parse_mode = "MarkdownV2")
        games_dict.pop(chat_id)
        return
    update.message.reply_text("```\n" + games_dict[update.message.chat_id].mazeToString() + "\n```", parse_mode="MarkdownV2")

def go_right(update: Update, context: CallbackContext) -> None:
    """Add a job to the queue."""
    chat_id = update.message.chat_id
    games_dict[chat_id].movePlayer("d")
    if (games_dict[chat_id].player == games_dict[chat_id].exit):
        update.message.reply_text("You win\. Type `/start` to start again", parse_mode = "MarkdownV2")
        games_dict.pop(chat_id)
        return
    update.message.reply_text("```\n" + games_dict[update.message.chat_id].mazeToString() + "\n```", parse_mode="MarkdownV2")

def main() -> None:
    """Run bot."""
    # Create the Updater and pass it your bot's token.
    tokenfile = open("token.txt", 'r')
    token = tokenfile.readline()
    updater = Updater(token)
    tokenfile.close()

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", start))
    dispatcher.add_handler(CommandHandler("w", go_up))
    dispatcher.add_handler(CommandHandler("a", go_left))
    dispatcher.add_handler(CommandHandler("s", go_down))
    dispatcher.add_handler(CommandHandler("d", go_right))

    # Start the Bot
    updater.start_polling()

    # Block until you press Ctrl-C or the process receives SIGINT, SIGTERM or
    # SIGABRT. This should be used most of the time, since start_polling() is
    # non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
