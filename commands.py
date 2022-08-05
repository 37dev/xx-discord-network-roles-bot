import nextcord
from nextcord.ext import commands

from config import DISCORD_GUILD_ID
from embeds import InitialEmbed
from views import NetworkRolesView


class UserNetworkRolesCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        guild_ids=[DISCORD_GUILD_ID], description="Change User Network Roles Command"
    )
    async def verify_network_roles(self, interaction: nextcord.Interaction):
        view = NetworkRolesView(interaction=interaction)
        embed = InitialEmbed()
        await interaction.response.send_message(view=view, embed=embed, ephemeral=True)


def setup(bot):
    bot.add_cog(UserNetworkRolesCog(bot))
