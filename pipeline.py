'''
The pipeline decorator makes a function into a stage in a zmq-powered pipeline.

It takes each message off of the network and feeds it through the decorated
function and pushes the return value back over the network.

This decorator will execute the function you decorate and immediately start
interacting with the network indefinately. Too much magic? 
I don't know.

arguments:
    in_ports -- list of ints or None, the ports to read from
    out_port -- int or None, the port to output on
    ip -- string, ip address to listen on, defaults to localhost

The function to decorate should take exactly one argument if in_ports is
provided and should return a value if out_port is provided.
'''
import zmq

class pipeline(object):
    def __init__(self, in_ports=None, out_port=None, ip='localhost'):
        context = zmq.Context()
        self.output = None
        if out_port:
            self.output = context.socket(zmq.PUSH)
            self.output.bind('tcp://*:%d' % out_port)

        if not in_ports:
            in_ports = []

        self.inputs = []
        for port in in_ports:
            input = context.socket(zmq.PULL)
            input.connect('tcp://%s:%d' % (ip, port))
            self.inputs.append(input)

        self.poller = zmq.Poller()
        for input in self.inputs:
            self.poller.register(input, zmq.POLLIN)

    def __call__(self, fn):
        if self.inputs:
            def pipefn():
                ready = dict(self.poller.poll())
                for input in self.inputs:
                    if ready.get(input) == zmq.POLLIN:
                        if self.output:
                            self.output.send(fn(input.recv()))
                        else:
                            fn(input.recv())
            self.pipefn = pipefn
        elif self.output:
            def pipefn():
                self.output.send(fn())
            self.pipefn = pipefn
        else:
            self.pipefn = fn
        return self

    def run(self):
        while True:
            self.pipefn()

