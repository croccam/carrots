from carrots import Microclient
from carrots.common.functions import apply

class Microworker(Microclient):
    def __init__(self, uri, exchange, qin, qout, process, init_queues=False):
        super().__init__(uri, exchange, qin=qin, qout=qout, process=process, init_queues=init_queues)

    def eat_carrot(self, *args):
        carrot = apply(self.process, *args)
        self.push_carrot(self.qout, carrot)

    def work(self):
        self.start()
        self.start_loop()