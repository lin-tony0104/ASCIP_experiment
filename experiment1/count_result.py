A={}



#50GB       429,496,729,600 bit
result1=[36127642,10519048,26831483,9296159,1222889,141967204,2589041982,55940007,363030080,2312039099,37350531,2800000000,2589041982] 

#51.2GB     439,804,651,110 bit
result2=[] 

#25.6GB     219,902,325,555 bit
result3= []

#5.12GB     43,980,465,111 bit
result4=[] 

#2.56GB     21,990,232,555 bit
result5=[37468231,4229546,33292103,4176128,53418,758086660,1856681401,158140055,1347593663,1109034343,37521649,2800000000,1856681401] 

keys=["noReuseObj","ReuseObj","strict_noReuseObj","AlternatedObj","strict_ReuseObj","R_noReuseObj","R_ReuseObj","R_strict_noReuseObj","R_AlternatedObj","R_strict_ReuseObj","DistObj","ReqCount","HitCount"]
for r,k in zip(result5,keys):
    A[k]=r


for key1,value1 in A.items():
    for key2,value2 in A.items():
        print(key1," / ",key2," : ",(value1/value2))
print(A["DistObj"])

