import json

def apply(process, channel, method, properties, data):
    channel.basic_ack(delivery_tag=method.delivery_tag)
    response = process(data)
    return response
