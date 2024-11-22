def floatInputValidator(msg, reMsg):
    userInput=input(msg)
    while not type(userInput)==float:
        try:
            userInput=float(userInput)
        except Exception as e:
            print(f"the following error has occured {e}")
            userInput=input(reMsg)
    return userInput

def intInputValidator(msg, reMsg):
    userInput=input(msg)
    while not type(userInput)==int:
        try:
            userInput=int(userInput)
        except Exception as e:
            print(f"the following error has occured {e}")
            userInput=input(reMsg)
    return userInput

def listTypeValidator(arr, itemType):
    for item in arr:
        if not type(item)==itemType:
            return False
    return True

