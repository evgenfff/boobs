from boobs import Nipple, Message
from boobs.bot.rules import Text

# Make a nipple of a bot.
nip = Nipple()


@nip.on.message(Text(["hi", "hello", "hey"], ignore_case=True))
async def hi_handler(m: Message) -> None:
    await m.answer("Glad to see you!")


@nip.on.message(
    Text(["good morning", "good afternoon", "good evening"], ignore_case=True)
)
async def hello_handler(m: Message) -> None:
    await m.answer("Welcome!")
