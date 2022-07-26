import re


REGEX_PATTERN = "^.{3,32}#[0-9]{4}$"

def extract_discord_username_from_identity_of(identity_of):
    identity_additional_info = identity_of["info"]["additional"]
    for identity_info in identity_additional_info:
        for value in identity_info.values():
            if discord_user := re.match(REGEX_PATTERN, value):
                return discord_user
