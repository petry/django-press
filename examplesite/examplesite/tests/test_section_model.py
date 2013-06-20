from django.test import TestCase
from model_mommy import mommy
from press.models import Section


class SectionModelTestCase(TestCase):
    def assert_field_in(self, field_name, model):
        self.assertIn(field_name, model._meta.get_all_field_names())

    def test_should_have_name(self):
        self.assert_field_in('name', Section)

    def test_should_output_user_name_on_model(self):
        section = mommy.make(Section)
        self.assertEqual(str(section), section.name)
