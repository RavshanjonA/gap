from django.contrib import admin
from django.urls import path, include

from config.views import landing_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page, name='landing_page'),
    path('gap/', include('apps.gap.urls')),
]
