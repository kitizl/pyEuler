#! python3
import time
start_time = time.time()


def collatz_loop(n):
    
    chain_size = 0
    
    while not n==1:
        if n%2 == 0:
            n = n/2
        else:
            n = 3*n + 1

        chain_size+=1
        
    chain_size += 1
    
    return chain_size

def iterator():
    col_size = 0
    col_num = 1

    for i in range(1,1000001):
        size = collatz_loop(i)
        if size>col_size:
            col_size = size
            col_num = i
    
    return [col_num,col_size]

result = iterator()
end_time = time.time()
print("Starting number : {} ; Number of chains : {}".format(result[0],result[1]))
print("Time taken to finish computation : %0.2f " %(-start_time+end_time))
