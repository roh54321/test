Numerals = ["I", "V", "X", "L", "C", "D", "M"]
Numeralvalues = ["1", "5", "10", "50", "100", "500", "1000"]

valueget = input("Give a number: ")
def getvalue(valueget):
    Numeralpos = Numeralvalues.index(valueget)
    return Numerals[Numeralpos]
Value = getvalue(valueget)
print(Value)