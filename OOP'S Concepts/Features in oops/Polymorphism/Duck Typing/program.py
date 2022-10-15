'''

DUck Typing :- 
look like duck,
sound like duck,
walk like duck,
run like duck is known as duck typing . 
duck typing a way to implement the polymorphism .

'''


#example:- 
class India:
    def capital(self):
        print("New Delhi")

    def language(self):
        print("Hindi")

class Russia:
    def capital(self):
        print("mosico")

    def language(self):
        print("Russian")

a = India()
b = Russia()
def main(obj):
    obj.capital()
    obj.language()

main(a)
main(b)

    