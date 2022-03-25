
# https://quera.org/problemset/110019/

class Transaction:
    def __init__(self, type, time,value):
        self.type=type
        self.time=time
        self.value=value
        self.status=''

def account_calculator(trans_lst):
    trans_lst.sort(key=lambda x: x.time)  
    b_stack = []
    limit=0
    limited = False
    balance = 0

    for i in trans_lst:
        
        if i.type=='DEP':
            if balance < 0:
                b_stack.append(balance)
                balance = i.value
            else:
                balance += i.value
            if limited:
                limit += i.value
        elif i.type == 'WIT' and i.status == 'OK':
            balance -= i.value
            
            if limited:
                if i.value >= limit:
                    return 'DOROGHE'
                else:
                    limit -= i.value


        elif i.type == 'WIT' and i.status == 'FAIL' and balance >= i.value:
            return 'DOROGHE'
        else:
            if not limited:
                limited = True
                limit = i.value 
            elif limit > i.value:
                limit = i.value           
            

    if balance < 0:
        b_stack.append(balance)        

    
    s = sum(b_stack)
    if s>=0:
        return str(0)
    else:
        return str(s*-1)


trans_list=[]

n = int(input())
for i in range(n):
    input_str = (input().split(' '))
    transaction = Transaction(type=input_str[0],time =input_str[2],value=int(input_str[1]))
    if transaction.type == 'WIT':
        transaction.status = input_str[3]

    trans_list.append(transaction)
trans_list.sort(key=lambda x: x.time )

print(account_calculator(trans_list))