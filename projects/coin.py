import random


class Coin:
    def __init__(self,rare=False,clean=True, **kwargs):
        for key,value in kwargs.items():
            setattr(self,key,value)
        
        self.is_rare= rare;
        if rare:
            self.value = self.original_value
        else:
            self.value = self.original_value *1.25
        
        self.is_clean= clean;
        heads = True
        self.num_edges = 1
        self.diameter = 22.5 #mm
        self.thick = 3.15 #mm
        self.colour = self.clean_colour
    
    def rust(self):
        self.colour = self.rusty_colour

    def clean(self):
        self.colour = self.clean_colour    

    def flip(self):
        options=[True,False]
        choice = random.choice(options)
        self.heads = choice
    
class Euro(Coin):
    def __init__(self,rare=False,clean=True):
        data={
            "original_value":1.00,
            "clean_colour":"gold",
            "rusty_colour":"green"
            }
        super().__init__(rare,clean,**data)    

class TwoEuro(Coin):
    def __init__(self,rare=False,clean=True):
        data={
            "original_value":2.00,
            "clean_colour":"Silver",
            "rusty_colour":"Blue"
            }
        super().__init__(rare,clean,**data)    

    def rust(self):
        print("no rusty")
        # do nothing, doesnt rust.

coin1 = Euro()
print(coin1.value)
coin2 = Euro(True,True)
print(coin2.value)

print(coin1.colour)
coin1.rust()
print(coin1.colour)

coin3 = TwoEuro()
print(coin3.colour)
coin3.rust()
print(coin3.colour)
