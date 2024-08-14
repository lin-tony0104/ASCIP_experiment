from collections import defaultdict
from Deque import Deque

class LRU:
    #改寫Deque 加上cache.size , cache.used
    class entry:
        def __init__(self,ID,size):
            self.ID=ID
            self.size=size
            self.hit_tag=False
 

    def __init__(self,cache_size):
        self.cache=Deque(cache_size)
        
        
        self.DEBUG_reqCount=0
        self.DEBUG_ReuseList=[]
        self.DEBUG_NoReuseList=[]
        
        #DEBUG
        self.HitCount=0
        self.ReusedObj_Counter=defaultdict(int)#發生過重用
        self.noReuseObj_Counter=defaultdict(int)#發生過未重用
        
    def DEBUG(self):
        #用兩個list 整理出資料

        temp=defaultdict(int)   #為了加快速度
        for id in self.DEBUG_ReuseList:
            temp[id]+=1
        for id,count in temp.items():
            self.ReusedObj_Counter[id]+=count

        temp=defaultdict(int)   #為了加快速度
        for id in self.DEBUG_NoReuseList:
            temp[id]+=1
        for id,count in temp.items():
            self.noReuseObj_Counter[id]+=count       

        

        #R:表示重複 、 strict:表示嚴格reuse,嚴格noreuse
        noReuseObj=len(self.noReuseObj_Counter.keys())                  #A U B
        ReuseObj=len(self.ReusedObj_Counter.keys())                     #B U C
        A=self.noReuseObj_Counter.keys()-self.ReusedObj_Counter.keys()
        B=self.noReuseObj_Counter.keys()&self.ReusedObj_Counter.keys()
        C=self.ReusedObj_Counter.keys()-self.noReuseObj_Counter.keys()
        strict_noReuseObj=len(A)             #從未reuse      A
        AlternatedObj=len(B)                  #都有發生過的   B
        strict_ReuseObj=len(C)               #必reuse        C    
        
        R_noReuseObj=sum(self.noReuseObj_Counter.values())          #A U B重複
        R_ReuseObj=sum(self.ReusedObj_Counter.values())             #B U C重複
        
        R_strict_noReuseObj=sum([self.noReuseObj_Counter[i] for i in A])                                                    #A重複
        R_AlternatedObj=sum([self.noReuseObj_Counter[i] for i in B])+sum([self.ReusedObj_Counter[i] for i in B])            #B重複
        R_strict_ReuseObj=sum([self.ReusedObj_Counter[i] for i in C])                                                       #C重複
        #|R_A|+|R_B|+|R_C|=req_num

        self.HitCount=sum(self.ReusedObj_Counter.values())
        hit_rate=round(100*self.HitCount/self.DEBUG_reqCount,2)
        
        
        
        #重置兩個list
        self.DEBUG_ReuseList=[]
        self.DEBUG_NoReuseList=[]       
        
        
        s="  cache: "+str(self.cache.used)\
        +"  hit: "+str(self.HitCount)\
        +"  hit_rate: "+str(hit_rate)\
        +"  noReuseObjNum: "+str(noReuseObj)\
        +"  ReuseObjNum: "+str(ReuseObj)\
        +"  strict_noReuseObjNum_A: "+str(strict_noReuseObj)\
        +"  AlternatedObjNum_B: "+str(AlternatedObj)\
        +"  strict_ReuseObjNum_C: "+str(strict_ReuseObj)\
        +"  R_noReuseObj: "+str(R_noReuseObj)\
        +"  R_ReuseObj: "+str(R_ReuseObj)\
        +"  R_strict_noReuseObj_A: "+str(R_strict_noReuseObj)\
        +"  R_AlternatedObj_B: "+str(R_AlternatedObj)\
        +"  R_strict_ReuseObj_C: "+str(R_strict_ReuseObj)
        
        return s

    def addToCache(self,obj):
        self.cache.pushFirst(obj)

    def evict(self):
        return self.cache.popLast()
    

    def request(self,ID,size):
        self.DEBUG_reqCount+=1

        cache=self.cache #為了讓名字看起來短一點

        

        if ID in self.cache: #hit
            obj=self.cache[ID]#沿用舊的entry
            obj.hit_tag=True
            self.cache[ID]=obj #更新到MRU位置
            self.DEBUG_ReuseList.append(obj.ID)#==========DEBUG
        else:#miss
            obj=self.entry(ID,size)
            while(obj.size+cache.used>cache.size):
                victim=self.evict()
                if not victim.hit_tag:
                    self.DEBUG_NoReuseList.append(victim.ID)#==========DEBUG 
            self.addToCache(obj)






    
if __name__=="__main__":
    lru=LRU()
    a=lru.entry(1,1)
    b=lru.entry(2,1)
    lru.cache.pushFirst(a)
    print("used:",lru.cache.used)
    lru.cache.pushFirst(b)
    print("used:",lru.cache.used)
    print(lru.cache.popLast().ID)
    print("used:",lru.cache.used)
    print(lru.cache.popLast().ID)
    print("used:",lru.cache.used)



