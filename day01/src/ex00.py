purse: dict = {"gold_ingots": 3}

def add_ingot(purse):
    if "gold_ingots" in purse:
        get: int = purse["gold_ingots"]
    else:
        get: int = 0
    new_purse: dict = {"gold_ingots": get + 1}
    return new_purse
    
def get_ingot(purse):
    if "gold_ingots" in purse:
        purse["gold_ingots"] -= 1
    return purse
    
def empty(purse):
    purse = {}
    return purse
    
if __name__ == "__main__":
    print(add_ingot(get_ingot(add_ingot(empty(purse)))))

