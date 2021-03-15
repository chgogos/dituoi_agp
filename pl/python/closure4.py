import logging

logging.basicConfig(level=logging.INFO)


def logger(func):
    def log_func(*args):
        logging.info(f'Running "{func.__name__}" with arguments {args}')
        print(func(*args))

    return log_func


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


add_logger = logger(add)
sub_logger = logger(sub)

add_logger(3,3)
sub_logger(3,3)

# INFO:root:Running "add" with arguments (3, 3)
# 6
# INFO:root:Running "sub" with arguments (3, 3)
# 0