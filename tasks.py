import asyncio

from nextcord.ext import tasks

from roles import (
    update_discord_user_network_roles,
    update_validator_addresses,
    update_nominator_addresses,
)


@tasks.loop(seconds=30)
async def update_discord_user_roles_task():
    loop = asyncio.get_running_loop()
    await loop.run_in_executor(None, update_discord_user_network_roles)


@tasks.loop(seconds=30)
async def update_validator_addresses_task():
    loop = asyncio.get_running_loop()
    await loop.run_in_executor(None, update_validator_addresses)


@tasks.loop(seconds=30)
async def update_nominator_addresses_task():
    loop = asyncio.get_running_loop()
    await loop.run_in_executor(None, update_nominator_addresses)
