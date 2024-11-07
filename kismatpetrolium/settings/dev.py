from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 't-42lhvu*qche(*jsy!3d24+un1g1m%y@14&!pb=ee8=n0howq'

# SECURITY WARNING: define the correct hosts in production!
<<<<<<< HEAD
ALLOWED_HOSTS = ['148.66.128.35','kismatpetroleum.com','www.kismatpetroleum.com'] 
=======
ALLOWED_HOSTS = ['65.1.92.28'] 
>>>>>>> 8686302645cb9f0958b46b6ae438cdb32f283527
#ALLOWED_HOSTS = []
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
