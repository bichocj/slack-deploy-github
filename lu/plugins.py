import re
import subprocess

import subprocess
from slackbot.bot import listen_to
from slackbot.bot import respond_to

from lu.config import BASE_DIR, ENV


@respond_to('hi', re.IGNORECASE)
def hi(message):
    message.reply('hi!')
    message.react('+1')


@respond_to('help', re.IGNORECASE)
def help(message):
    try:
        message.reply('- If you write me "deploy", I going to do : ')

        with open('lu/bash_commands.sh', "r") as f:
            for line in f:
                message.reply("    $ " + line.replace('echo ', ''))

        message.reply('- If you write me "exec your_command", I going : ')
        message.reply('    $ cd ' + BASE_DIR)
        message.reply('    $ ' + ENV)
        message.reply('    $ your_command')
    except Exception as e:
        message.reply(e)


@respond_to('deploy', re.IGNORECASE)
def deploy(message):
    message.reply('ok!, I\'m on that ..')
    try:
        p = subprocess.Popen(['./lu/bash_commands.sh'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        text = ''
        for line in p.stdout.readlines():
            line.decode("utf-8")
            message.reply(text)
    except Exception as e:
        message.reply(e)


@respond_to('exec (.*)')
def exec_command(message, something):
    try:
        task = 'cd ' + ENV + ' &'
        task += 'cd ' + BASE_DIR + ' &'
        task += something

        p = subprocess.Popen(task, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        text = ''
        for line in p.stdout.readlines():
            text = line.decode("utf-8")
            message.reply(text)
    except Exception as e:
        message.reply(e)
