# *args 與 **kwargs

def print_args(x, *args, **kwargs):
    print(x, type(x))
    print(args, type(args))
    print(kwargs, type(kwargs))


if __name__ == '__main__':
    print_args('john', 100, 90, 80, age=18, num=10)

