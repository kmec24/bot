from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Your Telegram Bot Token and User ID
BOT_TOKEN = "7857880959:AAE3hNXpDjOemmElAX9vIYse5tMhjdaU-gs"
OWNER_ID = "5960570782"

# Start command
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "Welcome to RecordWriterBot! 🎉\n"
        "We write records for Physics, Chemistry, and Botany.\n"
        "Rate: ₹1500 per record.\n"
        "Available within 10 kms of ECIL.\n\n"
        "To order:\n"
        "Send us your Name, Mobile Number, Record Type, and Subject.\n"
        "Example:\n"
        "Name: John Doe\n"
        "Mobile: 9876543210\n"
        "Record: Botany Practical\n"
        "Subject: Botany\n"
        "We’ll reach you soon!"
    )

# Handle messages and forward details
def handle_message(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    user_name = update.message.from_user.first_name or "User"
    # Forward the details to you
    context.bot.send_message(
        chat_id=OWNER_ID,
        text=f"New Order from {user_name}:\n\n{user_message}"
    )
    # Acknowledge the user
    update.message.reply_text(
        "Thanks for your details! We'll contact you shortly. 👍"
    )

def main():
    updater = Updater(BOT_TOKEN)

    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
