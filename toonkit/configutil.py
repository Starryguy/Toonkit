import random

def file(location, file):
    def internal():
        return getattr(__import__(location, globals(), locals(), [file], -1), file)
    return internal

def randomFile(*args):
    possiblities = len(args)
    def internal():
        return args[random.randrange(possiblities)]()
