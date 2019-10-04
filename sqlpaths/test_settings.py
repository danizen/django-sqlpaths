import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = True

SECRET_KEY = '7(f3d$@w#=pl54851o)3hzw49n3r8kmmr@ywntx(mcvel%^-@_'

INSTALLED_APPS = [
	'django.contrib.contenttypes',
	'sqlpaths',
]

DATABASES = {
	'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
	}
}

ROOT_URLCONF = __name__

# urls.py content
urlpatterns = []
