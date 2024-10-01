from django.contrib import admin
from .models import Review


class WordFilter(admin.SimpleListFilter):

    title = "Filter by words!"

    parameter_name = "word"

    def lookups(self, request, model_admin):
        return [
            ("good", "Good"),
            ("great", "Great"),
            ("awesome", "Awesome"),
        ]

    def queryset(self, request, reviews):
        word = self.value()
        if word:
            return reviews.filter(payload__contains=word)
        else:
            reviews


class GoodReviewFilter(admin.SimpleListFilter):
    title = "Good or Bad revies"

    parameter_name = "type"

    def lookups(self, request, model_admin):
        return [
            ("good_review", "Good Review"),
            ("bad_review", "Bad Review"),
        ]

    def queryset(self, request, reviews):
        print(request)
        print(reviews)
        type = self.value()
        print(type)
        if type:
            if type == "good_review":
                return reviews.filter(rating__gte=3)
            else:
                return reviews.filter(rating__lt=3)
        else:
            reviews


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = (
        "__str__",
        "payload",
    )
    list_filter = (
        WordFilter,
        GoodReviewFilter,
        "rating",
        "user__is_host",
        "room__category",
        "room__pet_friendly",
    )
