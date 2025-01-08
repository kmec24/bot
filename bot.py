from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from flask import Flask, request
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
        "To order:\n"
        "Send us your Name, Mobile Number, Record Name.\n"
        "Example:\n"
        "Name: \n"
        "Mobile: \n"
        "Record Subject: \n"
    )

# Handle messages and forward details
async def handle_message(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    user_name = update.message.from_user.first_name or "User"
    # Forward the details to you
    await context.bot.send_message(
        chat_id=OWNER_ID,
        text=f"New Order from {user_name}:\n\n{user_message}"
    )
    # Acknowledge the user
    await update.message.reply_text(
        "Thanks for your details! We'll contact you shortly. 👍"
    )

# Flask route to trigger the bot polling
@app.route("/")
def index():
    return "Bot is running!"

# Function to run the bot using polling
def run_polling():
    # Create the Application instance with the bot token
    application = Application.builder().token(BOT_TOKEN).build()

    # Handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start polling for Telegram updates
    application.run_polling()

# Start the Flask app and the bot polling in separate threads
if __name__ == "__main__":
    # Start Flask server in a separate thread
    threading.Thread(target=app.run, kwargs={"host": "0.0.0.0", "port": 5000}).start()
    # Run polling for the bot
    run_polling()
