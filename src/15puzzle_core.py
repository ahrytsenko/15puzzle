import simplegui

class Simple_class:
    sc = 0
    def __init__(self, value):
        self.sc = value
        
    def __str__(self):
        return str(self.sc)
        
sc_var = Simple_class(3)

print str(sc_var)
print sc_var
