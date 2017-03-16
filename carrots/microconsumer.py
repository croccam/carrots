# !/usr/bin/env python

from carrots import Microclient
from carrots import apply


class Microconsumer(Microclient):
    def __init__(self, uri, exchange, qin, process, routing=None):
        super().__init__(uri, exchange, qin=qin, process=process, routing=routing)

    def declare(self, x):
        self.channel.queue_bind(self.bind, exchange=self.exchange, queue=self.qin, routing_key=self.routing)

    def eat_carrot(self, *args):
        apply(self.process, *args)

    def receive(self):
        self.start()