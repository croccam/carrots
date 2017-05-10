from carrots import Microclient
from carrots.common.functions import apply

class Microconsumer(Microclient):
    def __init__(self, uri, exchange, qin, process, routing=None, init_queues=False):
        super().__init__(uri, exchange, qin=qin, process=process, routing=routing, init_queues=init_queues)

    def declare(self, x):
        self.channel.queue_bind(self.bind, exchange=self.exchange, queue=self.qin, routing_key=self.routing)

    def eat_carrot(self, *args):
        apply(self.process, *args)

    def receive(self):
        self.start()
        self.start_loop()
