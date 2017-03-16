import json

def apply(process, channel, method, properties, body):
    channel.basic_ack(delivery_tag=method.delivery_tag)
    data = json.loads(body)
    print('Received:')
    print(data)
    response = json.dumps(process(data))
    print('\t\tSent:')
    print(response)
    return response
