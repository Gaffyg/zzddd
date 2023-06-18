from django.urls import path
from .views import *

urlpatterns = [
    path('', NewsListView.as_view(), name='home'),
    path('concerts/', ConcertsListView.as_view(), name='concerts'),
    path('group/', AboutGroupListView.as_view(), name='group'),
    path('clips/', ClipsListView.as_view(), name='clips'),
    path('links/', LinksListView.as_view(), name='links'),
    path('buy/<slug:concert_slug>/', buy_ticket, name='buy'),
    path('success-buy/', success_buy, name='success')
]
