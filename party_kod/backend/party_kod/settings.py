# party_kod/settings.py

INSTALLED_APPS = [
    ...
    'channels',
    'chat',
]

ASGI_APPLICATION = 'party_kod.asgi.application'

# Настройки Redis (если используете Redis)
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}
