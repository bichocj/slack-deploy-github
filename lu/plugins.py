import re
import subprocess

import subprocess
from slackbot.bot import listen_to
from slackbot.bot import respond_to

from lu.config import BASE_DIR, ENV_DIR


@respond_to('hi', re.IGNORECASE)
def hi(message):
    message.react('+1')
    message.reply('hi!')


@respond_to('help', re.IGNORECASE)
def help(message):
    try:
        message.reply('- If you write me "deploy", I going to do : ')

        with open('lu/bash_commands.sh', "r") as f:
            for line in f:
                message.reply("_    $ " + line.replace('echo ', ''))

        message.reply('- If you write me "exec your_command", I going : ')
        message.reply('_    $ . ' + ENV_DIR)
        message.reply('_    $ cd ' + BASE_DIR)
        message.reply('_    $ your_command')
    except Exception as e:
        message.reply(e)


@respond_to('deploy', re.IGNORECASE)
def deploy(message):
    message.reply('ok!, I\'m on that ..')
    try:
        with open('lu/bash_commands.sh', "r") as f:
            for line in f:
                task = '. ' + ENV_DIR + ' ; cd ' + BASE_DIR + ' ; ' + line

                message.reply('_    $ '+task)
                p = subprocess.Popen([task], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                for line in p.stdout.readlines():
                    message.reply('_        $ '+line.decode("utf-8"))

    except Exception as e:
        message.reply(e)


@respond_to('exec (.*)')
def exec_command(message, something):
    try:
        task = '. ' + ENV_DIR + ' ; cd ' + BASE_DIR + ' ; ' + something

        p = subprocess.Popen(task, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        text = ''
        for line in p.stdout.readlines():
            text = line.decode("utf-8")
            message.reply(text)
    except Exception as e:
        message.reply(e)
