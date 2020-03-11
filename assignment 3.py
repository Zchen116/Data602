import csv, json, math, pandas as pd, requests, unittest, uuid, io

def exercise01():
    def __init__(self, first_name, last_name, account_num, balance=0):
        self.first_name = first_name
        self.last_name = last_name
        self.account_num = account_num
        self.balance = balance
        self.transactions = []
    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(+amount)
        return amount
    def withdrawal(self, amount, limit=500):
        if self.balance - amount > 0 and amount <= limit:
            self.balance -= amount
            self.transactions.append(-amount)
            return amount
        else:
            return 'Your withdrawal amount is ${} which exceeds your account limit! You have:' \
                   '\n${}. Your withdrawal limit is {}'.format(amount, self.balance, limit)

def exercise02():
 class Box:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def get_length(self):
        return self.length
        
    def get_width(self):
        return self.width
    
    def render(self):
        print('*' * self.length)
        
        for i in range(self.width -2):
            print("*" + (' ' * (self.length -2)) + "*")
            
        print('*' * self.length)
        
    def invert(self):
        self.length, self.width = self.width, self.length
        
    def get_area(self):
        return self.length * self.width
            
    def get_perimeter(self):
        return 2*(self.length + self.width)
        
    def double(self):
        self.length = 2 * self.length
        self.width = 2 * self.width 
        return 
    
    def __eq__(self, other):
        """Override the default Equals behavior"""
        return self.length == other.length and self.width == other.width
    
    def print_dim(self):
        print(f"length = {self.length}")
        print(f"width = {self.width}")


    def get_dim(self):
        return (self.length, self.width)
        
 box = Box(6,5)
 box.render()
 box.invert()
 box.render()
 print(box.get_area())
 print(box.get_perimeter())
 box.double()
 box.render()
 box.print_dim()
 print(box.get_dim())


def exercise03():
    url = "https://raw.githubusercontent.com/Zchen116/assignments/master/avocado.csv"
    s = requests.get(url).content
    ds = pd.read_csv(io.StringIO(s.decode('utf-8')))
    print(ds.describe())


class TestAssignment3(unittest.TestCase):

    def test_exercise02(self):
        print('Testing exercise 2')
        b1, b2, b3 = exercise02()
        self.assertEqual(b1.get_length(),16)
        self.assertEqual(b1.get_width(),28)
        self.assertTrue(b1==Box(16,28))
        self.assertEqual(b2.get_length(),6)
        self.assertEqual(b2.get_width(),8)
        self.assertEqual(b3.get_length(),5)
        self.assertEqual(b2.get_hypot(),10)
        self.assertEqual(b1.double().get_length(),32)
        self.assertEqual(b1.double().get_width(),112)
        self.assertTrue(6 in b2.get_dim())
        self.assertTrue(8 in b2.get_dim())
        self.assertTrue(b2.combine(Box(1,1))==Box(7,9))

        
    def test_exercise03(self):
        print('Exercise 3 not tested')
        exercise03()
     

if __name__ == '__main__':
    unittest.main()
