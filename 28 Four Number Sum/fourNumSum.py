def fourNumberSum(array, targetSum):

    quadruplets = []
    sums = {}

    for x in range(0, len(array) - 1):
        for y in range(x + 1, len(array)):
            sum_ = array[x] + array[y]
            if sum_ in sums:
                sums[sum_].append([x, y])
            else:
                sums[sum_] = [[x, y]]

    for P in sums:
        for pair in sums[P]:
            sum_ = array[pair[0]] + array[pair[1]]
            potentialSum = targetSum - (sum_)

            if potentialSum in sums:
                for pair2 in sums[potentialSum]:
                    p1 = pair2
                    p2 = [pair[0], pair[1]]
                    if p1[0] in p2 or p1[1] in p2:
                        continue
                    p1.sort()
                    p2.sort()
                    if p1[0] != p2[0] and p1[1] != p2[1]:
                        qr = [array[p1[0]], array[p1[1]],array[p2[0]],array[p2[1]]]
                        qr.sort()
                        if qr not in quadruplets:
                            quadruplets.append(qr)
    return quadruplets


