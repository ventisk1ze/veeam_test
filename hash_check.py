from hashlib import sha1, sha256, md5

BLOCK_SIZE = 65536
FOLDER = 'hash_data/'

def hash(file, hash_type):
    if hash_type == "SHA1":
        hash_object = sha1()
    elif hash_type == "SHA256":
        hash_object = sha256()
    elif hash_type == "MD5":
        hash_object = md5()
    with open(file, 'rb') as f:
        fb = f.read(BLOCK_SIZE)
        while len(fb) > 0:
            hash_object.update(fb)
            fb = f.read(BLOCK_SIZE)
    return hash_object.hexdigest()