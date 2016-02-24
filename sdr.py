"""
Author: Karthik Uppuluri
Brute forcing SDR count for a family of subsets;
"""

subsets = [{1,2,3},{1,4,5},{1,6,7},{2,4,6},{2,5,7},{3,4,7},{3,5,6}]

def sdr(index, selected_set):
    if index == len(subsets) - 1:
        # it's the last index. if a value is found here, we increment the count.
        count = 0
        for num in subsets[index]:
            if num not in selected_set:
                count += 1
        return count

    count = 0
    for num in subsets[index]:
        if num not in selected_set:
            count += sdr(index + 1, selected_set + (num,))

    return count


out = sdr(0, ())
print "out: ", out
