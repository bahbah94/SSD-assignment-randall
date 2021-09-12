import logging,time,inspect,contextlib,io
import pandas as pd

class decorator_3:
    global dict,res
    res = []
    dict = {}
    def __init__(self,func):
        #global dict
        #dict ={}
        self.func = func
        self.count = 0


    def __call__(self,*args,**kwargs):

        def Sort_sub(sub_lst):
            sub_lst.sort(key=lambda x: x[1])
            return sub_lst

        def insert_second(lst,i):
            lst.insert(1,i)
            return lst

        self.count += 1
        start = time.perf_counter()
        with contextlib.redirect_stdout(io.StringIO()) as f:
            self.func(*args,**kwargs)
        end = time.perf_counter()
        s = f.getvalue()
        if self.func.__name__ in dict:
            return
        else:
            dict[self.func.__name__] = end

        if len(dict) == 4:
            res = [[k,v] for k,v in dict.items()]
            final = Sort_sub(res)
            rank = [insert_second(j,i+1) for i,j in enumerate(res)]
            df = pd.DataFrame(rank,columns=["functionName", "Rank","Time"])
            print(df)




        #print(f"{self.func.__name__} call {decorator_4.count} executed in {end} seconds",file=f1)
        with open("output.txt", "a") as f:
            print(f"{self.func.__name__} call {self.count} executed in {end} seconds",file=f)
            print("Name:    ", self.func.__name__,file=f)
            print("Type:    ",type(self.func),file=f)
            print("Sign:    ",inspect.signature(self.func),file=f)
            print("Args:",end="    " ,file=f)
            print("Positional: ",locals()['args'],file=f)
            print("         key-worded:  ",locals()['kwargs'],file=f)
            print("Doc:     ",inspect.getdoc(self.func),file=f)
            print("Source:      ",inspect.getsource(self.func),file=f)
            print("Output:  ",self.func(*args,**kwargs),file=f)
