import hashlib

# Setup

raw_prefix = "iwrupvqb"


def find_hash(hash_prefix):
    x = 1
    while True:
        hsh = hashlib.md5((raw_prefix + str(x)).encode())
        if hsh.hexdigest().startswith(hash_prefix):
            return x
        x += 1


# Part One

print('--Part One--')
print(find_hash('0' * 5))

# Part Two

print('--Part Two--')
print(find_hash('0' * 6))
