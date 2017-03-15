# !/usr/bin/env python
import pika
import json


class Microconsumer(object):
    def __init__(self, uri, exchange, qin, process, routing=None):
        self.uri = uri
        self.exchange = exchange
        self.qin = qin
        self.process = process
        self.routing = routing
        self.connection = None
        self.channel = None

    def connection_open(self, connection):
        self.connection = connection
        self.connection.channel(self.channel_open)

    def channel_open(self, channel):
        self.channel = channel
        channel.queue_declare(self.declare, queue=self.qin)

    def declare(self, x):
        self.channel.queue_bind(self.bind, exchange=self.exchange, queue=self.qin, routing_key=self.routing)

    def bind(self, x):
        self.channel.basic_consume(self.unmarshall, self.qin)

    def unmarshall(self, channel, method, properties, body):
        channel.basic_ack(delivery_tag=method.delivery_tag)
        data = json.loads(body)
        print('Received:')
        print(data)
        response = self.process(data)
        print('Sent:')
        print(json.dumps(response))

    def start(self):
        parameters = pika.URLParameters(self.uri)
        self.connection = pika.SelectConnection(parameters=parameters,
                                           on_open_callback=self.connection_open)

        try:
            # Step #2 - Block on the IOLoop
            self.connection.ioloop.start()
        # Catch a Keyboard Interrupt to make sure that the connection is closed cleanly
        except KeyboardInterrupt:
            # Gracefully close the connection
            self.connection.close()
            # Start the IOLoop again so Pika can communicate, it will stop on its own when the connection is closed
            self.connection.ioloop.start()
