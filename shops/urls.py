from django.conf.urls import url
from shops.views import ShopsListView, LikedShopsListView, LikeShopView, RemoveShopView

urlpatterns = [
    url(r'^shops/$', ShopsListView.as_view(), name="list_of_shops"),
    url(r'^shops/liked/$', LikedShopsListView.as_view(), name="list_of_liked_shops"),
    url(r'^shops/(?P<shop>\d+)/like/$', LikeShopView.as_view(), name="like_shop"),
    url(r'^shops/(?P<shop>\d+)/remove/$', RemoveShopView.as_view(), name="remove_shop"),
]
