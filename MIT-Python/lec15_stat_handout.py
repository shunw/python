def stdDev(x):
    # x is the list or other thing
    mean = sum(x)/float(len(x))
    tot = 0.0
    for i in x:
        tot += (float(i) - mean) ** 2

    return (tot / float(len(x))) ** .5



if __name__ == '__main__':
    print stdDev_1([1, 2, 3])
