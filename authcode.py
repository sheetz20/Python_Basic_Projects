import random

def generateAuthCode(values):
    code = "".join(random.sample(values,4))
    return code
    

if __name__ == "__main__":
    values = "0123456789"
    authCode = generateAuthCode(values)
    print(authCode)
