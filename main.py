# Creator = Kyle Freidhof 

# Program = rsa generator 

# License = GPL3

# Created = May, 5 2024

# importing python library rsa 
import rsa

# generating variable for the rsa key 
publc_key, private_key = rsa.newkeys(2048)

# writing public key to file
with open("public.pem", "wb") as f:
    f.write(publc_key.save_pkcs1("PEM"))

# writing private key to file 
with open("private.pem", "wb") as f:
    f.write(private_key.save_pkcs1("PEM"))


 









