import time
import os
import sys
import quick_str
import merge_str

sys.setrecursionlimit(21000)

def run_merge_sort(path):
    START = time.clock()
    DATA = [line.rstrip('\n') for line in open(os.path.join("data", path))]
    DATA = merge_str.merge_sort(DATA)
    END = time.clock()
    save_result(DATA, os.path.join("output-merge", path))
    return END - START

def run_quick_sort(path):
    START = time.clock()
    DATA = [line.rstrip('\n') for line in open(os.path.join("data", path))]
    quick_str.quick_sort(DATA, 0, len(DATA)-1)
    END = time.clock()
    save_result(DATA, os.path.join("output-quick", path))
    return END - START

def save_result(DATA, path):
    file = open(path, 'w')
    for item in DATA:
        file.write("%s\n" % item)
    file.close()

dirs = os.listdir('.\data')
dirs.sort(key=lambda f: int(filter(str.isdigit, f)))

for dir in dirs:
    print "=== Merge Sort [", dir, "] ==="
    print "Best: ", run_merge_sort(os.path.join(dir, "az.txt"))
    print "Average: ", run_merge_sort(os.path.join(dir, "rnd.txt"))
    print "Worst: ", run_merge_sort(os.path.join(dir, "za.txt"))
    print "=== Quick Sort [", dir, "] ==="
    print "Best: ", run_quick_sort(os.path.join(dir, "az.txt"))
    print "Average: ", run_quick_sort(os.path.join(dir, "rnd.txt"))
    print "Worst: ", run_quick_sort(os.path.join(dir, "za.txt"))
    print "=============================="
