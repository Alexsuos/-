class Tomato:
    states={1:'в земле',2:'побег',3:"помидор"}

    def __init__(self,index):
        self._index=index
        self._state=1
    def grow(self):
        if self._state<3:
            self._state+=1
    def is_ripe(self):
        if self._state==3:
            return print("вырос")
        else:
            return print("не вырос")



