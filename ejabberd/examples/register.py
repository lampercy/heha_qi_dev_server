import logging

import sleekxmpp
from sleekxmpp.exceptions import IqError, IqTimeout


class RegisterBot(sleekxmpp.ClientXMPP):

    def __init__(self, jid, password):
        sleekxmpp.ClientXMPP.__init__(self, jid, password)
        self.register_plugin('xep_0077')
        self.register_plugin('xep_0030')  # Service Discovery
        self.register_plugin('xep_0004')  # Data forms
        self.register_plugin('xep_0066')  # Out-of-band Data

        self['xep_0077'].force_registration = True
        self.add_event_handler("session_start", self.start, threaded=True)
        self.add_event_handler("register", self.register, threaded=True)

    def start(self, event):
        self.send_presence()
        self.get_roster()
        self.disconnect()

    def register(self, iq):
        resp = self.Iq()
        resp['type'] = 'set'
        resp['register']['username'] = self.boundjid.user
        resp['register']['password'] = self.password

        try:
            resp.send(now=True)
            logging.info("Account created for %s!" % self.boundjid)
        except IqError as e:
            logging.error(
                "Could not register account: %s" % e.iq['error']['text'])
            self.disconnect()
        except IqTimeout:
            logging.error("No response from server.")
            self.disconnect()

if __name__ == '__main__':
    xmpp = RegisterBot('user_2@example.com', '1234')
    if xmpp.connect(("192.168.99.100", 5222)):
        xmpp.process(block=True)
