from contextlib import contextmanager


class HelloWorldContextManager:
    def __enter__(self):
        print("Entering the context")
        return "Hello, World!"

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")


@contextmanager
def hello_world_context_manger_method():
    print("Entering the context")
    yield "Hello, World!"
    print("Exiting the context")
