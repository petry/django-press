from django.contrib.auth.models import User
from django.test import TestCase
from model_mommy import mommy
from press.models import Author


class AuthorModelTestCase(TestCase):
    def assert_field_in(self, field_name, model):
        self.assertIn(field_name, model._meta.get_all_field_names())

    def test_should_have_about(self):
        self.assert_field_in('about', Author)

    def test_should_have_position(self):
        self.assert_field_in('position', Author)

    def test_should_have_photo(self):
        self.assert_field_in('photo', Author)

    def test_should_have_user(self):
        self.assert_field_in('user', Author)

    def test_should_output_user_name_on_model(self):
        user = mommy.make(User)
        article = mommy.make(Author, user=user)
        self.assertEqual(str(article), user.get_full_name())
