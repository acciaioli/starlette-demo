import logging.config

FORMATTERS = {
    "short": {"format": "%(levelname)s %(name)s: %(message)s"},
    "standard": {"format": "%(asctime)s %(levelname)s %(name)s: %(message)s", "datefmt": "%d %H:%M:%S"},
}

DEV_HANDLERS = {
    "console": {"level": "DEBUG", "formatter": "short", "class": "logging.StreamHandler"},
    "debug": {"level": "DEBUG", "formatter": "standard", "class": "logging.FileHandler", "filename": "debug.log"},
}

PROD_HANDLERS = {
    "console": {"level": "INFO", "formatter": "short", "class": "logging.StreamHandler"},
    "production": {
        "level": "WARNING",
        "class": "logging.handlers.TimedRotatingFileHandler",
        "filename": "app.log",
        "formatter": "standard",
        "when": "midnight",
        "backupCount": 14,
    },
}

DEV_LOGGERS = {"": {"handlers": ["console"], "level": "INFO"}, "app": {"handlers": ["debug"], "level": "DEBUG"}}

PROD_LOGGERS = {
    "": {"handlers": ["console"], "level": "INFO"},
    "app.tasks": {"handlers": ["console", "production"], "level": "WARNING"},
}


def configure_logging(env: str) -> None:
    handlers, loggers = {
        "dev": (DEV_HANDLERS, DEV_LOGGERS),
        "test": (PROD_HANDLERS, PROD_LOGGERS),
        "prod": (PROD_HANDLERS, PROD_LOGGERS),
    }[env]

    logging.config.dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": FORMATTERS,
            "handlers": handlers,
            "loggers": loggers,
        }
    )
