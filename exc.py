from pickle import TRUE
import unittest
import csv
from unittest import result


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


def open_file(name):
    file = open('F:/Program/Python/Jadi/Basic/ex2/%s.csv' %name)
    csvreader = csv.reader(file)
    rows = []
    for row in csvreader:
        rows.append(row)
    
    trans_lst = []
    result = rows.pop(0)[0]
    for i in rows:
        transaction = Transaction(type=i[0],time =i[2],value=int(i[1]))
        if transaction.type == 'WIT':
            transaction.status = i[3]
        trans_lst.append(transaction)

    return result,trans_lst

class Test(unittest.TestCase):  

    def test_fun1(self):
        result,lst = open_file('1')
        self.assertEqual(account_calculator(lst),result)

    def test_fun2(self):
        result,lst = open_file('2')
        self.assertEqual(account_calculator(lst),result)

    def test_fun3(self):
        result,lst = open_file('3')
        self.assertEqual(account_calculator(lst),result)

    def test_fun4(self):
        result,lst = open_file('4')
        self.assertEqual(account_calculator(lst),result)

    def test_fun5(self):
        result,lst = open_file('5')
        self.assertEqual(account_calculator(lst),result)

    def test_fun6(self):
        result,lst = open_file('6')
        self.assertEqual(account_calculator(lst),result)

    def test_fun7(self):
        result,lst = open_file('7')
        self.assertEqual(account_calculator(lst),result)

    def test_fun8(self):
        result,lst = open_file('8')
        self.assertEqual(account_calculator(lst),result)

    def test_fun9(self):
        result,lst = open_file('9')
        self.assertEqual(account_calculator(lst),result)

    def test_fun10(self):
        result,lst = open_file('10')
        self.assertEqual(account_calculator(lst),result)

    def test_fun11(self):
        result,lst = open_file('11')
        self.assertEqual(account_calculator(lst),result)

    def test_fun12(self):
        result,lst = open_file('12')
        self.assertEqual(account_calculator(lst),result)

    def test_fun13(self):
        result,lst = open_file('13')
        self.assertEqual(account_calculator(lst),result)

    def test_fun14(self):
        result,lst = open_file('14')
        self.assertEqual(account_calculator(lst),result)

    def test_fun15(self):
        result,lst = open_file('15')
        self.assertEqual(account_calculator(lst),result)

    def test_fun16(self):
        result,lst = open_file('16')
        self.assertEqual(account_calculator(lst),result)

    def test_fun17(self):
        result,lst = open_file('17')
        self.assertEqual(account_calculator(lst),result)

    def test_fun18(self):
        result,lst = open_file('18')
        self.assertEqual(account_calculator(lst),result)

    def test_fun19(self):
        result,lst = open_file('19')
        self.assertEqual(account_calculator(lst),result)

    def test_fun20(self):
        result,lst = open_file('20')
        self.assertEqual(account_calculator(lst),result)

    def test_fun21(self):
        result,lst = open_file('21')
        self.assertEqual(account_calculator(lst),result)


if __name__ == '__main__':
    unittest.main()