from asyncio import run

from boobs import API, Poller, Token
from boobs.modules import logger

api = API(Token.from_env())


async def main():
    poller = Poller(api)

    async for update in poller.poll():
        await logger.debug("Handling", update=update)


run(main())
