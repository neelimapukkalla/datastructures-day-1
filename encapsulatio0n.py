#protected
class encap:
    _a=10
    c=20
    def encapfunction(self):
        b=200
        print("encapfunction-accesing protected")
        print(self._a+10)
obj=encap()
print(obj._a)
obj.encapfunction()
print(obj.c)
