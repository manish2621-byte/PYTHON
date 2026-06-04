def before(func):
    def wrapper():
        print("before function calling")
        func()
    return wrapper

def after(func):
    def executor():
        func()
        print("after function calling")
    return executor

@before
@after
def test():
    print("test function calling")
    