from django.contrib.auth.models import User
from django.test import TestCase
from .models import UserProfile
from courses.models import Course
from slack.models import SlackChannel
from posts.models import PostCategory, Post
import datetime


class UserProfileTestCase(TestCase):
    def setUp(self):
        user_a = User(username="testUsername", email="test@email.com")
        user_a.set_password('testing321')
        user_a.save()

    def test_userprofile_created_with_new_user(self):
        user_a = User.objects.get(pk=1)
        profile = UserProfile.objects.get(pk=1)
        self.assertEqual(profile.user, user_a)
    
    def test_userprofile_bio_blank_by_default(self):
        profile = UserProfile.objects.get(pk=1)
        self.assertIsNone(profile.bio)

    def test_set_userprofile_bio_value(self):
        profile = UserProfile.objects.get(pk=1)
        profile.bio = 'Test bio'
        self.assertEqual(profile.bio, 'Test bio')

    def test_userprofile_is_admin_value_set_to_false_by_default(self):
        profile = UserProfile.objects.get(pk=1)
        self.assertFalse(profile.is_admin)

    def test_set_userprofile_is_admin_value(self):
        profile = UserProfile.objects.get(pk=1)
        profile.is_admin = True
        self.assertTrue(profile.is_admin)

    def test_userprofile_is_mod_value_set_to_false_by_default(self):
        profile = UserProfile.objects.get(pk=1)
        self.assertFalse(profile.is_mod)

    def test_set_userprofile_is_mod_value(self):
        profile = UserProfile.objects.get(pk=1)
        profile.is_mod = True
        self.assertTrue(profile.is_mod)

    def test_userprofile_is_staff_value_set_to_false_by_default(self):
        profile = UserProfile.objects.get(pk=1)
        self.assertFalse(profile.is_staff)

    def test_set_userprofile_is_staff_value(self):
        profile = UserProfile.objects.get(pk=1)
        profile.is_staff = True
        self.assertTrue(profile.is_staff)

    def test_userprofile_date_joined(self):
        profile = UserProfile.objects.get(pk=1)
        self.assertEqual(profile.date_joined, datetime.date.today())

    def test_userprofile_linkedin_blank_by_default(self):
        profile = UserProfile.objects.get(pk=1)
        self.assertIsNone(profile.linkedin)

    def test_set_userprofile_linkedin_value(self):
        profile = UserProfile.objects.get(pk=1)
        profile.linkedin = 'http://linkedin.com/in/test/'
        self.assertEqual(profile.linkedin, 'http://linkedin.com/in/test/')

    def test_userprofile_github_blank_by_default(self):
        profile = UserProfile.objects.get(pk=1)
        self.assertIsNone(profile.github)

    def test_set_userprofile_github_value(self):
        profile = UserProfile.objects.get(pk=1)
        profile.github = 'https://github.com/test'
        self.assertEqual(profile.github, 'https://github.com/test')

    def test_userprofile_dunder_string_with_defaults(self):
        profile = UserProfile.objects.get(pk=1)
        today = datetime.date.today()
        self.assertEqual(
            str(profile), f"testUsername | {today}"
        )

    def test_userprofile_dunder_string_with_admin_and_mod_true(self):
        profile = UserProfile.objects.get(pk=1)
        profile.is_admin = True
        profile.is_mod = True
        profile.save()
        today = datetime.date.today()
        self.assertEqual(
            str(profile), f"testUsername *admin | {today}"
        )

    def test_userprofile_dunder_string_with_admin_false_and_mod_true(self):
        profile = UserProfile.objects.get(pk=1)
        profile.is_mod = True
        profile.save()
        today = datetime.date.today()
        self.assertEqual(
            str(profile), f"testUsername *mod | {today}"
        )

    def test_default_profile_pic_created(self):
        profile = UserProfile.objects.get(pk=1)
        expected = '/media/images/profiles/default-profile-pic.png'
        self.assertEqual(profile.profile_pic.url, expected)


