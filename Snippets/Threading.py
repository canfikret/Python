import threading
from pprint import pprint

def hello():
    print("hello")

def main():
    print(threading.active_count())
    t=threading.current_thread()
    pprint(vars(t))

    for t in threading.enumerate():
        pprint(t)

    tls=threading.local()
    tls.x=1
    tls.y=2
    tls.__dict__
    dir(tls)

    t=threading.Timer(5.0, hello)
    t.start()
main()
