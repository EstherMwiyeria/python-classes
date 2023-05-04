 #class Fruits:
#     flavor = "Mango"


class Fruit:
    def __init__(self,flavor,size,shape):
        
        self.flavor = flavor
        self.size = size
        self.shape = shape
        

    def eat(self):
        return f"The {self.flavor} is very sweet"
    def fruit_purchase(self):
        return f"Hello can I have a {self.flavor}"
    def fruit_sale(self):
        return f"The {self.flavor} is very expensive"
    