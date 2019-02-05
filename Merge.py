# importing for run time calculation
import sys
import time
sys.setrecursionlimit(150000)
# Creating an array with input from user
arry = list()
number = input("Enter your elements:")
for i in range(int(number)):
        a = input("number :")
        arry.append(int(a))

# Print array entered by the user
print("ARRAY: ", arry)


# Define Merge function to merge two subarrays of arry[]: 1st subarray is arry[l..m], 2nd subarray is arry[m+1..r]
start = time.time()

def merge(arry, l, m, r):
    n1 = int(m - l + 1)
    n2 = int(r - m)

#  Temporary arrays:t1 and t2
# To Test for float: print("", n1)
    t1 = [0] * n1
    t2 = [0] * n2

    # Copying data to arrays t1[] and t2[]
    for i in range(0, n1):
        t1[i] = arry[l + i]

    for j in range(0, n2):
        t2[j] = arry[m + 1 + j]

    # Merging the t1[] and t2[] back into arry[l...m...r]
    i = 0	 # Initial index of 1st subarray
    j = 0	 # Initial index of 2nd subarray
    k = l	 # Initial index of 3rd subarray

    while i < n1 and j < n2:
        if t1[i] <= t2[j]:
            arry[k] = t1[i]
            i += 1
        else:
            arry[k] = t2[j]
            j += 1
        k += 1

    # if there are any remaining elements of t1, we copy here
    while i < n1:
        arry[k] = t1[i]
        i += 1
        k += 1

    # if there are any remaining elements of t[], we Copy here.
    while j < n2:
        arry[k] = t2[j]
        j += 1
        k += 1

# l: left index, r: right index of subarray of arry[] to be sorted


def mergesort(arry, l, r):
    if l < r:

        # To avoid overflow for large l& h, similar to (l+r)/2
        m = int((l+(r-1))/2)

        # Sorting of 1st and 2nd half
        mergesort(arry, l, m)
        mergesort(arry, m+1, r)
        merge(arry, l, m, r)


n = len(arry)
# Running the mergesort function for entered arry[]

mergesort(arry, 0, n - 1)
print("\n\nSorted array is")
for i in range(n):
    print("%d" % arry[i]),

end = time.time()
print("Elapsed time",end - start)
