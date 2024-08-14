from LRU import LRU
from ASC_IP_LRU import ASC_IP_LRU







#LRU
def run_LRU():
    
    DEBUG_reqCount=0
    trace="D:/all_Trace/ASC-IP/wiki2018.tr"
    # cache_size=2748779069 # 512GB*0.005= 2.56GB 以Byte為單位
    cache_size=21990232555 # 以bit為單位
    policy=LRU(cache_size)
        
    with open(trace,'r') as f:
        for line in f:
            temp=line.split()
            ID=int(temp[1])
            size=int(temp[2])
            if size>cache_size:
                print("object bigger then cache!  used-cache:",policy.cache.used,"  obj_size:  ",size)

            policy.request(ID,size)
            DEBUG_reqCount+=1


            if not DEBUG_reqCount%1000000:
                s="exp4_LRU "\
                    +"  cache_size: "+str(cache_size)\
                    +"  req_num:  "+str(DEBUG_reqCount)\
                    +policy.DEBUG()
                print(s)

#=================================================
#ASCIP
def run_ASCIP():
    c=100
    delta=1000

    # cache_size=21990232555 #2.56GB  512GB*0.005 = 512 * 2^30 * 8 * 0.005
    # cache_size=43980465111 #5.12GB  512GB*0.01 = 512 * 2^30 * 8 * 0.01
    # cache_size=219902325555 #25.6GB 512GB*0.05 = 512 * 2^30 * 8 * 0.05
    cache_size=439804651110 #51.2GB 512GB*0.1 = 512 * 2^30 * 8 * 0.1
    
    
    DEBUG_reqCount=0
    trace="D:/all_Trace/ASC-IP/wiki2018.tr"
    # cache_size=2748779069 # 512GB*0.005= 2.56GB 以Byte為單位
    policy=ASC_IP_LRU(cache_size,c,delta)
    with open(trace,'r') as f:
        for line in f:
            temp=line.split()
            ID=int(temp[1])
            size=int(temp[2])
            if size>cache_size:
                print("object bigger then cache!  used-cache:",policy.cache.used,"  obj_size:  ",size)

            policy.request(ID,size)
            DEBUG_reqCount+=1


            if not DEBUG_reqCount%1000000:
                s="exp4_ASC-IP-LRU "\
                    +"  cache_size: "+str(cache_size)\
                    +"  req_num:  "+str(DEBUG_reqCount)\
                    +policy.DEBUG()
                print(s)

            # print(policy.DEBUG_HitCount)
            #第560000000個req結束後，重置reqCount,HitCount    
            if DEBUG_reqCount==560000000:
                policy.DEBUG_reqCount=0
                policy.DEBUG_HitCount=0           


if __name__=="__main__":
    # run_LRU()
    run_ASCIP()