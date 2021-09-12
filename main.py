import sys
import time,os
import pandas as pd

def Sort_sub(sub_lst):
    sub_lst.sort(key=lambda x: x[1])
    return sub_lst

def insert_second(lst,i):
    lst.insert(1,i)
    return lst

other = sys.argv[1:]
res = []
for script in other:


        with open(script) as f:
            start = time.time()
            exec(f.read())
            end = time.time()

        res.append([script,end-start])
final = Sort_sub(res)
rank = [insert_second(j,i+1) for i,j in enumerate(res)]
df = pd.DataFrame(rank,columns=["scriptName", "Rank","Time"])
print(df)
