from config import XX_SUBSTRATE_URL
from models import DiscordUser, Validator, Nominator
from utils import extract_discord_username_from_identity_of
from xx_service import XXNetworkInterface
from db import Session


def update_discord_user_network_roles():
    xx_service = XXNetworkInterface(url=XX_SUBSTRATE_URL)

    with Session() as session:
        # TODO: blocking call - should refactor to async
        identities = xx_service.list_identities()

        # clear db from old records
        session.query(DiscordUser).delete()

        for identity in identities:
            account, identity_of = identity["account"], identity["identity_of"]
            discord_username = extract_discord_username_from_identity_of(identity_of)
            if discord_username is not None:
                discord_user = DiscordUser(username=discord_username)
                session.add(discord_user)
                session.flush()

                if (
                    validator := session.query(Validator)
                    .filter_by(address=account)
                    .first()
                ):
                    validator.discord_user_id = discord_user.id
                    session.add(validator)

                if (
                    nominator := session.query(Nominator)
                    .filter_by(address=account)
                    .first()
                ):
                    nominator.discord_user_id = discord_user.id
                    session.add(nominator)

        session.commit()


def update_validator_addresses():
    xx_service = XXNetworkInterface(url=XX_SUBSTRATE_URL)

    with Session() as session:
        # TODO: blocking call - should refactor to async
        validator_addresses = xx_service.list_validator_addresses()

        # clear db from old records
        session.query(Validator).delete()

        validator_address_objects = []
        for validator_address in validator_addresses:
            validator_address_objects.append(Validator(address=validator_address))

        session.bulk_save_objects(validator_address_objects)

        session.commit()


def update_nominator_addresses():
    xx_service = XXNetworkInterface(url=XX_SUBSTRATE_URL)

    with Session() as session:
        # TODO: blocking call - should refactor to async
        nominator_addresses = xx_service.list_nominator_addresses()

        # clear db from old records
        session.query(Nominator).delete()

        nominator_address_objects = []
        for nominator_address in nominator_addresses:
            nominator_address_objects.append(Nominator(address=nominator_address))

        session.bulk_save_objects(nominator_address_objects)

        session.commit()


def is_discord_user_validator(discord_username):
    with Session() as session:
        if (
            discord_user := session.query(DiscordUser)
            .filter_by(username=discord_username)
            .first()
        ):
            if validator := bool(discord_user.validator):
                return validator

        return False


def is_discord_user_nominator(discord_username):
    with Session() as session:
        if (
            discord_user := session.query(DiscordUser)
            .filter_by(username=discord_username)
            .first()
        ):
            if nominator := bool(discord_user.nominator):
                return nominator

        return False
