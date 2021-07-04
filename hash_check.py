from hashlib import sha1, sha512, md5
file = "source.xml"

sha1_hash = sha1()
sha512_hash = sha512()
md5_hash = md5()

BLOCK_SIZE = 65536

with open(file, 'rb') as f:
    fb = f.read(BLOCK_SIZE)
    while len(fb) > 0:
        sha1_hash.update(fb)
        fb = f.read(BLOCK_SIZE)

print(sha1_hash.hexdigest())