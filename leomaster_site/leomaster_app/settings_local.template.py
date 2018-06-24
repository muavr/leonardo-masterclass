import os
from django.conf import settings

LEO_TELEGRAM_MODE = 'HTML'
LEO_TELEGRAM_BOT_TOKEN = '<token>'
LEO_TELEGRAM_CHAT_ID = '<chat_id>'
LEO_TASK_LOG_PATH = '../log/task.log'
LEO_TASK_LOG_LEVEL = 'DEBUG'
LEO_PARSER_CONFIG_PATH = os.path.join(settings.BASE_DIR, '../leoparser/parser_config.json')
LEO_RETRY_DELAY = '60'
LEO_UPDATE_PERIOD = '5'
