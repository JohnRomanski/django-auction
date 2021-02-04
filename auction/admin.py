from django.contrib import admin
from auction import models

admin.site.register(models.biditem.BidItem)
admin.site.register(models.BidBasket)
admin.site.register(models.Auction)
admin.site.register(models.lot.Lot)
