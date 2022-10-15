'''
used to hide the actual implementaion code to the user 

python does't support abstraction

than i need module to import name is ABC as known as "abstract base class".

'''

from abc import ABC, abstractmethod

class shop(ABC):
    @abstractmethod
    def stock(self):
        pass
    @abstractmethod
    def sale(self):
        pass

    def discount(self):
        print("Discount Not Available")



class TipTop(shop):
    def sale(self):
        print("10 5 sale on momday")

    def stock(self):
        print("stock is full")

class kiaranstore(shop):
    def sale(self):
        print("10 5 sale on momday")

    def stock(self):
        print("stock is  available")

shop1 = TipTop()
shop2 = kiaranstore()
shop1.stock()
shop1.sale()