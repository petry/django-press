from django.conf import settings
from myapp.tests import settings_for_test

settings.configure(settings_for_test)

from django.core.management import call_command
call_command('syncdb', interactive=False)
