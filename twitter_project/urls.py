from django.contrib import admin
from django.urls import path, include
from twitter_project.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', form_twit),
    path('accounts/', include('allauth.urls')),
]
