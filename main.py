# importing python library rsa 
import rsa

# generating variable for the rsa key 
publc_key, private_key = rsa.newkeys(2048)

with open("public.pem", "wb") as f:
    f.write(publc_key.save_pkcs1("PEM"))

with open("private.pem", "wb") as f:
    f.write(private_key.save_pkcs1("PEM"))


 









