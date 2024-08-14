from Deque import Deque
import numpy as np

class ASC_IP_LRU:
    #改寫Deque 加上cache.size , cache.used
    class entry:
        def __init__(self,ID,size):
            self.ID=ID
            self.size=size
            self.mru_tag=False
            self.hit_tag=False


    def __init__(self,cache_size,c,delta):
        self.cache=Deque(cache_size)#用來記錄cache.size
        self.history=Deque(cache_size)

        self.c=c
        self.delta=delta

        self.DEBUG_reqCount=0
        self.DEBUG_HitCount=0
        self.DEBUG_MRU=0
        self.DEBUG_LRU=0
        self.DEBUG_evictCount=0
        self.DEBUG_c_up=0
        self.DEBUG_c_down=0


    def DEBUG(self):
        hit_rate=round(100*self.DEBUG_HitCount/self.DEBUG_reqCount,2)
        s="  cache-used:  "+str(self.cache.used)\
            +"  req_num:  "+str(self.DEBUG_reqCount)\
            +"  hit_num:  "+str(self.DEBUG_HitCount)\
            +"  hit_rate:  "+str(hit_rate)\
            +"  evictCount:  "+str(self.DEBUG_evictCount)\
            +"  insert_MRU:  "+str(self.DEBUG_MRU)\
            +"  insert_LRU:  "+str(self.DEBUG_LRU)\
            +"  c:  "+str(self.c)\
            +"  c_up:  "+str(self.DEBUG_c_up)\
            +"  c_down:  "+str(self.DEBUG_c_down)

        return s




    def evict(self):
        return self.cache.popLast()
    
    def request(self,ID,size):
        self.DEBUG_reqCount+=1
        cache=self.cache
        H=self.history
        O_i=cache[ID] if ID in cache else self.entry(ID,size)


        if not (O_i.ID in cache):
            while(cache.size<O_i.size+cache.used):
                O_e=self.evict()
                self.DEBUG_evictCount+=1
                if O_e.mru_tag==True:
                    if O_e.hit_tag==False:
                        # self.c=self.c-self.delta 若不做限制 c小於會全部准入
                        self.c=max(self.c-self.delta , 100)
                        self.DEBUG_c_down+=1
                else:
                    if (O_e.hit_tag==False) and (O_e.ID in H):
                        self.c=self.c+self.delta
                        self.DEBUG_c_up+=1
                
                
                if O_e.ID in H:
                    del H[O_e.ID]
                while(H.size<O_e.size+H.used):#如果H滿了則清空間
                    H.popLast()
                H[O_e.ID]=O_e

            p=np.exp(-O_i.size/self.c)
            r=np.random.rand()
            if O_i.size>=self.c and p<=r:
                self.DEBUG_LRU+=1
                O_i.mru_tag=False
                O_i.hit_tag=False
                cache.pushLast(O_i)#LRU position
            else:
                self.DEBUG_MRU+=1
                O_i.mru_tag=True
                O_i.hit_tag=False
                cache.pushFirst(O_i)#MRU position
        else: #hit
            self.DEBUG_HitCount+=1
            O_i.hit_tag=True
            cache[O_i.ID]=O_i
            if O_i.ID in H:
                del H[O_i.ID]
        # if O_i.ID in H:#會導致H O_e.ID in H永遠是false   改到
        #     del H[O_i.ID]


