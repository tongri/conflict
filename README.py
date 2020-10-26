<<<<<<< HEAD
def food(number):
    return "bulochka"*number
=======
def shouter(a):
    L = []

    for c in range(1, a + 1):

            if (c % fizz == 0) and (c % buzz == 0):
                L.append('FB')#print ("FB")
            elif c % fizz == 0:
                L.append('F')#print("F")#
            elif c % buzz == 0:
                L.append('B')#print ("B")#
            else:
                L.append(c)#print(c)#
    G = (': ' .join(map(str, L)))
    print(G)
#print(shouter(a))
fizz = int(input("Enter first number"))
buzz = int(input("Enter second number"))
a = int(input("Enter the third one"))
shouter(a)
>>>>>>> 6f5f5808d9a31159a89cf0f1f9d9c067f16f4252
