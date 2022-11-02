import nextcord
from nextcord.utils import get

from config import DISCORD_VALIDATOR_ROLE, DISCORD_NOMINATOR_ROLE
from embeds import (
    IdentityNotSetErrorEmbed,
    RoleAddedSuccessfullyEmbed,
    RolesResetSuccessfullyEmbed,
)
from roles import is_discord_user_validator, is_discord_user_nominator


class BaseRoleButton(nextcord.ui.Button["NetworkRolesView"]):
    BUTTON_CONFIG = {}

    def __init__(self, **kwargs):
        super().__init__(**self.BUTTON_CONFIG, **kwargs)


class AddValidatorRoleButton(BaseRoleButton):
    label = DISCORD_VALIDATOR_ROLE.upper()
    BUTTON_CONFIG = {
        "row": 1,
        "label": label,
        "style": nextcord.ButtonStyle.success,
    }

    async def callback(self, interaction):
        member = interaction.guild.get_member(interaction.user.id)
        member_username = str(member)

        if is_discord_user_validator(member_username):
            validator_role = get(interaction.guild.roles, name=DISCORD_VALIDATOR_ROLE)
            self.view.update_disabled_role_buttons(disable_validator=True)
            await member.add_roles(validator_role)

            embed = RoleAddedSuccessfullyEmbed(role=DISCORD_VALIDATOR_ROLE)
            await interaction.response.edit_message(view=self.view, embed=embed)
        else:
            embed = IdentityNotSetErrorEmbed(role=DISCORD_VALIDATOR_ROLE)
            await interaction.response.edit_message(view=self.view, embed=embed)


class AddNominatorRoleButton(BaseRoleButton):
    label = DISCORD_NOMINATOR_ROLE.upper()
    BUTTON_CONFIG = {
        "row": 1,
        "label": label,
        "style": nextcord.ButtonStyle.success,
    }

    async def callback(self, interaction):
        member = interaction.guild.get_member(interaction.user.id)
        member_username = str(member)

        if is_discord_user_nominator(member_username):
            nominator_role = get(interaction.guild.roles, name=DISCORD_NOMINATOR_ROLE)
            self.view.update_disabled_role_buttons(disable_nominator=True)
            await member.add_roles(nominator_role)

            embed = RoleAddedSuccessfullyEmbed(role=DISCORD_NOMINATOR_ROLE)
            await interaction.response.edit_message(view=self.view, embed=embed)
        else:
            embed = IdentityNotSetErrorEmbed(role=DISCORD_NOMINATOR_ROLE)
            await interaction.response.edit_message(view=self.view, embed=embed)


class ResetRolesButton(BaseRoleButton):
    label = "RESET"
    BUTTON_CONFIG = {"row": 2, "label": label, "style": nextcord.ButtonStyle.danger}

    async def callback(self, interaction):
        member = interaction.guild.get_member(interaction.user.id)
        member_username = str(member)

        if is_discord_user_validator(member_username):
            validator_role = get(interaction.guild.roles, name=DISCORD_VALIDATOR_ROLE)
            await member.remove_roles(validator_role)

        if is_discord_user_nominator(member_username):
            nominator_role = get(interaction.guild.roles, name=DISCORD_NOMINATOR_ROLE)
            await member.remove_roles(nominator_role)

        self.view.update_disabled_role_buttons(
            disable_nominator=False, disable_validator=False
        )

        embed = RolesResetSuccessfullyEmbed()
        await interaction.response.edit_message(view=self.view, embed=embed)


class NetworkRolesView(nextcord.ui.View):
    def __init__(self, interaction):
        super().__init__()
        self._set_role_buttons(interaction)

    def _set_role_buttons(self, interaction):
        self.add_item(AddValidatorRoleButton())
        self.add_item(AddNominatorRoleButton())
        self.add_item(ResetRolesButton())

        self._set_disabled_role_buttons(interaction)

    def _set_disabled_role_buttons(self, interaction):
        member = interaction.guild.get_member(interaction.user.id)

        validator_role = get(interaction.guild.roles, name=DISCORD_VALIDATOR_ROLE)
        nominator_role = get(interaction.guild.roles, name=DISCORD_NOMINATOR_ROLE)

        disable_validator_button = True if member.get_role(validator_role.id) else False
        disable_nominator_button = True if member.get_role(nominator_role.id) else False

        self.update_disabled_role_buttons(
            disable_validator_button, disable_nominator_button
        )

    def update_disabled_role_buttons(
        self, disable_validator=None, disable_nominator=None
    ):
        disable_reset_button = disable_validator is False and disable_nominator is False

        if not self.children:
            raise ValueError("Children not set")

        for button in self.children:
            if button.label == AddValidatorRoleButton.label:
                if disable_validator is not None:
                    button.disabled = disable_validator
            elif button.label == AddNominatorRoleButton.label:
                if disable_nominator is not None:
                    button.disabled = disable_nominator
            else:
                button.disabled = disable_reset_button
