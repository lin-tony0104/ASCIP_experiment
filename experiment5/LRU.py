from Deque import Deque

class LRU:
    #改寫Deque 加上cache.size , cache.used
    class entry:
        def __init__(self,ID,size):
            self.ID=ID
            self.size=size
            self.hit_tag=False
 

    def __init__(self,cache_size):
        self.cache=Deque(cache_size)#用來記錄cache.size
        
        
        self.DEBUG_reqCount=0
        self.DEBUG_HitCount=0

    def addToCache(self,obj):
        self.cache.pushFirst(obj)

    def evict(self):
        return self.cache.popLast()
    

    def request(self,ID,size):
        self.DEBUG_reqCount+=1

        cache=self.cache #為了讓名字看起來短一點

        # obj=self.entry(ID,size)

        if ID in cache: #hit
            obj=cache[ID]#沿用舊的entry
            obj.hit_tag=True
            cache[ID]=obj #更新到MRU位置

            self.DEBUG_HitCount+=1
        else:#miss
            obj=self.entry(ID,size)
            while(obj.size+cache.used>cache.size):
                victim=self.evict()
            self.addToCache(obj)

    def DEBUG(self):
        hit_rate=round(100*self.DEBUG_HitCount/self.DEBUG_reqCount,2)
        s="  lru_req_num:  "+str(self.DEBUG_reqCount)\
            +"  lru_hit_num:  "+str(self.DEBUG_HitCount)\
            +"  hit_rate:  "+str(hit_rate)
        return s







