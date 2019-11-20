import sys
import time
import bisect

'''
https://www.cs.princeton.edu/~wayne/cs423/lectures/dynamic-programming-4up.pdf
have referred to this pdf for the pseudo code of Weighted-Activity-Selection
'''

'''
Load data from the given input Text File.
Input - Filename
Output - job_data (tuple with start time,finish time,weight)
'''
def load_job(filename):
    f = open(filename, "r")
    lines = f.readlines()
    job_data = []
    for x in lines:
        l = x.split()
        data = tuple(int(x) for x in l)
        if len(data)==3:
            job_data.append(data)
        else:
            print("Data read error")
    f.close()
    #return start_time,finish_time,weight
    return job_data

'''
Calculate the list of q1,q2,q3.....qn using binary search.
Input - job_data
Output - Q-list 
'''
def Compute_Q(job_data):
    finish_time = [i[1] for i in job_data]
    start_time = [j[0] for j in job_data]
    Q_list = []
    for k in range(len(job_data)):
        i = bisect.bisect_right(finish_time,start_time[k])
        Q_list.append(i)
    return Q_list
'''
Calculate the maximum weight subset of mutually compatible jobs.
Input - job_data
Output - Maximum Weight (Answer is stored at the end of the list)
'''
def Max_Profit_dynamic(job_data):
    p_interval = Compute_Q(job_data)
    n = len(job_data)
    Opt = [0 for i in range(n+1)]
    for j in range(1,len(job_data)+1):
        Opt[j] = max(job_data[j-1][2]+Opt[p_interval[j-1]],Opt[j-1])
    return Opt[-1]

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        raise Exception('Error: expected 1 command line argument')
    job_data = load_job(sys.argv[1])
    #sort the given data by finish time
    job_data.sort(key=lambda x: x[1])
    t1 = time.perf_counter()
    #Calculate Max Profit using dynamic programming
    ans = Max_Profit_dynamic(job_data)
    t2 = time.perf_counter()
    print("Time is ",t2-t1)
    print("Max profit is {}".format(ans))








