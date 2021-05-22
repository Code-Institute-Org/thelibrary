from django.contrib.auth.models import User
from django.test import TestCase
from .models import PostTag, PostCategory, PostFlag


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
