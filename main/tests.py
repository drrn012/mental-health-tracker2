from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User
from .models import MoodEntry

class MainTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpassword")

    def test_main_template_uses_correct_page_title(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get("/", cookies={'last_login': 'some_value'})
        html_response = response.content.decode("utf8")
        self.assertIn("PBD Mental Health Tracker", html_response)

    def test_main_url_is_exist(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get("/", cookies={'last_login': 'some_value'})
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get("/", cookies={'last_login': 'some_value'})
        self.assertTemplateUsed(response, "main.html")

    def test_nonexistent_page(self):
        response = self.client.get("/skibidi/")
        self.assertEqual(response.status_code, 404)

    def test_strong_mood_user(self):
        now = timezone.now()
        mood = MoodEntry.objects.create(
            mood="Happy",
            time=now,
            feelings="I'm happy, even though my clothes are soaked from the rain :(",
            mood_intensity=8,
            user=self.user
        )
        self.assertTrue(mood.is_mood_strong)
