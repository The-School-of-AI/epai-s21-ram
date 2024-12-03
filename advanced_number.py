class AdvancedNumber:

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Value: {self.value}"
    
    def __repr__(self):
        return f"AdvancedNumber({self.value})"
    
    def __add__(self, other):
        if isinstance(other, AdvancedNumber):
            return AdvancedNumber(self.value + other.value)
        elif isinstance(other, (int, float)):
            return AdvancedNumber(self.value + other)
        else:
            raise TypeError("Unsupported operand type(s) for +: 'AdvancedNumber' and '{}'".format(type(other).__name__))
    
    def __sub__(self, other):
        if isinstance(other, AdvancedNumber):
            return AdvancedNumber(self.value - other.value)
        elif isinstance(other, (int, float)):
            return AdvancedNumber(self.value - other)
        else:
            raise TypeError("Unsupported operand type(s) for -: 'AdvancedNumber' and '{}'".format(type(other).__name__))
    
    def __mul__(self, other):
        if isinstance(other, AdvancedNumber):
            return AdvancedNumber(self.value * other.value)
        elif isinstance(other, (int, float)):
            return AdvancedNumber(self.value * other)
        else:
            raise TypeError("Unsupported operand type(s) for *: 'AdvancedNumber' and '{}'".format(type(other).__name__))
        
    def __truediv__(self, other):
        if isinstance(other, AdvancedNumber):
            return AdvancedNumber(self.value / other.value)
        elif isinstance(other, (int, float)):
            return AdvancedNumber(self.value / other)
        else:
            raise TypeError("Unsupported operand type(s) for /: 'AdvancedNumber' and '{}'".format(type(other).__name__))
        
    def __mod__(self, other):
        if isinstance(other, AdvancedNumber):
            return AdvancedNumber(self.value % other.value)
        elif isinstance(other, (int, float)):
            return AdvancedNumber(self.value % other)
        else:
            raise TypeError("Unsupported operand type(s) for %: 'AdvancedNumber' and '{}'".format(type(other).__name__))

    def __eq__(self, other):
        if isinstance(other, AdvancedNumber):
            return self.value == other.value
        elif isinstance(other, (int, float)):
            return self.value == other
        else:
            return False
        
    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if isinstance(other, AdvancedNumber):
            return self.value < other.value
        elif isinstance(other, (int, float)):
            return self.value < other
        else:
            return False
        
    def __le__(self, other):
        return self.value <= other.value if isinstance(other, AdvancedNumber) else self.value <= other

    def __gt__(self, other):
        return self.value > other.value if isinstance(other, AdvancedNumber) else self.value > other

    def __ge__(self, other):
        return self.value >= other.value if isinstance(other, AdvancedNumber) else self.value >= other
    
    def __hash__(self):
        return hash(self.value)
    
    def __bool__(self):
        return bool(self.value)
    
    def __call__(self):
        return self.value ** 2
    
    def __format__(self, format_spec):
        if "f" in format_spec:
            return f"{self.value:.{format_spec.split('.')[1]}}"
        elif "x" in format_spec:
            return f"{self.value:#x}"
        else:
            return str(self)
        
    def __del__(self):
        print(f"AdvancedNumber with value {self.value} is being destroyed")
