from sleekxmpp import ClientXMPP


class EchoBot(ClientXMPP):

    def __init__(self, jid, password):
        ClientXMPP.__init__(self, jid, password)
        self.add_event_handler("session_start", self.session_start)
        self.add_event_handler("message", self.message)
        self.register_plugin('xep_0077')
        self['xep_0077'].force_registration = True

    def session_start(self, event):
        self.send_presence()
        self.get_roster()

    def message(self, msg):
        if msg['type'] in ('chat', 'normal'):
            self.last_msg = msg
            msg.reply("Thanks for sending\n%(body)s" % msg).send()

if __name__ == '__main__':
    xmpp = EchoBot('user_1@example.com', '1234')
    xmpp.connect(("192.168.99.100", 5222))
    xmpp.process(block=True)
