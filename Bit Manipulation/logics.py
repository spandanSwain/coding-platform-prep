# https://www.google.com/url?sa=i&url=https%3A%2F%2Fopen4tech.com%2Flogical-vs-arithmetic-shift%2F&psig=AOvVaw0s2PI7mcnzd2pobTMgcDoE&ust=1760623891883000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCMDb7ryxppADFQAAAAAdAAAAABAE
# CHECK THAT LINK TO SEE HOW LS AND RS WORK
"""
1 - To find Least Significant Bit (LSB) of a number (i.e. for 4 0100 LSB is 0 - item at last index)
    LSB = number & 1
        ex: 
            0 1 0 0
        &   0 0 0 1
        ____________
            0 0 0 0 = 0 = LSB
This is same as doing:
    res = ""
    looping till number > 0 and appending number%2 at start of res, i.e.
    while number>0:
        res = str(number%2) + res (in bits: no loop, simply n&1, get LSB)
"""

"""
to insert LSB at end do:
    shift the answer's bit to 1 left (left shift 1 pos, i.e. ans << 1)
    then do ->  | (number & 1)
    i.e. ans = (ans << 1) | (number & 1)
"""

"""
continue operation by ignoring the LSB which was added:
    number = number >> 1 (ignore 1 space from right)
"""