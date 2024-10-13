from rest_framework.test import APITestCase
from . import models
from users import models as users_model


# 과제 - GET, POST
class TestTweets(APITestCase):

    USERNAME = "Test User"
    PAYLOADS = [
        "Tweet Payload 1",
        "Tweet Payload 2",
        "Tweet Payload 3",
        "Tweet Payload 4",
        "Tweet Payload 5",
    ]
    URL = "/api/v1/tweets/"

    def setUp(self):
        new_user = users_model.User.objects.create(
            name=self.USERNAME,
            language="kr",
            currency="won",
        )

        for paylaod in self.PAYLOADS:
            models.Tweet.objects.create(
                user=new_user,
                payload=paylaod,
            )

        self.user = new_user

    def test_all_tweet(self):
        print(f"GET {self.URL}")

        response = self.client.get(self.URL)
        data = response.json()

        self.assertEqual(
            response.status_code,
            200,
            "Status code isn't 200.",
        )
        self.assertIsInstance(
            data,
            list,
        )
        self.assertEqual(
            len(data),
            len(self.PAYLOADS),
        )
        for index, tweet in enumerate(data):
            self.assertEqual(
                tweet["payload"],
                self.PAYLOADS[index],
            )

    def test_create_tweet(self):
        print(f"POST {self.URL}")

        NEW_PAYLOAD = "new tweet payload"

        self.client.force_login(
            self.user,
        )

        response = self.client.post(
            self.URL,
            data={
                "payload": NEW_PAYLOAD,
            },
            headers={
                "X-USERNAME": self.USERNAME,
            },
        )

        self.assertEqual(
            response.status_code,
            200,
            "Status code isn't 200.",
        )

        data = response.json()

        self.assertEqual(
            data["payload"],
            NEW_PAYLOAD,
        )


# 과제 - GET, PUT, DELETE
class TestTweet(APITestCase):
    USERNAME = "Test User"
    PAYLOAD = "Test Tweet"
    NEW_PAYLOAD = "new tweet payload"
    URL = "/api/v1/tweets/1"

    def setUp(self):
        new_user = users_model.User.objects.create(
            name=self.USERNAME,
            language="kr",
            currency="won",
        )

        models.Tweet.objects.create(
            user=new_user,
            payload=self.PAYLOAD,
        )

        self.user = new_user

    def test_get_tweet(self):
        print(f"GET {self.URL}")

        response = self.client.get(self.URL)
        data = response.json()

        self.assertEqual(
            response.status_code,
            200,
            "Status code isn't 200.",
        )

        self.assertIsInstance(
            data,
            dict,
        )

        self.assertEqual(
            data["payload"],
            self.PAYLOAD,
        )

        self.assertEqual(
            data["user"]["name"],
            self.USERNAME,
        )

    def test_put_tweet(self):
        print(f"PUT {self.URL}")

        self.client.force_login(
            self.user,
        )

        response = self.client.put(
            self.URL,
            data={
                "user": self.user,
                "payload": self.NEW_PAYLOAD,
            },
        )

        data = response.json()

        self.assertEqual(
            response.status_code,
            200,
            "Status code isn't 200.",
        )

        self.assertEqual(
            data["payload"],
            self.NEW_PAYLOAD,
        )

    def test_delete_tweet(self):
        print(f"DELETE {self.URL}")

        self.client.force_login(
            self.user,
        )

        response = self.client.delete(self.URL)

        self.assertEqual(
            response.status_code,
            204,
            "Status code isn't 204.",
        )
