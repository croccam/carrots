# !/usr/bin/env python
import pika


class Microclient():
    def __init__(self, uri, exchange, qin=None, qout=None, process=lambda x: x, routing=None):
        self.uri = uri
        self.exchange = exchange
        self.qin = qin
        self.qout = qout
        self.process = process
        self.routing = routing
        self.connection = None
        self.channel = None
        if self.exchange == '':
            self.declare = self.bind

    def connection_open(self, connection):
        self.connection = connection
        self.connection.channel(self.channel_open)

    def channel_open(self, channel):
        self.channel = channel
        channel.queue_declare(self.declare, queue=self.qin)

    def declare(self, x):
        self.channel.queue_bind(self.bind, exchange=self.exchange, queue=self.qin)

    def bind(self, x):
        self.channel.basic_consume(self.eat_carrot, self.qin)

    def eat_carrot(self, channel, method, properties, body):
        pass

    def push_carrot(self, queue, payload):
        self.channel.basic_publish(self.exchange,
                                   queue,
                                   payload,
                                   pika.BasicProperties(content_type='text/json',
                                                        delivery_mode=1))

    def start(self):
        parameters = pika.URLParameters(self.uri)
        self.connection = pika.SelectConnection(parameters=parameters,
                                                on_open_callback=self.connection_open)

    def start_loop(self):
        try:
            self.connection.ioloop.start()
        except KeyboardInterrupt:
            self.connection.close()
            self.connection.ioloop.start()