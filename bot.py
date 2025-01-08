from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from flask import Flask
import os
import threading

# Your Telegram Bot Token and User ID
BOT_TOKEN = "7857880959:AAE3hNXpDjOemmElAX9vIYse5tMhjdaU-gs"
OWNER_ID = "5960570782"

# Initialize Flask app
app = Flask(__name__)

# Start command
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(
        "Welcome to RecordWriterBot! 🎉\n"
        "We write records of any subject.\n"
        "Available within 10 kms of ECIL.\n\n"
        "To make an enquiry:\n"
        "Send us your Name, Mobile Number, Record Name.\n"
        "Example:\n"
        "Name: \n"
        "Mobile: \n"
        "Record Subject: \n"
    )

# Handle messages and forward details as enquiries
async def handle_message(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    user_name = update.message.from_user.first_name or "User"
    # Forward the details to you as an enquiry
    await context.bot.send_message(
        chat_id=OWNER_ID,
        text=f"New Enquiry from {user_name}:\n\n{user_message}"
    )
    # Acknowledge the user with an enquiry confirmation
    await update.message.reply_text(
        "Thanks for your enquiry! We'll contact you shortly. 👍\n\nThis is an enquiry, not an order."
    )

def start_polling():
    # Create the Application instance with the bot token
    application = Application.builder().token(BOT_TOKEN).build()

    # Handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start polling
    application.run_polling()

# Flask route to make sure the web service is running
@app.route('/')
def hello():
    return "The bot is running!"

def main():
    # Start the bot in a separate thread to avoid blocking Flask
    bot_thread = threading.Thread(target=start_polling)
    bot_thread.start()

    # Run the Flask web server
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))

if __name__ == "__main__":
    main()
