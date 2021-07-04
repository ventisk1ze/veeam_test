from hashlib import sha1, sha256, md5
import sys

BLOCK_SIZE = 65536
INPUT_FILE_NAME = sys.argv[1]
FOLDER = sys.argv[2]


def hash(file, hash_type):
    if hash_type == "sha1":
        hash_object = sha1()
    elif hash_type == "sha256":
        hash_object = sha256()
    elif hash_type == "md5":
        hash_object = md5()
    with open(file, 'rb') as f:
        fb = f.read(BLOCK_SIZE)
        while len(fb) > 0:
            hash_object.update(fb)
            fb = f.read(BLOCK_SIZE)
    return hash_object.hexdigest()


input_file = open("input.txt", 'r', encoding='utf-8-sig')
for line in input_file:
    properties = line.split(" ")
    properties[2] = properties[2].strip("\n")
    path = FOLDER + properties[0]
    if(hash(path, properties[1]) == properties[2]):
        print(properties[0] + " " + "OK")
    else:
        print(properties[0] + " " + "FAIL")
