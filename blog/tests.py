from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Post

# Create your tests here.


class BlogTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="tester",
            email="pirat@gmail.com",
            password="datenbank"
        )

        self.post = Post.objects.create(
            title="A title",
            body="Some content",
            author=self.user,
        )

    def test_string_representation(self):
        post = Post(title="A sample title")
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f"{self.post.title}", "A title")
        self.assertEqual(f"{self.post.author}", "tester")
        self.assertEqual(f"{self.post.body}", "Some content")

    def test_post_live_view(self):
        res = self.client.get(reverse("home"))
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "Some content")
        self.assertTemplateUsed(res, "home.html")

    def test_post_detail_view(self):
        res = self.client.get("/post/1/")
        no_res = self.client.get("/post/10")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(no_res.status_code, 200)
        self.assertContains(res, "A title")
        self.assertTemplateUsed(res, "post_detail.html")
