

def some_function():
    for i in range(4):
        yield i

for i in some_function():
    print(i)