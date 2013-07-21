#!/usr/bin/env python
# from __future__ import division
import argparse
import numpy
import math


parser = argparse.ArgumentParser(description='Script to find comparisons done by quicksort')
parser.add_argument('input_file', type=str, help='Input file containing array')
parser.add_argument('--pivot_method', type=int, default=1, 
                    help='Pivot selection technique. 1 (default) - First element, 2 - Last element, 3 - Median of three')
args = parser.parse_args()
  
def find_median(arr, left, right):
    if right - left < 2:
        return left
        
    mid = (left + right) / 2
    temp = [arr[left], arr[mid], arr[right]]
    median = int(numpy.median(temp))
    pos = temp.index(median)
    
    if pos == 1:
        return mid
    elif pos == 2:
        return right
    else: return left
  
def choose_pivot(arr, left, right, method):   
    if method == 1:
        return left
    elif method == 2:
        return right
    elif method == 3: # return median of first, last and mid
        return find_median(arr, left, right)
    else:
        raise Exception("Invalid pivot selection mode!")
             
def partition(arr, left, right, pivot):
    if arr[pivot] != arr[left]: # if pivot is not the first element, swap
        arr[left], arr[pivot] = arr[pivot], arr[left]
        
    i = left + 1 #initialize i = 1
    
    for j in range(i, right + 1):
        if arr[j] < arr[left]:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
            
    # partition complete, swap pivot and i - 1
    arr[left], arr[i-1] = arr[i-1], arr[left]
    return i - 1
    
def q_sort(arr, left, right, pivot_method):
    num_comparisons = 0
        
    if left < right:
        pivot = choose_pivot(arr, left, right, pivot_method)
        pivot_pos = partition(arr, left, right, pivot)
        num_comparisons += right - left
        
        num_comparisons += q_sort(arr, left, pivot_pos - 1, pivot_method)
        num_comparisons += q_sort(arr, pivot_pos + 1, right, pivot_method)
    
    return num_comparisons
# load text file
arr = numpy.loadtxt(args.input_file, int) 
# print 'Total number of inversions in the given dataset = ' + str(count_inversions(arr)[1])
# 
# arr = [8, 2]
# p = choose_pivot(arr, 0, 1, 3)
# print p


# print (arr)

# # partition(arr, 0, 6, 0)
n = q_sort(arr, 0, len(arr) - 1, args.pivot_method)

print (n)
# 
with open('output.txt', 'w') as file:
    for item in arr:
            file.write("{}\n".format(item))
    

# partition(arr, 0, 6, 0)
# # q_sort(arr, 0, len(arr) - 1)
# print (arr)

            
            
    
    
        

