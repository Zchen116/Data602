import math
import unittest
import numpy as np
import requests as r

def exercise01():
    animals = ['cat', 'dog', 'crouching tiger', 'hidden dragon', 'manta ray' ]
    return animals

def exercise02():
    animals = ['cat', 'dog', 'crouching tiger', 'hidden dragon', 'manta ray']
    len_animals = len(animals)
    for animal in range(0,len(animals)):
    
      print(animals[animal])
    print(len_animals)
    return animals, len_animals

def exercise03():
    countdown = [9, 8, 7, 5, 4, 2, 1, 6, 10, 3, 0, -5]
    the_fifth_element = -999

    countdown.sort()
    countdown.reverse()
    the_fifth_element = countdown[4]
    return countdown, the_fifth_element


def exercise04(more_temperatures, iot_sensor_points, a, b, c, d, e):
    temperatures = [9999,2,3,4,5,6,7,8,9,10,1,801,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]
    samples = [1,2,3,4,5,6,7,8,9,8000]
    copy_of_samples=[8000,66]
    a=8000
    b=8500
    c=9000
    d=9500
    e=9999
    return samples, temperatures, more_temperatures, iot_sensor_points, a, b, c, d, e, copy_of_samples

def exercise05(n):
    a = 1
    for i in range(1,n+1):
        a= a*i
    
    return a
    

def exercise06(n):
    length_n =len(n)
    sum_n = sum(n)
    average_n=sum_n/length_n
    return length_n, sum_n, average_n

def exercise07(n):
    
    if len(n)!=len(set(n)):
        return True
    else:
        return False


def exercise08(s):
    int_s = int(float(s))
    float_s = float(s)
    
    return int_s, float_s


def exercise09():
    dogs = []
    url = 'https://random.dog/woof.json'
    dog_media = r.get(url=url)
    print(str(dog_media.content))

    for n in range(0,12):
        dogs.append(str(dog_media.content))
        dog_media=r.get(url=url)
    return dogs



def exercise10(sentence):
    reversed = ''

    sentenceN = sentence.swapcase()
    rp = sentenceN.replace(' ','_')
    rp_seq = rp[::-1]
    
    reversed = rp_seq
    return reversed

class TestAssignment2(unittest.TestCase):
    def test_exercise01(self):
        print('Testing exercise 1')
        a = exercise01()
        self.assertEqual(len(a), 5)
        self.assertTrue('cat' in a)
        self.assertTrue('dog' in a)
        self.assertTrue('manta ray' in a)
    
    def test_exercise02(self):
        print('Testing exercise 2')
        a, l = exercise02()
        self.assertEqual(len(a), 5)
        self.assertEqual(l, 5)
        self.assertTrue('cat' in a)
        self.assertTrue('dog' in a)
        self.assertTrue('manta ray' in a)

    def test_exercise03(self):
        print('Testing exercise 3')
        c, tfe = exercise03()
        self.assertEqual(c[0], 10)
        self.assertEqual(c[11], -5)
        self.assertEqual(len(c), 12)
        self.assertEqual(tfe, 6)

    def test_exercise04(self):
        print('Testing exercise 4')
        more_temperatures = np.random.randint(300, 400, size=25)
        iot_sensor_points = {1: 801, 2: 644, 3: 991, 4: 721,
                             5: 752, 6: 871, 7: 991, 8: 1023, 9: 804, 10: 882}
        samples, temperatures, more_temperatures, iot_sensor_points, a, b, c, d, e, copy_of_samples = exercise04(more_temperatures, iot_sensor_points,
                                                                                                                 8000, 8500, 9000, 9500, 9999)

        self.assertEqual(len(temperatures), 50)
        self.assertEqual(len(samples), 10)
        self.assertEqual(temperatures[0], 9999)
        self.assertEqual(temperatures[11], 801)
        self.assertEqual(samples[9], 8000)
        self.assertEqual(copy_of_samples[0], 8000)
        self.assertEqual(a, 8000)
        self.assertEqual(b, 8500)
        self.assertEqual(c, 9000)
        self.assertEqual(d, 9500)
        self.assertEqual(e, 9999)

    def test_exercise05(self):
        print('Testing exercise 5')
        self.assertEqual(exercise05(5), 120)
        self.assertEqual(exercise05(10), 3628800)

    def test_exercise06(self):
        print('Testing exercise 6')
        length_n, sum_n, average_n = exercise06([1, 2, 3, 4, 5])
        self.assertEqual(average_n, 3)
        self.assertEqual(length_n, 5)
        length_n, sum_n, average_n = exercise06([1, 2, 120])
        self.assertEqual(average_n, 41)
        self.assertEqual(length_n, 3)

    def test_exercise07(self):
        print('Testing exercise 7')
        self.assertTrue(exercise07([1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == True)
        self.assertTrue(exercise07([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == False)
        self.assertTrue(exercise07([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10]) == True)
        self.assertTrue(exercise07([1, 2.00002, 2.00001, 4, 5, 6, 7, 8, 9, 10]) == False)
    
    def test_exercise09(self):
        print('Testing exercise 9')
        dogs = exercise09()
        for d in dogs:
            print(d)
        self.assertTrue('https://random.dog/' in d)
            

    def test_exercise10(self):
        print('Testing exercise 10')
        self.assertEqual(exercise10('HellO'),'oLLEh')
        self.assertEqual(exercise10('ThIs Is MaD'),'dAm_Si_SiHt')




if __name__ == '__main__':
    unittest.main()









    




    
