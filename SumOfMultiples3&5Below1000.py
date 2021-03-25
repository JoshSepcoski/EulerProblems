def multiesOfFiveAndThree(top):
    MultOfThree = 3
    MultOfFive = 5
    MultOfFifteen = 15
    counter = 1
    limit = top/3
    fiveSum = 0
    threeSum = 0
    fifteenSum = 0

    while counter < limit:
        if (counter*MultOfFive) < top:
            fiveSum = (MultOfFive*counter) + fiveSum 
        if (counter*MultOfFifteen) < top:
            fifteenSum = (MultOfFifteen*counter) + fifteenSum 
        threeSum = (MultOfThree*counter) + threeSum
        counter += 1
    totSum = threeSum + fiveSum - fifteenSum
    return totSum
print(multiesOfFiveAndThree(1000))