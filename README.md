# Pipeline
This library defines a decorator that turns any function into a zmq pipeline
stage.

## Example time
This is a boring function.

```python
def echo(data):
    return data
```

And this is a boring part of a zmq pipeline that takes input from ports 5555,
5556, and 5557 over tcp on localhost and echos everything it reads to port 5558.

```python
from pipeline import pipeline

@pipeline(in_ports=[5555,5556,5557], out_port=5558)
def echo(data):
    return data

echo.run()
```
## What do the examples do?
There are four example programs that cover every part of a pipeline.

* source -- continuously prints numbers on --out-port
* read -- reads from stdin and pushes to --out-port
* work -- reads from --in-ports, doubles the input, and puts it on --out-port
* sink -- reads from --in-ports and prints what it reads to stdout 

## How do I run them?
To set up a pipeline like this:
<pre>
source (5555) -->
                  work (5556) --> sink
read   (5558) -->
</pre>

In one shell start this (so you can see the output):

```bash
python source.py --out-port 5555 &
python work.py --in-ports 5555 5558 --out-port 5556 &
python sink.py --in-ports 5556
```

In another shell start this (so you can interact with it):

```bash
python read.py --out-port 5558
```
