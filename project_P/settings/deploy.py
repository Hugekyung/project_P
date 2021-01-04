# 배포용 #
from .base import *

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# reading .env file
environ.Env.read_env(
    env_file=os.path.join(BASE_DIR, '.env')
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*'] # 모든 호스트에 대해서 허용한다.(배포 시에는 다르게 설정해줘야 한다)

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# db 관련 container를 생성할 때 아래 DATABASE의 정보에 맞게 생성해야 한다. 위 주소에서 해당 내용을 가져온다.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': 'password1234',
        'HOST': 'mariadb', # network로 연결해 줄 때 container name을 하나의 도메인으로 본다.
        'PORT': '3306',
    }
}