This library defines a decorator that turns any function into a stage in a zmq
pipeline.

Example time:

This is a boring function.

def echo(data):
    return data

And this is a boring part of a zmq pipeline that takes input from ports 5555,
5556, and 5557 over tcp on localhost and echos everything it to port 5558.

from pipeline import pipeline

@pipeline([5555,5556,5557], 5558)
def echo(data):
    return data

Is it any good?
    Yes.

Is a magical?
    Maybe too much.

