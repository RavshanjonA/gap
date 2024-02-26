from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from apps.gap.models import Room, Opinion, Comment, OpinionLike


class RoomListView(View):
    def get(self, request):
        rooms = Room.objects.all()
        return render(request, 'gap/rooms.html', {"rooms": rooms})


class RoomDetailView(View):
    def get(self, request, pk):
        room = Room.objects.get(pk=pk)
        opinions = sorted(Opinion.objects.filter(room=room), key=lambda o: o.like_count, reverse=True)
        context = {
            "room": room,
            "opinions": opinions
        }
        return render(request, "gap/opinoins.html", context=context)


class LikeOpinionView(LoginRequiredMixin, View):
    def get(self, request, pk):
        opinion = Opinion.objects.get(pk=pk)
        like, created = OpinionLike.objects.get_or_create(user=request.user, opinion=opinion)
        if not created:
            like.delete()
        return redirect(reverse("gap:room", kwargs={"pk": opinion.room.pk}))


class OpinionDetailView(LoginRequiredMixin, View):
    def get(self, request, pk):
        opinion = Opinion.objects.get(pk=pk)
        comments = opinion.comments.all().order_by("-created_at")
        comments = sorted(comments, key=lambda c: c.like_count, reverse=True)
        context = {
            "opinion": opinion,
            "comments": comments
        }
        return render(request, "gap/comments.html", context=context)


class CommentLikeView(View):
    def get(self, request, pk):
        comment = Comment.objects.get(pk=pk)


class SearchOpinionView(View):
    def get(self, request):
        q = request.GET.get('q', None)
        if q:
            opinions = Opinion.objects.filter(Q(title__icontains=q) | Q(body__icontains=q))
        else:
            opinions = None

        context = {
            'param': q,
            'opinions': opinions
        }
        return render(request, 'gap/search-opinion.html', context=context)
