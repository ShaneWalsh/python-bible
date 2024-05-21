import random
import math

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
