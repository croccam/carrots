from carrots import Microworker

rabbit_uri = 'amqp://rabbitmq:rabbitmq@localhost:5672/%2F'

def my_f(data):
    print('Processing in worker')
    print(data)
    return data

mw = Microworker(rabbit_uri,
                  '',
                  'example.tasks',
                  'example.results',
                  my_f)

mw.work()