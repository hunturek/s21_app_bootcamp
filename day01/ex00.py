def empty(purse:dict[str, int]):
  return {}

def add_ingot(purse:dict[str, int]):
  if "gold_ingots" not in purse:
    return {"gold_ingots": 1}
  else:
    return {"gold_ingots": purse["gold_ingots"] + 1}

def get_ingot(purse:dict[str, int]):
  if "gold_ingots" not in purse or purse["gold_ingots"] == 1:
    return {}
  return {"gold_ingots": purse["gold_ingots"] - 1}
