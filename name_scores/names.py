#! python3

import time

start_time = time.time()

def value_name(name):
    mapper = {n:i+1 for (i,n) in enumerate(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))}
    return sum([mapper[x] for x in name])

def sort_names(names):
    # using quicksort
    if names == []:
        return []
    pivot = names[0]
    l = sort_names([x for x in names[1:] if x < pivot])
    u = sort_names([x for x in names[1:] if x >= pivot])
    return l + [pivot] + u

# opening the file and converting it into a list
name_handle = open("names.txt")
name_list = [name[1:-1] for name in name_handle.read().split(",")]

name_score = sum([i+1*value_name(x) for (i,x) in enumerate(sort_names(name_list))])

end_time = time.time()

print("Name score for the given file: %d" %name_score)
print("Time taken for computation: %0.5f seconds." %(end_time-start_time))
