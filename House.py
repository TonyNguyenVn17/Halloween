import random


class House():

    def __init__(self):
        self.candy = random.randint(1, 10)

    def get_candy(self):
        return self.candy

    def __str__(self):
        return str(self.candy)


    
