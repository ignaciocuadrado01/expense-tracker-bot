import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

load_dotenv()

TOKEN=os.getenv("TELEGRAM_BOT_TOKEN")

async def start(update:Update, contexto:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("¡Hola! Soy tu bot de seguimiento de gastos. \n" 
                                    "Todavia estoy en construccion!")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    print("Bot corriendo...")
    app.run_polling()
