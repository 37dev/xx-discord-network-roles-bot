import nextcord
from nextcord.ext import commands
from config import BOT_TOKEN, DISCORD_XX_ROLES
from db import engine
from models import Base
from tasks import (
    update_discord_user_roles_task,
    update_nominator_addresses_task,
    update_validator_addresses_task,
)

# create db schemas
Base.metadata.create_all(engine)

# add member intent
intents = nextcord.Intents.default()
intents.members = True

# start bot
bot = commands.Bot(intents=intents)

# start async tasks
update_discord_user_roles_task.start()
update_validator_addresses_task.start()
update_nominator_addresses_task.start()

# start command cog
bot.load_extension("commands")


@bot.event
async def on_ready():
    # add roles to server if they don't exist
    for guild in bot.guilds:
        guild_roles_names = [role.name for role in guild.roles]
        for role in DISCORD_XX_ROLES:
            if role not in guild_roles_names:
                print(f"Adding role {role} to guild {guild.name}")
                await guild.create_role(name=role)

    print(f"We have logged in as {bot.user}")


bot.run(BOT_TOKEN)


# user should first execute command like /verify_network_roles
# show message with buttons:
# "remove all roles" if one or more is set, remove role btn for the one that is already set and add role if not set
# the text of the messages must mention that the identity must be set on chain first, or it will be disabled
