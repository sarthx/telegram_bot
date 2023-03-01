import asyncio
from telegram import KeyboardButton, ReplyKeyboardMarkup, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import *

button = [[KeyboardButton("/payment"), KeyboardButton("/rules"), KeyboardButton("/contact")], [KeyboardButton("/services"), KeyboardButton("/subscription"), KeyboardButton("/donate")]]
print(type(button))
print(button)
reply = ReplyKeyboardMarkup(button, resize_keyboard=True)
print(type(reply))
print(reply)
price = "0.00848"
pay = "www.stripe.com"
newline="\n"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(chat_id=update.effective_chat.id, text="sarthak", reply_markup=reply)

#async def product(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#    await context.bot.send_message(chat_id=update.effective_chat.id, title="Lamborgini", description = "a well behtf",payload="greed", provider_token="2051251535:TEST:OTk5MDA4ODgxLTU", currency="usd", prices=145)

async def butto(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
            [
            InlineKeyboardButton("Bitcoin Payment", callback_data="1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"),
            InlineKeyboardButton("Dogecoin Payment", callback_data="1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNb"),
            ],
            [
            InlineKeyboardButton("Etherium Payment", callback_data="1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNc")
            ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Please choose One Option:", reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query

    await query.answer()

    await query.edit_message_text(text=f"Purchase: 1 Month Subscription{newline}Price: {price} BTC{newline}Wallet Address: {query.data}")

def main() -> None:
    application = Application.builder().token("6032000040:AAFPqTE6XFgttOOS57QkLHPs3WLM0QIJzR8").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT, butto))
    #application.add_handler(MessageHandler("product", product))
    application.add_handler(CallbackQueryHandler(button))

    application.run_polling()

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())

if __name__ == "__main__":
    main()