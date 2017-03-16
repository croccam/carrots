# !/usr/bin/env python
import pika
import json

class Microproducer(object):
    def __init__(self, uri, exchange, qout):
        self.uri = uri
        self.exchange = exchange
        self.qout = qout
        self.data = None
        self.connection = None
        self.channel = None

    def connection_open(self, connection):
        self.connection = connection
        self.connection.channel(self.channel_open)

    def channel_open(self, channel):
        self.channel = channel
        self.channel.queue_declare(self.declare, queue=self.qout)

    def declare(self, x):
        self.channel.queue_bind(self.bind, exchange=self.exchange, queue=self.qout)

    def bind(self, x):
        for item in self.data:
            body = json.dumps(item)
            self.channel.basic_publish(self.exchange,
                                       self.qout,
                                       body,
                                       pika.BasicProperties(content_type='text/json',
                                                            delivery_mode=1))
            print('Task sent:')
            print(body)
        self.connection.close()
        self.connection.ioloop.start()

    def send(self, data):
        self.data = data
        parameters = pika.URLParameters(self.uri)
        self.connection = pika.SelectConnection(parameters=parameters,
                                                on_open_callback=self.connection_open)
        try:
            self.connection.ioloop.start()
        except:
            print('Some error ocurred')
