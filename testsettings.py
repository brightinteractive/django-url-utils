DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
}

INSTALLED_APPS = (
    'url_utils',
)

# Django 1.5 raises an exception if this setting is not present.
# Make this unique, and don't share it with anybody.
SECRET_KEY = '5jdsc!3ig$g3d=1)$n_s7+atnf2zqzaiwt$l%5n)+0-an0x383'
