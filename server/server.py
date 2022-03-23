class Server(object):
    def __init__(self):
        self.clients = {}
        self.host = None
        self.db = None
        self.game = None
