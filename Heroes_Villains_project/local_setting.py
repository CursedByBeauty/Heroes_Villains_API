# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-4dy3jz-%@-rc^38=6@4@6$5er&jjrv$a3q^4ofw&4q)tx)$!b0'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'heroes_villains_database',
        'USER': 'root',
        'PASSWORD': 'Doghotman85!',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
        'autocommit': True
        }
    }
}