import sys

def stderr(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def upperbound(*args):
    return int(max(args))

def lowerbound(*args):
    return int(min(args))
