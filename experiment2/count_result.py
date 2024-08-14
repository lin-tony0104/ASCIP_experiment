A={}

A["noReuseObj"]=28946404
A["ReuseObj"]=4511927
A["strict_noReuseObj"]=24544433                 #A
A["AlternatedObj"]=4401971                     #B
A["strict_ReuseObj"]=109956                   #C

A["R_noReuseObj"]=303449169
A["R_ReuseObj"]=1220438747
A["R_strict_noReuseObj"]=81291891
A["R_AlternatedObj"]=638714757
A["R_strict_ReuseObj"]=803881268

A["DistObj"]=24544433+4401971+109956                    #DistObj=|A|+|B|+|C|
A["ReqCount"]=1621000000
A["HitCount"]=1220438747

for key1,value1 in A.items():
    for key2,value2 in A.items():
        print(key1," / ",key2," : ",(value1/value2))