import datetime
from users.models import UserProfile
from django.contrib.auth.models import User
from django.test import TestCase
from .models import PostTag, PostCategory, PostFlag, Post


class PostTagTestCase(TestCase):

    def setUp(self):
        tag = PostTag(name='testTag')
        tag.save()

    def test_tag_created(self):
        tag_count = PostTag.objects.all().count()
        self.assertEqual(tag_count, 1)

    def test_tag_has_correct_name(self):
        tag = PostTag.objects.get(pk=1)
        self.assertEqual(tag.name, 'testTag')


class PostCategoryTestCase(TestCase):

    def setUp(self):
        category = PostCategory(name='Test Category')
        category.save()

    def test_category_created(self):
        category_count = PostCategory.objects.all().count()
        self.assertEqual(category_count, 1)

    def test_category_has_correct_name(self):
        category = PostCategory.objects.get(pk=1)
        self.assertEqual(category.name, 'Test Category')


class PostFlagTestCase(TestCase):
    def setUp(self):
        # Create User instance for flag
        user_a = User(username="testUsername", email="test@email.com")
        user_a.set_password('testing321')
        user_a.save()

        # Create flag
        flag = PostFlag(flagger=user_a)
        flag.save()

    def test_flag_has_correct_user_value(self):
        flag = PostFlag.objects.get(pk=1)
        flagger = User.objects.get(pk=1)
        self.assertEqual(flag.flagger, flagger)

    def test_flag_has_correct_default_reason(self):
        flag = PostFlag.objects.get(pk=1)
        self.assertEqual(flag.reason, 'Innappropriate content')

    def test_set_flag_reason(self):
        flag = PostFlag.objects.get(pk=1)
        flag.reason = 'Outdated content'
        flag.save()
        self.assertEqual(flag.reason, 'Outdated content')

    def test_flag_dunder(self):
        flag = PostFlag.objects.get(pk=1)
        self.assertEqual(
            str(flag), 'flag by testUsername | Innappropriate content')


class PostTestCase(TestCase):
    def setUp(self):
        user = User(username="testUsername", email="test@email.com")
        user.set_password('testing321')
        user.save()

        category = PostCategory(name='test category')
        category.save()

        post = Post(title="post title")
        post.summary = "post summary"
        post.slug = "post-title"
        post.body = 'body'
        post.author = user.userprofile
        post.category = category
        post.save()

    def test_post_exists(self):
        post = Post.objects.get(pk=1)
        user = User.objects.get(pk=1)
        self.assertIsNotNone(post)
        self.assertEqual(post.title, "post title")
        self.assertEqual(post.summary, "post summary")
        self.assertEqual(post.body, "body")
        self.assertIsInstance(post.author, UserProfile)
        self.assertEqual(post.author, user.userprofile)
        self.assertIsInstance(post.category, PostCategory)
        self.assertEqual(str(post.category), 'test category')

    def test_post_default_values(self):
        post = Post.objects.get(pk=1)
        self.assertEqual(post.status, "Submitted")
        self.assertIsNone(post.updated_on)
        self.assertIsNone(post.mod_message)
        self.assertIsNone(post.moderator)
        self.assertIsNone(post.flag)
        self.assertIsNone(post.editors_note)
        self.assertEqual(str(post.image_1), '')
        self.assertEqual(str(post.image_2), '')
        self.assertEqual(str(post.image_3), '')
        self.assertEqual(str(post.image_4), '')

    def test_update_default_fields(self):
        mod = User.objects.create(username="mod", email="mod@email.com")
        mod.set_password('testing321')
        mod.save()

        flagger = User.objects.create(
            username="flagger", email="flagger@email.com")
        flagger.set_password('testing321')
        flagger.save()

        flag = PostFlag(flagger=flagger)
        flag.save()

        post = Post.objects.get(pk=1)
        post.status = "Published"
        post.mod_message = 'test mod message'
        post.moderator = mod
        post.flag = flag
        post.editors_note = 'test editors note'
        post.save()

        self.assertEqual(post.status, "Published")
        self.assertEqual(post.mod_message, 'test mod message')
        self.assertEqual(post.moderator.username, 'mod')
        self.assertIsInstance(post.moderator, User)
        self.assertIsInstance(post.flag, PostFlag)
        self.assertEqual(post.editors_note, 'test editors note')

    def test_post_likes(self):
        user_a = User(username="user_a", email="a@email.com")
        user_a.set_password("test321")
        user_a.save()

        user_b = User(username="user_b", email="b@email.com")
        user_b.set_password("test321")
        user_b.save()

        post = Post.objects.get(pk=1)
        post.likes.add(user_a)
        post.likes.add(user_b)
        post.save()

        self.assertEqual(post.total_likes(), 2)

    def test_post_dunder_string(self):
        post = Post.objects.get(pk=1)
        self.assertEqual(str(post), 'post title')

    def test_get_absolute_url(self):
        post = Post.objects.get(pk=1)
        url = post.get_absolute_url()
        self.assertEqual(url, '/posts/post/1/post-title/')
