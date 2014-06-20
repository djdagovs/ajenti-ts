import ts3
from ajenti.api import *
from ajenti.api.http import *
from ajenti.plugins.dashboard.api import ConfigurableWidget
from ajenti.ui import on

@plugin
class TempWidget (ConfigurableWidget):
    name = 'Teamspeak'
    icon = 'leaf'

    def on_prepare(self):
        self.append(self.ui.inflate('ajenti-ts:widget'))

    def on_start(self):
        server = ts3.TS3Server(self.config['host'], self.config['port'])
        server.login(str(self.config['username']), str(self.config['password']))
        server.use(1)
        clientlist = server.clientlist()
        # -1 because the serverquery user gets counted
        clientlistLength = len(clientlist.values()) - 1
        self.find('value').text = "Users: " + str(clientlistLength)

    def create_config(self):
        return {'host': '127.0.0.1', 'port': 10011, 'username': '', 'password': ''}

    def on_config_start(self):
        self.find('host').value = self.config['host'] if 'host' in self.config else '127.0.0.1'
        self.find('port').value = self.config['port'] if 'port' in self.config else 1011
        self.find('username').value = self.config['username'] if 'username' in self.config else ''
        self.find('password').value = self.config['password'] if 'password' in self.config else ''

    def on_config_save(self):
        self.config['host'] = self.dialog.find('host').value
        self.config['port'] = self.dialog.find('port').value
        self.config['username'] = self.dialog.find('username').value
        self.config['password'] = self.dialog.find('password').value
