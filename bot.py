from nextcord.ext import commands
from dotenv import load_dotenv

from constants import BOT_TOKEN
from db import engine
from models import Base
from tasks import (
    update_discord_user_roles_task,
    update_nominator_addresses_task,
    update_validator_addresses_task
)

# load bot environ
load_dotenv()

# create model schemas
Base.metadata.create_all(engine)

# start bot
bot = commands.Bot()

# start async tasks
update_discord_user_roles_task.start()
update_validator_addresses_task.start()
update_nominator_addresses_task.start()

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


bot.run(BOT_TOKEN)


# user should first execute command like /verify_network_roles
# show message with buttons:
# "remove all roles" if one or more is set, remove role btn for the one that is already set and add role if not set
# the text of the messages must mention that the identity must be set on chain first, or it will be disabled