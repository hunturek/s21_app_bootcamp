purse1: dict = {"gold_ingots": 10}
purse2: dict = {"gold_ingots": 1, "gold_rocks": 3}
purse3: dict = {"gold_ingots": 2, "gold_apples": 8}

def squeak_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("SQUEAK")
        return result
    return wrapper

@squeak_decorator
def add_ingot(purse):
    if "gold_ingots" in purse:
        get: int = purse["gold_ingots"]
    else:
        get: int = 0
    new_purse: dict = {"gold_ingots": get + 1}
    return new_purse

@squeak_decorator
def get_ingot(purse):
    if "gold_ingots" in purse:
        purse["gold_ingots"] -= 1
    return purse

@squeak_decorator    
def empty(purse):
    purse = {}
    return purse
   
def split_booty(*purses):
    sum: int = 0
    for purse in purses:
        if "gold_ingots" in purse:
            sum += purse["gold_ingots"]
    if sum % 3 == 0:
        return {"gold_ingots": int(sum / 3)}, {"gold_ingots": int(sum / 3)}, \
            {"gold_ingots": int(sum / 3)}
    elif sum % 3 == 1:
        return {"gold_ingots": int(sum / 3 + 1)}, \
            {"gold_ingots": int(sum / 3)}, {"gold_ingots": int(sum / 3)}
    elif sum % 3 == 2:
        return {"gold_ingots": int(sum / 3 + 1)}, \
            {"gold_ingots": int(sum / 3 + 1)}, {"gold_ingots": int(sum / 3)}
    
if __name__ == "__main__":
    print(add_ingot(add_ingot(empty(purse1))))

