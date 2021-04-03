import slack
import time

import parcer
import extensions
import config


def start():
    current = ''
    while True:
        if current != parcer.req():
            s = extensions.Settings('TestSlackBot', 'new', 'Всем привет')
            if s.workspace in config.SLACK_TOKEN.keys():
                client = slack.WebClient(token=config.SLACK_TOKEN[s.workspace])
            else:
                raise extensions.SlackException('Wrong Workspace')

            text = s.text + '\n' + parcer.req()
            client.chat_postMessage(channel='#' + s.channel, text=text)
            current = parcer.req()

        time.sleep(7)

start()


