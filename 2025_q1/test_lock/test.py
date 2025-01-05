import threading
from threading import Lock


class FooBar:
    def __init__(self, n):
        self.n = n
        self.LockFoo = Lock()
        self.LockBar = Lock()
        self.LockBar.acquire()

    def foo(self, printFoo: 'Callable[[], None]') -> None:

        for i in range(self.n):
            self.LockFoo.acquire()
            printFoo()
            self.LockBar.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:

        for i in range(self.n):
            self.LockBar.acquire()
            printBar()
            self.LockFoo.release()