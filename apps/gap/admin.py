from django.contrib import admin

from apps.gap.models import Room, Opinion, Comment, OpinionLike


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']


@admin.register(Opinion)
class OpinionAdmin(admin.ModelAdmin):
    list_display = ['title', 'body', 'like_count']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['body', 'author', 'like_count']

@admin.register(OpinionLike)
class OpinionLikeAdmin(admin.ModelAdmin):
    pass