'''
define a class inside a class is known as inner class.

'''

#eaxmple :- 
class color:
    def __init__(self):
        self.text_color = "black"
        self.obj_bg = self.background_color()

    def tet(self):
        print(self.text_color)


    class background_color:
        def __init__(self):
            self.bg = "grey"
        
        def background(self):
            print(self.bg)
obj = color()
obj.text()
obj.obj_bg.background()