class GetAuthorNameMethodTestCase(TestCase):
    def setUp(self):
        user = User(username="testUsername", email="test@email.com")
        user.set_password('testing321')
        user.save()

    def test_first_name_does_not_exist(self):
        user = User.objects.get(pk=1)
        self.assertEqual(user.first_name, '')
        self.assertEqual(user.last_name, '')

    def test_get_author_name_when_only_username_exists(self):
        user = User.objects.get(pk=1)
        expected = "testUsername"
        result = user.userprofile.get_author_name()
        self.assertEqual(result, expected)

    def test_get_author_name_when_only_first_name_exists(self):
        user = User.objects.get(pk=1)
        user.first_name = 'Arthur'
        user.save()

        expected = "testUsername"
        result = user.userprofile.get_author_name()
        self.assertEqual(result, expected)

    def test_get_author_name_when_first_and_last_names_exist(self):
        user = User.objects.get(pk=1)
        user.first_name = 'Arthur'
        user.last_name = 'Dent'
        user.save()

        expected = "Arthur Dent"
        result = user.userprofile.get_author_name()
        self.assertEqual(result, expected)


def create_num_posts_for_author(num):
    """
    Generate specified number of posts in the test database
    for a single author. To test kudos badge method of UserProfile
    """
    user = User(username="testUsername", email="test@email.com")
    user.set_password('testing321')
    user.save()

    category = PostCategory(name='test category')
    category.save()

    # Create slack channel
    channel = SlackChannel.objects.create(
        name="#test", slack_channel_id="ABCDE")

    # create course
    course = Course.objects.create(
        name="A1")

    for i in range(num):
        post = Post(title=f"post title {i}")
        post.summary = f"post summary {i}"
        post.slug = f"post-title-{i}"
        post.body = 'body'
        post.author = user.userprofile
        post.status = "Published"
        post.category = category
        post.slack_channel = channel
        post.course = course
        post.save()


class CreateNumPostsForAuthorTestCase(TestCase):
    def test_no_posts_created(self):
        create_num_posts_for_author(0)
        posts_qs_count = Post.objects.all().count()
        self.assertEqual(posts_qs_count, 0)

    def test_five_posts_created(self):
        create_num_posts_for_author(5)
        posts_qs_count = Post.objects.all().count()
        self.assertEqual(posts_qs_count, 5)

    def test_author_instance_applied_to_created_posts(self):
        create_num_posts_for_author(1)
        post = Post.objects.get(pk=1)
        date = datetime.date.today()
        self.assertEqual(str(post.author), f'testUsername | {date}')


class KudosBadgeTestCase(TestCase):
    def test_kudos_badge_is_invisible_when_no_posts_by_author(self):
        create_num_posts_for_author(0)
        user = User.objects.get(pk=1)
        badge = user.userprofile.kudos_badge()
        self.assertEqual(badge, 'invisible')

    def test_kudos_badge_is_invisible_when_2_posts_by_author(self):
        create_num_posts_for_author(2)
        user = User.objects.get(pk=1)
        badge = user.userprofile.kudos_badge()
        self.assertEqual(badge, 'invisible')

    def test_kudos_badge_is_bronze_when_3_posts_by_author(self):
        create_num_posts_for_author(3)
        user = User.objects.get(pk=1)
        badge = user.userprofile.kudos_badge()
        self.assertEqual(badge, 'kudos-badge-bronze')

    def test_kudos_badge_is_silver_when_8_posts_by_author(self):
        create_num_posts_for_author(8)
        user = User.objects.get(pk=1)
        badge = user.userprofile.kudos_badge()
        self.assertEqual(badge, 'kudos-badge-silver')

    def test_kudos_badge_is_gold_when_15_posts_by_author(self):
        create_num_posts_for_author(15)
        user = User.objects.get(pk=1)
        badge = user.userprofile.kudos_badge()
        self.assertEqual(badge, 'kudos-badge-gold')

    def test_kudos_badge_is_gold_when_25_posts_by_author(self):
        create_num_posts_for_author(25)
        user = User.objects.get(pk=1)
        badge = user.userprofile.kudos_badge()
        self.assertEqual(badge, 'kudos-badge-gold')
