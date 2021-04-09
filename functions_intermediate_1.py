import random


def randInt(min=0, max=100):
    if min > max:
        return False
    elif max < 0:
        return False
    else:
        num = random.random() * (max-min) + min
        return num


# print(randInt()) 		    # should print a random integer between 0 to 100
# print(randInt(max=50)) 	    # should print a random integer between 0 to 50
# print(randInt(min=50)) 	    # should print a random integer between 50 to 100
# print(randInt(min=50, max=500))    # should print a random integer between 50 and 500

print("0-100: "+str(randInt()))
print("0-50: "+str(randInt(max=50)))
print("50-100: "+str(randInt(min=50)))
print("50-500: "+str(randInt(min=50, max=500)))
