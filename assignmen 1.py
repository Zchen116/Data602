import math
import unittest

def exercise_example():
    y=5
    
    return y



def exercise01():
    x=5
    
    return x


def exercise02():
    name = str('ZhiYing')
    
    return name
 

def exercise03():
    sentence = str('I like apple.')
    return sentence


def exercise04():
    first_name = str('ZhiYing')
    last_name = str('Chen')
    return first_name, last_name
  

def exercise05():
    first_name = str('ZhiYing')
    last_name = str('Chen')
    name_type = type(first_name)
    return first_name, last_name ,name_type   



def exercise06():
    hours_worked = 20
    wage_per_hour = 15
    total_pay = hours_worked*wage_per_hour
    return hours_worked, wage_per_hour, total_pay
    


def exercise07():
    wage=17.0
    print(type(wage))
    doubled=2*float(wage)
    return wage, doubled


def exercise08():
    quantity = 5
    hello = 'hello'
    hello_repeated = str(hello)*quantity
    return quantity, hello, hello_repeated

def exercise09():
    qty = 10
    price = 5
    total_cost = qty*price

    return qty, price, total_cost


def exercise10():
    factor1 = 1
    factor2 = 2
    factor3 = 3
    factor4 = 4
    factor5 = 5
    product = factor1*factor2*factor3*factor4*factor5

    return factor1, factor2, factor3, factor4, factor5, product


def exercise11():
    pi=round(math.pi-0.00000000005,10)

    return pi

def exercise12():
    x =10
    y =x**7
    return x, y


def exercise13():
    pi = 3.14159
    r = 7
    volume_sphere = 4/3*pi*pow(r,3)

    return pi, r, volume_sphere


def exercise14():
    length = 50
    height = 10.2
    area = length*height
    area_type = type (area)
    return area, length, height, area_type


def exercise15():
    speed_mph = 80
    duration = 3
    distance = speed_mph*duration
    return distance, speed_mph, duration
    

def exercise16():
    a = 3
    b = 4
    c = math.sqrt(pow(a,2)+pow(b,2))

    return a, b, c


class TestAssignment1(unittest.TestCase):

    def test_exercise1(self):
        print('Testing exercise 1')
        self.assertEqual(exercise01(), 5)

    def test_exercise2(self):
        print('Testing exercise 2')
        self.assertTrue(isinstance(exercise02(), str))
        self.assertGreater(len(exercise02()), 1)

    def test_exercise3(self):
        print('Testing exercise 3')
        words = exercise03().split(' ')
        self.assertGreater(len(words), 2)

    def test_exercise4(self):
        print('Testing exercise 4')
        f, l = exercise04()
        self.assertTrue(isinstance(f, str))
        self.assertGreater(len(f), 0)
        self.assertTrue(isinstance(l, str))
        self.assertGreater(len(l), 0)

    def test_exercise5(self):
        print('Testing exercise 5')
        f, l, nt = exercise05()
        self.assertTrue(isinstance(f, str))
        self.assertGreater(len(f), 0)
        self.assertTrue(isinstance(l, str))
        self.assertGreater(len(l), 0)
        self.assertTrue(isinstance(nt, type))

    def test_exercise6(self):
        print('Testing exercise 6')
        h, w, p = exercise06()
        self.assertTrue(isinstance(h, int))
        self.assertTrue(isinstance(w, int))
        self.assertTrue(isinstance(p, int))
        self.assertEqual(h, p/w)

    def test_exercise7(self):
        print('Testing exercise 7')
        w, d = exercise07()
        self.assertTrue(isinstance(w, float))
        self.assertTrue(isinstance(d, float))
        self.assertEqual(w, 17.0)

    def test_exercise8(self):
        print('Testing exercise 8')
        q, h, hr = exercise08()
        self.assertTrue(isinstance(q, int))
        self.assertTrue(isinstance(h, str))
        self.assertTrue(isinstance(hr, str))
        self.assertEqual(hr, 'hellohellohellohellohello')

    def test_exercise9(self):
        print('Testing exercise 9')
        q, p, tc = exercise09()
        self.assertTrue(isinstance(q, int))
        self.assertTrue(isinstance(p, int))
        self.assertTrue(isinstance(tc, int))
        self.assertEqual(q, tc/p)

    def test_exercise10(self):
        print('Testing exercise 10')
        f1, f2, f3, f4, f5, p = exercise10()
        self.assertEqual(f1, 1)
        self.assertEqual(f2, 2)
        self.assertEqual(f3, 3)
        self.assertEqual(f4, 4)
        self.assertEqual(f5, 5)
        self.assertEqual(p, 120)

    def test_exercise11(self):
        print('Testing exercise 11')
        p = exercise11()
        self.assertEqual(p, 3.1415926535)

    def test_exercise12(self):
        print('Testing exercise 12')
        x, y = exercise12()
        self.assertEqual(x, 10)
        self.assertEqual(y, 10000000)

    def test_exercise13(self):
        print('Testing exercise 13')
        p, r, vs = exercise13()
        self.assertLess(vs, 1436.8)
        self.assertGreater(vs, 1436.7)
        self.assertEqual(r, 7)
        self.assertEqual(p, 3.14159)

    def test_exercise14(self):
        print('Testing exercise 14')
        a, l, h, at = exercise14()
        self.assertGreater(a, 509)
        self.assertLess(a, 510)
        self.assertEqual(l, 50)
        self.assertEqual(h, 10.2)
        self.assertTrue(isinstance(at, type))

    def test_exercise15(self):
        print('Testing exercise 15')
        di, s, du = exercise15()
        self.assertEqual(s, 80)
        self.assertEqual(du, 3)
        self.assertEqual(s, di / du)

    def test_exercise16(self):
        print('Not testing exercise 16')


if __name__ == '__main__':
    unittest.main()

