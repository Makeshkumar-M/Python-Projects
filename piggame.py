import random #to get the random values

def random_roll():
    min_value=1
    max_value=6
    roll=random.randint(min_value,max_value) # given range for random values

    return roll 

Value=random_roll()
print(Value)