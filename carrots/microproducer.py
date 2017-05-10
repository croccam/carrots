from carrots import Microclient
import json

class Microproducer(Microclient):
    def __init__(self, uri, exchange, qout, init_queues=False):
        super().__init__(uri, exchange, qout=qout, init_queues=init_queues)
        self.data = None

    def channel_open(self, channel):
        self.channel = channel
        if self.init_queues:
            self.channel.queue_declare(self.declare, queue=self.qout)
        else:
            self.declare(None)

    def declare(self, x):
        self.channel.queue_bind(self.bind, exchange=self.exchange, queue=self.qout)

    def bind(self, *args):
        if isinstance(self.data,list):
            for item in self.data:
                #body = json.dumps(item)
                self.push_carrot(self.qout, item)
        else:
            self.push_carrot(self.qout, self.data)
        self.connection.close()
        self.connection.ioloop.start()

    def send(self, data):
        self.data = data
        self.start()
        self.start_loop()