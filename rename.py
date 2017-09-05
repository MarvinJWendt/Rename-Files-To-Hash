import os
import hashlib

def sha1(file):
    f = open(file, 'rb')
    sum = hashlib.sha1(f.read()).hexdigest()
    f.close()
    return sum

for file in os.listdir('.'):
    if not file.endswith('.py'):
        filename, file_extension = os.path.splitext(file)
        sum = sha1(file)
        print(file + ' --> ' + sum)
        os.rename(file, sum + file_extension)
