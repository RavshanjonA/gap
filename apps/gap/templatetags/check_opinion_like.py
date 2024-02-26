from django import template

from apps.gap.models import OpinionLike

register = template.Library()



def check_like(opnion, user):
    return OpinionLike.objects.filter(opinion=opnion, user=user).exists()
register.filter(check_like)