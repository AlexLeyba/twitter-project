from django.contrib import admin
from django.urls import path, include
from twitter_project.views import *

urlpatterns = [
    path('', form_twit),
    path('user/<int:pk>', user),
    path('user/edit/<int:pk>', edit_twit, name="edit_twit"),
]
