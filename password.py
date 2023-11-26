import bcrypt
password = b"nehajaiswal@123"
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
print(hashed) 

enter_pass =  input('enter your password')
enterd_pass  = bytes(enter_pass , encoding='utf-8' )
if bcrypt.checkpw(enter_pass, hashed):
    print("login succ")
else:
    print("wrong pass")    