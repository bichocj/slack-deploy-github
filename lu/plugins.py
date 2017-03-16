import re
import subprocess

from slackbot.bot import listen_to
from slackbot.bot import respond_to


@respond_to('hi', re.IGNORECASE)
def hi(message):
    message.reply('hi-me -> jaime XD')
    message.react('+1')


@respond_to('help', re.IGNORECASE)
def help(message):
    message.reply('I going to do: ')
    with open('bash_commands.sh', "r") as f:
        for line in f:
            message.reply("$ " + line)

    message.reply("write 'deploy' if you want I run the script")
    message.reply("also you can give me your own command using 'exec (.*)'")


@respond_to('deploy', re.IGNORECASE)
def deploy(message):
    message.reply('ok!, I\'m beginning with de deploy')

    with open('bash_commands.sh', "r") as f:
        for line in f:
            p = subprocess.Popen(line, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            text = ''
            for line in p.stdout.readlines():
                text += line.decode("utf-8")
            message.reply(text)
    f.close()


@respond_to('exec (.*)')
def exec_command(message, something):
    p = subprocess.Popen(something, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    text = ''
    for line in p.stdout.readlines():
        text += line.decode("utf-8")
    message.reply(text)
