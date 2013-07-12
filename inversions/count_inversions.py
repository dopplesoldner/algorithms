#!/usr/bin/env python
import argparse
import numpy

parser = argparse.ArgumentParser(description='Script to find inversions in an array')
parser.add_argument('input_file', type=str, help='Input file containing array')
args = parser.parse_args()

def count_inversions(arr):
    if len(arr) <= 1:
        return arr, 0
        
    mid = len(arr) / 2
    left, x = count_inversions(arr[:mid])
    right, y  = count_inversions(arr[mid:])
    result, z = merge_and_count(left, right)
    
    return result, (x+y+z)
    
def merge_and_count(left, right):
    count, i, j = 0, 0, 0
    result = []
    left_len, right_len = len(left), len(right)

    while i < left_len and j < right_len:
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            count += left_len - i

    result.extend(left[i:])    
    result.extend(right[j:])        
    return result, count 
    
# load text file
arr = numpy.loadtxt(args.input_file)
print 'Total number of inversions in the given dataset = ' + str(count_inversions(arr)[1])
            
            
    
    
        

