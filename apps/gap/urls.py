from django.urls import path

from apps.gap.views import RoomListView, RoomDetailView, LikeOpinionView, SearchOpinionView, OpinionDetailView

app_name = 'gap'
urlpatterns = [
    path('rooms/', RoomListView.as_view(), name='rooms'),
    path('room/<pk>', RoomDetailView.as_view(), name='room'),
    path('opinion/<pk>', OpinionDetailView.as_view(), name='opinion'),
    path('like/<pk>', LikeOpinionView.as_view(), name='opinion-like'),
    path('search', SearchOpinionView.as_view(), name='search-opinion'),

]
