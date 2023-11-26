import random
import numpy as np

if __name__ == "__main__":

    population_size = 10**6
    negPop = 48*10**4
    numbers = np.arange(population_size)

    voteArr = np.ones(population_size)
    selectedIdxs = np.random.choice(numbers, size=negPop, replace=False)

    voteArr[selectedIdxs] = -1

    plusCount = np.count_nonzero(voteArr == 1)
    negCount = np.count_nonzero(voteArr == -1)

    print("Plus Count: {}\nMinus Count: {}".format(plusCount, negCount))

    numIter = 100

    sampleVals = [20, 100, 400, 600]
    for sample in sampleVals:
        posMajorityCount = 0
        for i in range(numIter):
            idxs = np.random.choice(numbers, size=sample, replace=False)
            newArr = voteArr[idxs]
            samplePlusCount = np.count_nonzero(newArr == 1)
            sampleNegCount = np.count_nonzero(newArr == -1)
            if samplePlusCount > sampleNegCount:
                posMajorityCount += 1
        negMajorityCount = numIter - posMajorityCount
        print("Sample Size: {}\n+1 Majority Probability: {}\n-1 Majority Probability: {}"
            .format(sample, posMajorityCount/numIter, negMajorityCount/numIter))
