import json

def apply(process, channel, method, properties, body):
    channel.basic_ack(delivery_tag=method.delivery_tag)
    data = json.loads(body)
    response = json.dumps(process(data))
    return response
