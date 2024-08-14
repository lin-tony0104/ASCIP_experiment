from LRU import LRU
#DEBUG
DEBUG_reqCount=0

#cache_size 單位為 bit 。
cache_size=429496729600#50G = 50 * 2^30 *8 。  
# cache_size=21990232555 #2.56GB  512GB*0.005 = 512 * 2^30 * 8 * 0.005
# cache_size=43980465111 #5.12GB  512GB*0.01 = 512 * 2^30 * 8 * 0.01
# cache_size=219902325555 #25.6GB 512GB*0.05 = 512 * 2^30 * 8 * 0.05
# cache_size=439804651110 #51.2GB 512GB*0.1 = 512 * 2^30 * 8 * 0.1


trace="D:/all_Trace/ASC-IP/wiki2018.tr"

lru=LRU(cache_size)
with open(trace,'r') as f:
    for line in f:
        temp=line.split()
        ID=int(temp[1])
        size=int(temp[2])
        if size>cache_size:
            print("object bigger then cache!  used-cache:",lru.cache.used,"  obj_size:  ",size)
        
        
        lru.request(ID,size)
        DEBUG_reqCount+=1


        if not DEBUG_reqCount%1000000:
            s="LRU "\
                +"  cache_size: "+str(cache_size)\
                +"  req_num:  "+str(DEBUG_reqCount)\
                +lru.DEBUG()
            print(s)
            print()
        