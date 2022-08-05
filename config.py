import os
from dotenv import load_dotenv

# load bot environ
load_dotenv()

BOT_TOKEN = os.environ["BOT_TOKEN"]

XX_SUBSTRATE_URL = os.environ["XX_SUBSTRATE_URL"]

DISCORD_GUILD_ID = int(os.environ["DISCORD_GUILD_ID"])

# global vars
DISCORD_VALIDATOR_ROLE = "validator"
DISCORD_NOMINATOR_ROLE = "nominator"

DISCORD_XX_ROLES = [DISCORD_VALIDATOR_ROLE, DISCORD_NOMINATOR_ROLE]
