# Creator = Kyle Freidhof

# Program = Encryption/Decryption 

# License = GPL3 

# Created May, 2 2023 

# importing python library rsa 
import rsa

# Opening and reading the public and private key
with open("public.pem", "rb") as f:
    public_key = rsa.PublicKey.load_pkcs1(f.read())

# opening and reading private key
with open("private.pem", "rb") as f:
    private_key = rsa.PrivateKey.load_pkcs1(f.read())

# asks what would you like to encrypt 
m = input("What would you like to encrypt: ")

# varriables for encrypting the message
encrypted_message = rsa.encrypt(m.encode(), public_key)

# opens encrypted file with encrypted message 
with open("encrypted.message", "wb") as f:
    f.write(encrypted_message)
# asks if you want to decrypt the program 
d = input("Decrypt the Message: ")

# if y then decrypt
if d == "y":
    clear_message = rsa.decrypt(encrypted_message, private_key)
    print(clear_message.decode())
# other wise print do nothing 
else:
    print("Not Doing anything")




 









