from carrots import Microproducer

rabbit_uri = 'amqp://rabbitmq:rabbitmq@localhost:5672/%2F'

mp = Microproducer(rabbit_uri,'','example.tasks')
ids = [{'id': i} for i in range(0,100)]

mp.send(ids)
