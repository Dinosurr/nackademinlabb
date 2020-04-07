import itertools


def readLine(fname, nLines):
    with open(fname) as f:
        for line in itertools.islice(f,nLines):
            print(line)

readLine('test.txt', 2)
