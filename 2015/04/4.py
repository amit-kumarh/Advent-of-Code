import hashlib
input = "bgvyzdsv"

i = 1
while True:
    h = hashlib.md5((input + str(i)).encode())
    if str(h.hexdigest()).startswith('000000'):
        print(i)
        break
    i += 1
    
    
