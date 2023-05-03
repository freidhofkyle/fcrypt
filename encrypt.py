# importing python library rsa 
import rsa

# Opening and reading the public and private key
with open("public.pem", "rb") as f:
    public_key = rsa.PublicKey.load_pkcs1(f.read())

with open("private.pem", "rb") as f:
    private_key = rsa.PrivateKey.load_pkcs1(f.read())

m = input("What would you like to encrypt: ")

encrypted_message = rsa.encrypt(m.encode(), public_key)

with open("encrypted.message", "wb") as f:
    f.write(encrypted_message)

d = input("Decrypt the Message: ")

if d == "y":
    clear_message = rsa.decrypt(encrypted_message, private_key)
    print(clear_message.decode())

else:
    print("Not Doing anything")




 









