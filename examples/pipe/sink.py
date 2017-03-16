from carrots import Microconsumer

rabbit_uri = 'amqp://rabbitmq:rabbitmq@localhost:5672/%2F'

def my_f(data):
    print('Data arrived at sink')
    print(data)
    return data

mc = Microconsumer(rabbit_uri,
                   '',
                   'example.results',
                   my_f)

mc.receive()