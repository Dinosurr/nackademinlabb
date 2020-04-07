from itertools import islice

def write(fname, text1, text2):
    with open(fname, 'w') as f:
        f.write(text1)
        f.write(text2)
    txt = open(fname)
    print(txt.read())

write('test.txt', 'this is the test of writing a text\n', 'this is the second line')