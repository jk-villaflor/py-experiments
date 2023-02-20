import sys

def binary_to_hash(target: str)->str:
    return hash(target)


hashedString = binary_to_hash(sys.argv[1])
print(hashedString)
