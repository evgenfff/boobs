from boobs import Bot, Token
from boobs.bot.rules import Command, Text
from boobs.bot.updates import CallbackQuery, Message
from boobs.tools.keyboard import Callback, InlineKeyboardBuilder

# Make a bot with a token from an environment variable.
bot = Bot(Token.from_env())

# Create an inline keyboard with a button that will be used to trigger a callback.
INLINE_KEYBOARD = (
    InlineKeyboardBuilder()
    .add(Callback("🍎 Apple", "apple"))
    .add(Callback("🍊 Orange", "orange"))
    .add(Callback("🍌 Banana", "banana"))
    .row()
    .add(Callback("Won't choose", "stop"))
    .build()
)


@bot.on.message(Command("fruits"))
async def start_handler(m: Message) -> None:
    # This is a handler that sends a simple inline keyboard
    # containing three buttons with their respective callback data.
    await m.answer(
        "Pick any of these fruits on the keyboard!",
        reply_markup=INLINE_KEYBOARD,
    )


@bot.on.callback_query(Text(["apple", "orange", "banana"]))
async def fruit_handler(cq: CallbackQuery) -> None:
    fruit = cq.data.capitalize()

    # Answer a callback query using <.answer()> method.
    # To display an alert, pass `show_alert` param.
    await cq.answer(
        f"You chose a fruit! {fruit}s are healthy and delicious 😌", show_alert=True
    )


@bot.on.callback_query(Text("stop"))
async def stop_handler(cq: CallbackQuery) -> None:
    await cq.ctx_api.edit_message_text(
        "That's ok. Some choices are just too hard to make.",
        message_id=cq.message.message_id,
        chat_id=cq.message.chat.id,
    )


# Run the bot. This function uses `.run_polling()` under the hood to start receiving updates.
# It will also run any tasks you may've added in `loop_wrapper`.
bot.run_forever()
