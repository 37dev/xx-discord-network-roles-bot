from nextcord.ext import tasks

from roles import (
    update_discord_user_network_roles,
    update_validator_addresses,
    update_nominator_addresses,
)


@tasks.loop(minutes=5)
async def update_discord_user_roles_task():
    update_discord_user_network_roles()


@tasks.loop(minutes=5)
async def update_validator_addresses_task():
    update_validator_addresses()


@tasks.loop(minutes=5)
async def update_nominator_addresses_task():
    update_nominator_addresses()
