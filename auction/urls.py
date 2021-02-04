from django.urls import include, path
import auction.views

urlpatterns = [
    path('', auction.views.AuctionListView.as_view(), name='auctions'),
    path('bids/', auction.views.BidListView.as_view(), name='bids'),
    path('bids/delete/<bid_id>/', auction.views.BidDetailView.as_view(action="delete"), name='delete_bid'),
    path('auction/<slug>/', auction.views.AuctionView.as_view(), name='auction'),
    path('auction/<auctionslug>/lot/<slug>/<pk>/', auction.views.LotDetailView.as_view(), name='lot'),
]