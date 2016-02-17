from sleekxmpp import ClientXMPP


class SendMsgBot(ClientXMPP):

    def __init__(self, jid, password):
        super(SendMsgBot, self).__init__(jid, password)
        self.add_event_handler('session_start', self.start)

    def start(self, event):
        self.send_presence()
        self.get_roster()


if __name__ == '__main__':
    xmpp = SendMsgBot('user_2@example.com', '1234')
    xmpp.register_plugin('xep_0313')
    xep0313 = xmpp['xep_0313']
    xmpp.connect(("192.168.99.100", 5222))
    xmpp.process()
    messages = xep0313.retrieve(jid="user_2@example.com")
    messages.getStanzaValues()
