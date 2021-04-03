class SlackException(Exception):
    pass


class Settings:
    def __init__(self, workspace, channel, text):
        self.workspace = workspace
        self.channel = channel
        self.text = text
