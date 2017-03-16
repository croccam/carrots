# Description
This library is intended to make the process of building RabbitMQ architectures easier. It uses Pika client under the hood,
and helps to abstract some low-level requirements and reduce the boiler-plate code.
As a side effect, the flexibility of RabbitMQ is lost. I'm working on increasing the capabilities of carrots.

# Usage
The main idea of carrots library is to provide an abstraction to work with RabbitMQ architectures.
In this paradigm, an asynchronous architecture is made of blocks, each one of the blocks being a piece of software on
its own. Blocks communicate through RabbitMQ, but this might get tedious.
Carrots offer three roles to ease the development of such architectures: microproducers, microworkers, and microconsumers.
These three roles can be understood as the entrypoints, middlepoints, and endpoints of a network of blocks that conform the service.

Use __carrots__ right away with:
`pip install carrots`
## Examples

# TODO
What I'm planning to do soon enough:
- Why carrots???
- Explain the architecture, some use cases, draw some diagrams
- Document this sh*t!
- Develop the same library for GO and Scala
- TESTS, TESTS, TESTS!

# Extra
You're hugely encouraged to request pulls, open issues, or send me e-mails to antcarri at gmail dot com