import os
from dotenv import load_dotenv

# load bot environ
load_dotenv()

BOT_TOKEN = os.environ["BOT_TOKEN"]
XX_SUBSTRATE_URL = os.environ["XX_SUBSTRATE_URL"]
GUILD_ID = int(os.environ["GUILD_ID"])
