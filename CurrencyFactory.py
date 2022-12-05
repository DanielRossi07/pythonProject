from dataclasses import dataclass


@dataclass
class Currency:
    asset_id: str
    name: str
    type_is_crypto:  bool
    price_usd: str

    def __init__(self, currency):
        self.asset_id = currency[0]['asset_id']
        self.name = currency[0]['name']
        self.type_is_crypto = currency[0]['type_is_crypto']
        self.price_usd = currency[0]['price_usd']


