import aiohttp
from .local_settings import WORDS_API_URL_RANDOM


async def get_random():
                                #trust_env=True
    async with aiohttp.ClientSession() as session:
        async with session.get(WORDS_API_URL_RANDOM) as response:
            return await response.json()
