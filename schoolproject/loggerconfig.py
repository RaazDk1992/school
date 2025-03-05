import os
from pathlib import Path
#Logger BASE_URL
REQUEST_BASE_URL="http://localhost:8000/"

BASE_DIR = Path(__file__).resolve().parent.parent


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/django.log'),
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.request': {  # Logs requests and responses
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django.security': {  # Logs security-related events
            'handlers': ['file'],
            'level': 'WARNING',
            'propagate': False,
        },
    },
}
