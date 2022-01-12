from .settings import DEBUG

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'a0587819_hram_alekseevskii',
            'USER': 'a0587819_hram_alekseevskii_user',
            'PASSWORD': 'u1IPdI9q',
            'HOST': 'igorkhaylov.uz',
            'PORT': '3306',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'a0587819_hram_alekseevskii',
            'USER': 'a0587819_hram_alekseevskii_user',
            'PASSWORD': 'u1IPdI9q',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'totpravka@gmail.com'
EMAIL_HOST_PASSWORD = 'q1w2e3r4*'
EMAIL_USE_SSL = True
