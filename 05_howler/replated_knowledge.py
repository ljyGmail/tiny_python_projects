# @ 5.1 Reading files
import os
print(os.path.isfile('blargh'))

# help(os)

file = '/var/lib/db.txt'
print(os.path.dirname(file))
print(os.path.basename(file))

file = 'inputs/fox.txt'
print(os.path.isfile(file))

# file handler
fh = open(file)

# file = 'blargh'
# open(file) ## FileNotFoundError

print(type(fh))

# help(fh)

print(fh.read())
print(fh.read())

# Each time you open() the file, you get a fresh file handle to read():
print(open(file).read())
print(open(file).read())

text = open(file).read()
print(text)
print(type(text))

print(open(file).read().rstrip())

# @ 5.2 Writing files
out_fh = open('05_howler/test-outs/out.txt', 'wt')

print(out_fh.write('this is some text\n'))

print(len('this is some text\n'))

print('this is some more text', file=out_fh)

out_fh.close()

print(open('05_howler/test-outs/out.txt').read())

print("I am what I am an' I'm not ashamed.", file=open(
    '05_howler/test-outs/hagrid.txt', 'wt'))

print(open('05_howler/test-outs/hagrid.txt').read())

# Recommend way to write to a file
fh = open('05_howler/test-outs/hagrid.txt', 'wt')
fh.write("I am what I am an' I'm not ashamed.\n")
fh.close()
