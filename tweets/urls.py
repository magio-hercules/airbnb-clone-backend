from django.urls import path
from . import views


urlpatterns = [
    # GET /api/v1/tweets: See all tweets
    # POST /api/v1/tweets: Create a tweet
    # GET /api/v1/tweets/<int:pk>: See a tweet
    # PUT /api/v1/tweets/<int:pk>: Edit a tweet
    # DELETE /api/v1/tweets/<int:pk>: Delete a tweet
    path("", views.Tweets.as_view()),
    path("<int:pk>", views.TweetDetail.as_view()),
]
