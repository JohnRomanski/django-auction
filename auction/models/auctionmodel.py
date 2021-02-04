import importlib
from django.conf import settings
from auction.utils.loader import load_class

AUCTION_AUCTION_MODEL = getattr(settings, 'AUCTION_AUCTION_MODEL',
                                  'auction.models.defaults.Auction')
                                  
Auction = load_class(AUCTION_AUCTION_MODEL, 'AUCTION_AUCTION_MODEL')