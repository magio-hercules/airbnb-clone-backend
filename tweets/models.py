from django.db import models
from common.models import CommonModel


class Tweet(CommonModel):
    payload = models.CharField(
        max_length=180,
        default="",
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="tweets",
    )

    def __str__(self) -> str:
        # return f"{self.user}'s payload : {self.payload}"
        return self.payload

    def like_count(self):
        return self.likes.all().count()


class Like(CommonModel):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
    tweet = models.ForeignKey(
        "tweets.tweet",
        on_delete=models.CASCADE,
        related_name="likes",
    )

    def __str__(self) -> str:
        return f"{self.user}'s like"
