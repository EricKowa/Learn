def three_timser(func):
    def wrapper(*args):
        func(*args)
        func(*args)
        func(*args)
    return wrapper