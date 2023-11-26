import random
from datetime import datetime
random.seed(datetime.now().timestamp())

if __name__ == "__main__":
    tvals = [5*10**4, 9*10**4, 16*10**4]
    movearr = [-1, 1]
    counts = []
    for tval in tvals:
        c = 0
        maxVal = 0
        minVal = 0
        currVal = 0
        for i in range(tval):
            rval = random.randint(0, 100) % 2
            currVal += movearr[rval]
            maxVal = max(currVal, maxVal)
            minVal = min(currVal, minVal)
            if currVal == 0:
                c += 1
        counts.append(c)
        print("For t = {}: Count = {}, MaxVal = {}, MinVal = {}, CurrVal = {}".format(tval, c, maxVal, minVal, currVal))
    print(counts)