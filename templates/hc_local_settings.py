import os

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'WARNING',
    },
}

DEBUG = False
# FIXME: Move this somewhere else...
SECRET_KEY = "insertedbozoscrop'sbinderyremembrancesballadeglantinessimplestenduingprohibitgrungierasteroidroundinghorriblyginkgo'sholler'sforeclosureexcisingmansardsOlivia's"
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "/mnt/backup-drive/rpi-data/hc.sqlite",
    }
}
SITE_NAME = "Raspberry Pi HealthChecks Server"
