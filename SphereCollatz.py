#!/usr/bin/env python3


import sys

# ----
# main
# ----

if __name__ == "__main__" :
    collatz_solve(sys.stdin, sys.stdout)


def collatz_read (s) :
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    assert i > 0
    assert j > 0

    if(j > i):
        # Make sure i < j so works in range function
        temp = i
        i = j
        j = temp
    cache = [0]*500000
    finalMax = 1
    for n in range(i, j+1):
        if(cache[n] != 0):
            curMax = cache[n]
        else:
            curMax = collatz_calc(n)
            cache[n] = curMax
        if(curMax > finalMax):
            finalMax = curMax

    assert finalMax > 0
    return finalMax

# -------------
# collatz_calc
# -------------
def collatz_calc (n) :
    """
    n is the positive int passed in
    returns the cycle length of n
    """
    cycle = 1
    while n > 1 :
        if (n % 2) == 0 :
            n = (n // 2)
        else :
            n = (3 * n) + 1
        cycle += 1
    assert cycle > 0
    return cycle

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    r a reader
    w a writer
    """
    for s in r :
        i, j = collatz_read(s)
        v    = collatz_eval(i, j)
        collatz_print(w, i, j, v)
