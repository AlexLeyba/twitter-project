# coding=utf-8
from django.forms import ModelForm
from twitter_project.models import Twit

class TwitForm(ModelForm):
    class Meta:
        model = Twit
        fields = ("text",)