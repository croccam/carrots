# !/usr/bin/env python
from carrots.common.microclient import Microclient
from carrots.common.functions import apply
import pika

class Microworker(Microclient):
    def __init__(self, uri, exchange, qin, qout, process):
        super().__init__(uri, exchange, qin=qin, qout=qout, process=process)

    def eat_carrot(self, *args):
        carrot = apply(self.process, *args)
        self.push_carrot(self.qout, carrot)

    def work(self):
        self.start()