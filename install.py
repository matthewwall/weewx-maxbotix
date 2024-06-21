# installer for Maxbotix
# Copyright 2015 Matthew Wall
# Distributed under the terms of the GNU Public License (GPLv3)

from weecfg.extension import ExtensionInstaller

def loader():
    return MaxbotixInstaller()

class MaxbotixInstaller(ExtensionInstaller):
    def __init__(self):
        super(MaxbotixInstaller, self).__init__(
            version="0.6",
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
