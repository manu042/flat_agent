import os
from tools.settings import settings

log_dir_path = os.path.dirname(settings.LOG_FILE_PATH)
if not os.path.exists(log_dir_path):
    os.makedirs(log_dir_path)

LOG_CONFIG_DICT = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'default': {'format': '%(asctime)s - %(levelname)s - %(message)s', 'datefmt': '%Y-%m-%d %H:%M:%S'},
    },

    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'stream': 'ext://sys.stdout'
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'default',
            'filename': settings.LOG_FILE_PATH,
            'maxBytes': 1 * 1024 * 1000,  # 1 MB
            'backupCount': 5
        },
    },

    'loggers': {
        'default': {
            'level': 'DEBUG',
            'handlers': ['console', 'file']
        },
    },
}
