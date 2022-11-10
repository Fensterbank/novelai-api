from asyncio import run

from boilerplate import API


async def main():
    async with API() as api_handler:    # noqa: F841
        pass


run(main())
