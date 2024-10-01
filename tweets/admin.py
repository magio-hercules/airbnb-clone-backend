from django.contrib import admin
from .models import Tweet, Like


class WordFilter(admin.SimpleListFilter):
    title = "Filter by words except Elon Musk"

    parameter_name = "word"

    def lookups(self, request, model_admin):
        return [
            ("hi", "Hi"),
            ("hello", "Hello"),
            ("good", "Good"),
        ]

    def queryset(self, request, reviews):
        word = self.value()
        if word:
            return reviews.filter(payload__contains=word).exclude(
                payload__contains="Elon Musk"
            )
        else:
            reviews


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "payload",
        "like_count",
        "created_at",
        "updated_at",
    )

    list_filter = (
        "created_at",
        "updated_at",
    )

    search_fields = (
        "payload",
        "user__username",
    )

    list_filter = (
        WordFilter,
        "created_at",
    )


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "tweet",
        "created_at",
        "updated_at",
    )

    search_fields = ("user__username",)

    list_filter = ("created_at",)
