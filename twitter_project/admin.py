from django.contrib import admin

from .models import Twit


class TwitAdmin(admin.ModelAdmin):
    list_display = ("user", "text", "created_date", 'retwits')
    # list_editable = ("user",)
    search_fields = ["user__username", "created_date"]
    fields = ("user", "text", "created_date", "re_twit")
    list_filter = ("user",)

    def retwits(self, obj):
        return "\n".join([user.username for user in obj.re_twit.all()])

admin.site.register(Twit, TwitAdmin)
