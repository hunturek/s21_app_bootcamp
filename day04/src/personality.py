import random

traits = {'neuroticism', 'openness', 'conscientiousness', \
    'extraversion', 'agreeableness'}

def generate_personality():
    traits_sum: int = 0
    traits_nums: list = {}
    for i in traits:
        trait = random.randint(0, 100 - traits_sum)
        traits_sum += trait
        traits_nums[i] = trait
    traits_nums['agreeableness'] += 100 - sum(traits_nums.values())
    return traits_nums
    
def turrets_generator():
    personality = generate_personality()
    turret_class = type('Turret', (), {
        'shoot': lambda self: print('shooting'),
        'search': lambda self: print('searching'),
        'talk': lambda self: print('talking'),
        **personality
    })
    return turret_class()
    
if __name__ == "__main__":
    turret = turrets_generator()
    print(f"Neuroticism: {turret.neuroticism}")
    print(f"Openness: {turret.openness}")
    print(f"Conscientiousness: {turret.conscientiousness}")
    print(f"Extraversion: {turret.extraversion}")
    print(f"Agreeableness: {turret.agreeableness}")
    turret.shoot()
    turret.search()
    turret.talk()
