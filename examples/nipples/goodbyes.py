from boobs import Nipple, Cock
from boobs.bot.rules import Text

# Make a nipple of a bot.
nip = Nipple()


@nip.on.message(Text(["bye", "cheers"], ignore_case=True))
async def bye_handler(c: Cock) -> None:
    await c.cum("See you soon!")


@nip.on.message(Text(["take care", "have a good day"], ignore_case=True))
async def goodbye_handler(c: Cock) -> None:
    await c.cum("You too, bye!")
