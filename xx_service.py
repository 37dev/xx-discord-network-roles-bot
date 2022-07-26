from substrateinterface import SubstrateInterface
from pprint import pprint


class XXNetworkInterface(SubstrateInterface):
    def __int__(self, url: str = None):
        super().__init__(url=url)

    def list_identities(self):
        query = self.query_map('Identity', 'IdentityOf')

        identities = []
        for account, identity in query:
            identities.append({
                "account": account,
                "identity_of": identity
            })

        return identities

    def list_validator_addresses(self):
        query = self.query_map('Staking', 'Validators')

        validator_addresses = []
        for account, _ in query:
            validator_addresses.append(account)

        return validator_addresses

    def list_nominator_addresses(self):
        query = self.query_map('Staking', 'Nominators')

        validator_addresses = []
        for account, _ in query:
            validator_addresses.append(account)

        return validator_addresses
