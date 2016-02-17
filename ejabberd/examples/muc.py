import sleekxmpp


class MUCBot(sleekxmpp.ClientXMPP):

    def __init__(self, jid, password, room, nick):
        sleekxmpp.ClientXMPP.__init__(self, jid, password)

        self.register_plugin('xep_0030')  # Service Discovery
        self.register_plugin('xep_0045')  # Multi-User Chat
        self.register_plugin('xep_0199')  # XMPP Ping

        self.room = room
        self.nick = nick
        self.add_event_handler("session_start", self.start)

        self.add_event_handler("groupchat_message", self.muc_message)
        self.add_event_handler("muc::%s::got_online" % self.room,
                               self.muc_online)

    def start(self, event):
        self.get_roster()
        self.send_presence()

    def muc_message(self, msg):
        if msg['mucnick'] != self.nick and self.nick in msg['body']:
            self.send_message(mto=msg['from'].bare,
                              mbody="I heard that, %s." % msg['mucnick'],
                              mtype='groupchat')

    def muc_online(self, presence):
        if presence['muc']['nick'] != self.nick:
            self.send_message(mto=presence['from'].bare,
                              mbody="Hello, %s %s" % (presence['muc']['role'],
                                                      presence['muc']['nick']),
                              mtype='groupchat')

    def joinMUC(self):
        self.plugin['xep_0045'].joinMUC(self.room, self.nick)


if __name__ == '__main__':
    xmpp = MUCBot(
        "user_2@example.com", "1234", "room3@conference.example.com", "room3")
    xmpp.connect(("192.168.99.100", 5222))
    xmpp.joinMUC()
    xmpp.process()
