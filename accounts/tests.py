import hashlib

userpass = "1222323"
h = hashlib.new("SHA256")
h.update(userpass.encode())

print(h.digest())
print(h.hexdigest())
