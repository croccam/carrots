# !/usr/bin/env python
import json

from .common.microclient import Microclient


class Microproducer(Microclient):
    def __init__(self, uri, exchange, qout):
        super().__init__(uri, exchange, qout=qout)
        self.data = None

    def channel_open(self, channel):
        self.channel = channel
        self.channel.queue_declare(self.declare, queue=self.qout)

    def declare(self, x):
        self.channel.queue_bind(self.bind, exchange=self.exchange, queue=self.qout)

    def bind(self, x):
        for item in self.data:
            body = json.dumps(item)
            self.push_carrot(self.qout, body)
        self.connection.close()
        self.connection.ioloop.start()

    def send(self, data):
        self.data = data
        self.start()
