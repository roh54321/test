Numerals = ["I", "V", "X", "L", "C", "D", "M"]
Numeralvalues = ["1", "5", "10", "50", "100", "500", "1000"]

def main():
    num = askuser()
    done = convert(num)
    print(done)
    

def askuser():
    stringinput = input("Give a number between 1 and 3999 please: ")
    num = int(stringinput)
    if num > 3999 or num < 1:
        raise Exception("Number too big or too small")
    return stringinput

def convert(num):
    s = ""
    place = len(num) - 1
    placevalue = 1
    Iteration = 0
    while place != -1:    
        print("num = {}, placevalue = {}".format(num[place], placevalue))
        templist = Numerals[Iteration * 2:Iteration * 2 + 3]
        print(templist)
        numplace = int(num[place])

        if numplace == 0:
            pass
        elif numplace < 4:
            s = templist[0] * numplace + s
        elif numplace == 4:
            s = templist[0] + templist[1] + s
        elif numplace < 9:
            s = templist[1] + templist[0] * (numplace - 5) + s
        else:
            s = templist[0] + templist[2] + s

        placevalue *= 10
        place -= 1
        Iteration += 1
    return s

def test_main():
    inputs = [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "501",
        "0",
    ]
    for i in inputs:
        output = convert(i)
        print("in: {}, out: {}".format(i, output))

if __name__ == "__main__":
    # main()
    test_main()
