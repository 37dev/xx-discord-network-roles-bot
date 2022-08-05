from nextcord import Embed


class InitialEmbed(Embed):
    TITLE = "Select the network roles to be added on your discord account"
    DESCRIPTION = "Make sure you have your discord username added to your nominator / validator wallet identity"
    COLOR = 0x2FA737

    def __init__(self):
        super().__init__(
            title=self.TITLE, description=self.DESCRIPTION, color=self.COLOR
        )


class RoleAddedSuccessfullyEmbed(Embed):
    TITLE = "Select the network roles to be added on your discord account"
    DESCRIPTION = "***{}*** role added successfully"
    COLOR = 0x0096FF

    def __init__(self, role):
        super().__init__(
            title=self.TITLE,
            description=self.DESCRIPTION.format(role.capitalize()),
            color=self.COLOR,
        )


class RolesResetSuccessfullyEmbed(Embed):
    TITLE = "Select the network roles to be added on your discord account"
    DESCRIPTION = "Roles successfully reset"
    COLOR = 0x0096FF

    def __init__(self):
        super().__init__(
            title=self.TITLE, description=self.DESCRIPTION, color=self.COLOR
        )


class IdentityNotSetErrorEmbed(Embed):
    TITLE = "Select the network roles to be added on your discord account"
    DESCRIPTION = (
        "***{}*** role not added. You must set discord username identity first"
    )
    COLOR = 0xFF0000

    def __init__(self, role):
        super().__init__(
            title=self.TITLE,
            description=self.DESCRIPTION.format(role.capitalize()),
            color=self.COLOR,
        )
