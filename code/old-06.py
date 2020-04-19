import base64

def encoder(param):
    """20번 인코딩"""
    param = param.encode('utf-8')
    for i in range(0,20):
        param = base64.b64encode(param)
    param = param.decode('utf-8')
    return param

def replacer(param):
    """규칙에 맞게 교체"""
    param = param.replace("1", "!")
    param = param.replace("2", "@")
    param = param.replace("3", "$")
    param = param.replace("4", "^")
    param = param.replace("5", "&")
    param = param.replace("6", "*")
    param = param.replace("7", "(")
    param = param.replace("8", ")")
    return param

id = "admin"
pw = "nimda"

print("id: " + replacer(str(encoder(id))) + "\n")
print("pw: " + replacer(str(encoder(pw))) + "\n")