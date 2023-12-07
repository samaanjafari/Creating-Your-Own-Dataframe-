import pandas as pd
import random

df = pd.DataFrame()
count = 0
while count!=1000:
    wine = []
    fa = fixed_acidity = random.uniform(5,15.5)
    fa = '{:04.1f}'.format(fa)
    fa = float(fa)
    
    va = volatile_acidity = random.uniform(0.2,1)
    va = '{:04.2f}'.format(va)
    va = float(va)
    
    ca = critic_acid = 0
    
    rs = residual_sugar = random.uniform(1.5,3)
    rs = '{:03.1f}'.format(rs)
    rs = float(rs)
    
    ch = chlorides = random.uniform(0.070,0.1)
    ch = '{:5.3f}'.format(ch)
    ch = float(ch)
    
    fsd = free_sulfur_dioxide = random.randint(10,27)
    tsd = total_sulfur_dioxide = random.randint(35,75)
    
    dn = density = random.uniform(0.9900,0.9999)
    dn = '{:06.4f}'.format(dn)
    dn = float(dn)
    
    pH = random.uniform(3.15,3.6)
    pH = '{:04.2f}'.format(pH)
    pH = float(pH)
    
    sl  = sulfate = random.uniform(0.50,0.70)
    sl = '{:04.2f}'.format(sl)
    sl = float(sl)
    
    alc = alcohol = random.uniform(9.4,11)
    alc = '{:03.1f}'.format(alc)
    alc = float(alc)
    
    if fixed_acidity>=12 or pH<=3.2:
        quality = 6
        if alcohol>=10:
            quality = 7
    else:
        quality = 5
    
    wine = [[fa,va,ca,rs,ch,fsd,tsd,dn,pH,sl,alc,quality]]          
    
    wines = pd.DataFrame(wine,columns=['fixed acidity','volatile acidity','citric acid','residual sugar','chlorides','free sulfur dioxide','total sulfur dioxide','density','pH','sulfates','alcohol','quality'])
    df = pd.concat([df,wines])
    count += 1
       
df.to_csv('/Users/ASUS/Desktop/python/Data Science/ownwine.csv',index=False)    
df2 = pd.read_csv('/Users/ASUS/Desktop/python/Data Science/ownwine.csv' , sep = ',')    
print(df2.to_string(index=False))   