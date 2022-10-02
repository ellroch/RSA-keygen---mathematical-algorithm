
def rsa_encryption(e, n, message):
    encryptedMessage = pow(message, e, n)
    print(str(message)+"^"+str(e)+"(mod"+str(n)+")= "+str(encryptedMessage)+"\n")
        


print("\nI'm gonna need three things from you, the exponent key to encrypt/decrypt (e or d), the modulii (n), and the message (number) I'm operating on(x or y).")
print("first things first, hit me with the exponent:")
e=int(input())
print("aight, now hit me with the modulii:")
n=int(input())
print("ok, now the message (number):")
message=int(input())
rsa_encryption(e,n,message)
print("\nthis window will self destruct... hit an key to continue")
input()
