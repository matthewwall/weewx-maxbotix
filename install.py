# $Id: install.py 1563 2016-10-25 15:11:37Z mwall $
# installer for Maxbotix
# Copyright 2015 Matthew Wall

from setup import ExtensionInstaller

def loader():
    return MaxbotixInstaller()

class MaxbotixInstaller(ExtensionInstaller):
    def __init__(self):
        super(MaxbotixInstaller, self).__init__(
            version="0.5",
            name='maxbotix',
            description='driver for maxbotix range-finding sensors',
            author="Matthew Wall",
            author_email="mwall@users.sourceforge.net",
            config={
                'Maxbotix': {
                    'driver': 'user.maxbotix',
                    'port': '/dev/ttyUSB0'}},
            files=[('bin/user', ['bin/user/maxbotix.py'])]
            )
