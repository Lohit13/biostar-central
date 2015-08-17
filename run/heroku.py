# Import all values from the base then override site specific settings.
from biostar3.settings.base import *

# Turn this off during deployment.
DEBUG = True
TEMPLATE_DEBUG = True

# Site administrators. Make sure to override this.
ADMINS = (
    (get_env("BIOSTAR_ADMIN_NAME"), get_env("BIOSTAR_ADMIN_EMAIL")),
)

DEFAULT_FROM_EMAIL = get_env("DEFAULT_FROM_EMAIL")

MANAGERS = ADMINS

# Needs to match the server domain.
SESSION_COOKIE_DOMAIN = get_env("BIOSTAR_HOSTNAME")

ALLOWED_HOSTS = [get_env("BIOSTAR_HOSTNAME")]

# The secret key can be used to log into the admin account!
# Make sure to change it in production.
SECRET_KEY = get_env("SECRET_KEY")

# The database name must be present.
DATABASE_NAME = get_env('DATABASE_NAME')

SITE_ID = 1
SITE_NAME = "Lohit"
SITE_DOMAIN = get_env("BIOSTAR_HOSTNAME")
SITE_SCHEME = "http"
