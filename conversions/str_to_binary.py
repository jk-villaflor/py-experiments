import sys

def string_to_binary(target:str)->str:
    res = ''.join(format(ord(i), '08b') for i in target)
    return res

binaryString = string_to_binary(sys.argv[1])
print(binaryString)