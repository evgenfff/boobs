from boobs import Nipple, Message
from boobs.bot.rules import Text

# Make a nipple of a bot.
nip = Nipple()


@nip.on.message(Text(["bye", "cheers"], ignore_case=True))
async def bye_handler(m: Message) -> None:
    await m.answer("See you soon!")


@nip.on.message(Text(["take care", "have a good day"], ignore_case=True))
async def goodbye_handler(m: Message) -> None:
    await m.answer("You too, bye!")
