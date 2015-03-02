#!/usr/bin/env python3

"""
http://spark-public.s3.amazonaws.com/algo1/programming_prob/Median.txt

The goal of this problem is to implement the "Median Maintenance" algorithm
(covered in the Week 5 lecture on heap applications). The text file contains a
list of the integers from 1 to 10000 in unsorted order; you should treat this as
a stream of numbers, arriving one by one. Letting xi denote the ith number of
the file, the kth median mk is defined as the median of the numbers x1,…,xk.
(So, if k is odd, then mk is ((k+1)/2)th smallest number among x1,…,xk; if k is
even, then mk is the (k/2)th smallest number among x1,…,xk.)

In the box below you should type the sum of these 10000 medians, modulo 10000
(i.e., only the last 4 digits). That is, you should compute
(m1+m2+m3+⋯+m10000)mod10000.

OPTIONAL EXERCISE: Compare the performance achieved by heap-based and
search-tree-based implementations of the algorithm.
"""

import heapq
import math

def main():
    filename = "Median.txt"
    with open(filename) as f:
        data = f.readlines()

    heap_low = [] # max
    heap_high = [] # min
    median = None
    medians = []

    # First number
    median = int(data[0])
    medians.append(median)
    heapq.heappush(heap_high, median)
    
    for line in data[1:]:
        integer = int(line)
        if integer < median:
            # Python heaps only support fetch min so to effectively use
            # fetch min as fetch max, flip the sign of the integer
            heapq.heappush(heap_low, -integer)
        else:
            heapq.heappush(heap_high, integer)
        lhl = len(heap_low)
        lhh = len(heap_high)
        ldiff = abs(lhl - lhh)
        if ldiff > 1:
            # Rebalance so median calculations are correct
            # ldiff should never be above 2 as that means rebalance failed when
            # ldiff was 2
            assert ldiff == 2
            # Sign flips for effective fetch max from heap_low
            if lhl > lhh:
                i = -heapq.heappop(heap_low)
                heapq.heappush(heap_high, i)
            elif lhh > lhl:
                i = heapq.heappop(heap_high)
                heapq.heappush(heap_low, -i)
        lhl = len(heap_low)
        lhh = len(heap_high)
        is_even = True if (lhl + lhh) % 2 == 0 else False
        # Calculate the new median
        if is_even:
            # Median is the average of the integers from each heap
            # Python heaps are fetch min only. To implement fetch max, integer
            # signs were flipped before inserting into heap. Correct the sign
            # before use.
            heap_low_int = -heap_low[0]
            heap_high_int = heap_high[0]
            #median = int((heap_low_int + heap_high_int) / 2)
            median = heap_low_int
        else:
            if lhl > lhh:
                median = -heap_low[0]
            elif lhh > lhl:
                median = heap_high[0]
        medians.append(median)
    answer = sum(medians) % 10000
    return answer



if __name__ == '__main__':
    print(main())
