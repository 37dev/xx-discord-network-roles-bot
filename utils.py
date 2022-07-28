import re


DISCORD_USERNAME_REGEX_PATTERN = "^.{3,32}#[0-9]{4}$"


def extract_discord_username_from_identity_of(identity_of):
    identity_additional_info = identity_of["info"]["additional"]
    for identity_info in list(flatten(identity_additional_info)):
        if isinstance(identity_info, dict):
            for _, value in identity_info.items():
                if discord_user := re.match(DISCORD_USERNAME_REGEX_PATTERN, value):
                    return discord_user.string


def flatten(nested_list):
    for item in nested_list:
        if isinstance(item, (list, tuple)):
            for x in flatten(item):
                yield x
        else:
            yield item
