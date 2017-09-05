import os
import sys
import hashlib

def hash(file, method):
    if not os.path.isdir(file):
        f = open(file, 'rb')
        sum = ""
        if method == "sha1":
            sum = hashlib.sha1(f.read()).hexdigest()
        elif method == "sha224":
            sum = hashlib.sha224(f.read()).hexdigest()
        elif method == "sha256":
            sum = hashlib.sha256(f.read()).hexdigest()
        elif method == "sha384":
            sum = hashlib.sha384(f.read()).hexdigest()
        elif method == "sha512":
            sum = hashlib.sha512(f.read()).hexdigest()
        elif method == "md5":
            sum = hashlib.md5(f.read()).hexdigest()
        f.close()
        return sum
    else:
        return "dir"

for file in os.listdir('.'):
    if not file == "rename.py":

        filename, file_extension = os.path.splitext(file)

        if len(sys.argv) >= 2:
            sum = hash(file, sys.argv[1])
        else:
            sum = hash(file, "md5")
        try:
            print("Trying to rename: " + file)

            if os.path.isfile(sum + file_extension):
                print("file " + sum + file_extension + " already exists")
                if not file == (sum + file_extension):
                    print("Removing: " + file + " because it is a duplicate")
                    os.remove(file)

            elif not sum == "dir":
                os.rename(file, sum + file_extension)
                print(file + ' --> ' + sum + file_extension)
            else:
                print("Skipping directory " + file)
        except Exception as e:
            print("Error displaying file name.")

        print("")
