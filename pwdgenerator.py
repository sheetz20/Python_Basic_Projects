import random

def generatePwd(values,pwd_length):
    pwd = "".join(random.sample(values,pwd_length))
    return pwd

if __name__ == "__main__":
    pwd_length = int(input("enter length of password "))
    values = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()?"
    password = generatePwd(values,pwd_length)
    print(password)