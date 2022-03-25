import random
import math

n = random.randint(0,10)

def roundup(x):
    return int(math.ceil(x / 100.0)) * 100


for i in range(n):
    b = random.randint(0,2)
    price = random.randint(1,2000)
    hour = random.randint(0,23)
    min = random.randint(0,59)
   
    if b==0:
        print('DEP,%s,%02d:%02d'%(roundup(price),hour,min))
    elif b==1:
        print('WIT,%s,%02d:%02d,OK'%(price,hour,min))
    elif b==2:
        print('WIT,%s,%02d:%02d,FAIL'%(price,hour,min))