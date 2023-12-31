class Geek:
    def __init__(self, value):
        self.value = value

    def __and__(self, obj):
        print("AND Operator Overloaded")
        if isinstance(obj, Geek):
            return self.value & obj.value
        else:
            raise ValueError("Must be an object of class Geek")

    def __or__(self, obj):
        print("OR Operator Overloaded")
        if isinstance(obj, Geek):
            return self.value | obj.value
        else:
            raise ValueError("Must be an object of class Geek")

    def __xor__(self, obj):
        print("XOR Operator Overloaded")
        if isinstance(obj, Geek):
            return self.value ^ obj.value
        else:
            raise ValueError("Must be an object of class Geek")

    def __lshift__(self, obj):
        print("Left Shift Operator Overloaded")
        if isinstance(obj, Geek):
            return self.value << obj.value
        else:
            raise ValueError("Must be an object of class Geek")

    def __rshift__(self, obj):
        print("Right Shift Operator Overloaded")
        if isinstance(obj, Geek):
            return self.value >> obj.value
        else:
            raise ValueError("Must be an object of class Geek")

    def __invert__(self):
        print("Invert operator overloaded")
        return ~self.value

# Driver's code
if __name__ == "__main__":
    a = Geek(10)
    b = Geek(12)
    print(a & b)
    print(a | b)
    print(a ^ b)
    print(a << b)
    print(a >> b)
    print(~a)
