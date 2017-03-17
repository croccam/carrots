from carrots import Microproducer
import datetime
rabbit_uri = 'amqp://rabbitmq:rabbitmq@localhost:5672/%2F'

mp = Microproducer(rabbit_uri,'','example.tasks')
ids = [{'id': i} for i in range(0,100000)]

before = datetime.datetime.now()
mp.send(ids)
print((datetime.datetime.now()-before).total_seconds())