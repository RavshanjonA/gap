from django.contrib.auth.models import User
from django.db import models
from django.db.models import Model, CharField, TextField, ForeignKey, CASCADE

from apps.shared.models import AbstractModel


class Room(AbstractModel):
    name = CharField(max_length=42)

    def __str__(self):
        return self.name


class Opinion(AbstractModel):
    room = ForeignKey(Room, CASCADE, 'opinions')
    title = CharField(max_length=256)
    body = TextField()
    author = ForeignKey(User, CASCADE, 'opinions')

    @property
    def like_count(self):
        return self.opinionlike_set.count()

    def __str__(self):
        return self.title


class OpinionLike(AbstractModel):
    user = ForeignKey(User, CASCADE, 'likes')
    opinion = ForeignKey(Opinion, CASCADE, )

    def __str__(self):
        return f"{self.opinion}-{self.user}"


class Comment(AbstractModel):
    body = TextField()
    opinion = ForeignKey(Opinion, CASCADE, 'comments')
    author = ForeignKey(User, CASCADE, 'comments')

    @property
    def like_count(self):
        return self.commentlike_set.count()

    def __str__(self):
        return self.body


class CommentLike(AbstractModel):
    user = ForeignKey(User, CASCADE)
    comment = ForeignKey(Comment, CASCADE)

    def __str__(self):
        return f"{self.comment}-{self.user}"
