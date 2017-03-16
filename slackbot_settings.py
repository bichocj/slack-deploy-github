import configparser

config = configparser.ConfigParser()
config.read('config.ini')

# TODO get this token from slack api https://api.slack.com/apps
API_TOKEN = config['BASE'].get('API_TOKEN')

DEFAULT_REPLY = "Sorry but I didn't understand you"

ERRORS_TO = 'bichocj'

PLUGINS = [
    'slackbot.plugins',
    'lu.plugins',
]
