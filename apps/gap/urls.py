from django.urls import path

from apps.gap.views import RoomListView, RoomDetailView, LikeOpinionView

app_name = 'gap'
urlpatterns = [
    path('rooms/', RoomListView.as_view(), name='rooms'),
    path('room/<pk>', RoomDetailView.as_view(), name='room'),
    path('like/<pk>', LikeOpinionView.as_view(), name='opinion-like')

]
