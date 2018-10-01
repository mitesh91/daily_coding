# Given a number in the form of a list of digits, return all possible permutations.

# For example, given [1,2,3], return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

import copy
def permutation(alist):
    def permute(alist, l, r):
        if l==r:
            print (copy.copy(alist))
        else:
            for i in range(l, len(alist)):
                alist[i], alist[l] = alist[l], alist[i]
                permute(alist, l+1, r)
                alist[i], alist[l] = alist[l], alist[i]
    permute(alist, 0, len(alist)-1)
                
if __name__ == "__main__":
  permutation(['n', 'e', 'h'])
