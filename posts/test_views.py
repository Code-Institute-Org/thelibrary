from django.test import TestCase, Client
from django.urls import reverse
from users.models import User
from courses.models import Course
from slack.models import SlackChannel
from posts.models import Post, PostCategory


class AllPostsViewTests(TestCase):

    def setUp(self):
        user_a = User(username="user_a", email="a@x.com")
        user_a.set_password('pass')
        user_a.save()
        user_b = User(username="user_b", email="b@x.com")
        user_b.set_password('pass')
        user_b.save()

        # Create categories
        category_a = PostCategory.objects.create(name="category_a")
        category_b = PostCategory.objects.create(name="category_b")

        # Create slack channel
        channel = SlackChannel.objects.create(
            name="#test", slack_channel_id="ABCDE")

        # create course
        course = Course.objects.create(
            name="A1")

        for i in range(20):
            post = Post(title=f"post title {i}")
            post.summary = f"post summary {i}"
            post.slug = f"post-title-{i}"
            post.body = 'body'
            post.slack_channel = channel
            post.course = course

            if i % 2 == 0:
                post.author = user_a.userprofile
                post.category = category_a
            else:
                post.author = user_b.userprofile
                post.category = category_b

            if i < 15:
                post.status = "Published"
            elif i < 18:
                post.status = "Review"

            post.save()

    def test_can_access_when_logged_in(self):
        c = Client()
        user_login = c.login(username='user_a', password='pass')
        self.assertTrue(user_login)

        response = c.get(reverse('all_posts'))
        self.assertEqual(response.status_code, 200)

    def test_can_access_when_not_logged_in(self):
        response = self.client.get(reverse('all_posts'), follow=True)

        self.assertEqual(response.status_code, 200)

    def test_all_posts_view_context(self):
        c = Client()
        user_login = c.login(username='user_a', password='pass')
        self.assertTrue(user_login)

        response = c.get(reverse('all_posts'))
        pg_obj = response.context['page_obj']
        self.assertEqual(response.context['pg_title'], 'All Posts')

        # Checks if only "Published" posts are in queryset
        self.assertEqual(pg_obj.paginator.count, 15)


# class BookmarkPostViewTests(TestCase):

#     def setUp(self):
#         user_a = User(username="user_a", email="a@x.com")
#         user_a.set_password('pass')
#         user_a.save()

#         category_a = PostCategory.objects.create(name="category_a")
#         channel = SlackChannel.objects.create(
#             name="#test", slack_channel_id="ABCDE")
#         course = Course.objects.create(name="A1")

#         post = Post(title="post title")
#         post.summary = "post summary"
#         post.slug = "post-title"
#         post.body = 'body'
#         post.slack_channel = channel
#         post.course = course
#         post.author = user_a.userprofile
#         post.category = category_a
#         post.status = "Published"
#         post.save()

#     def test_anon_user_redirected(self):
#         response = self.client.get('/posts/bookmark/1')
#         self.assertRedirects(
#             response, '/accounts/login/?next=/bookmark/1/', status_code=301,
#             target_status_code=200, fetch_redirect_response=True)
