import random
import math

def randomEmotion(v):
    if(v < 20):
        return "young"
    else:
        return "Old"

health = 50
difficultly = random.randint(1,3)
potionHealth = int(random.randint(25,50) / difficultly)

print('health', health)
health += potionHealth
print('health', health)
    

print(round(5/3))
print(math.floor(5/3))
print(math.ceil(5/3))
print(math.sin(12232) * math.pow(4, 3))

name = input("Whats your name bro?")
print("{} thats a lovely name.".format(name))
age = input("Your age?")
template= "Whoooo {1}, you are soooo {0}"
output = template.format(randomEmotion(int(age)),name)
print(output)


    
