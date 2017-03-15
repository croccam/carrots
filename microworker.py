# !/usr/bin/env python
import pika
import json


class Microworker(object):
    def __init__(self, uri, exchange, qin, qout, process):
        self.uri = uri
        self.exchange = exchange
        self.qin = qin
        self.qout = qout
        self.process = process
        self.connection = None
        self.channel = None

    def connection_open(self, connection):
        self.connection = connection
        self.connection.channel(self.channel_open)

    def channel_open(self, channel):
        self.channel = channel
        channel.queue_declare(self.declare, queue=self.qin)

    def declare(self, x):
        self.channel.queue_bind(self.bind, exchange=self.exchange, queue=self.qin)

    def bind(self, x):
        self.channel.basic_consume(self.unmarshall, self.qin)

    def unmarshall(self, channel, method, properties, body):
        channel.basic_ack(delivery_tag=method.delivery_tag)
        data = json.loads(body)
        print('Received:')
        print(data)
        response = self.process(data)
        print('Sent:')
        response = json.dumps(response)
        print(response)
        self.channel.basic_publish(self.exchange,
                              self.qout,
                              response,
                              pika.BasicProperties(content_type='text/json',
                                                   delivery_mode=1))
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
