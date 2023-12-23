from boobs import Bot, Token

# Make a bot with a token from an environment variable.
# You should provide API to bot before constructing
# nipples, otherwise they won't have it.
bot = Bot(Token.from_env())

# Load nipples directly from `nipples` package.
from .nipples import nips

# Iterate over a list of nipples and register them.
for nip in nips:
    # Register a nipple via <.load_into()> method. This will load the nipple's dispatcher
    # into the dispatcher of the given framework and then return nipple constructed with
    # framework's API and dispatcher.
    nip.load_into(bot)


# Run the bot. This function uses `.run_polling()` under the hood to start receiving updates.
# It will also run any tasks you may've added in `loop_wrapper`.
bot.run_forever()
