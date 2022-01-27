#class Person:
#
#    def __init__(self, age):
#        self._age = age
#
#    @property
#    def age(self):
#        return self._age + 10
#
#    @age.setter
#    def age(self, new_age):
#        self._age = new_age * 10
#
#jun = Person(10)
#
#jun.age = 11
#
#print(jun.age)
#
#import random
#
#print(random.sample([1, 2, 3, 4, 5],4 ))

class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

        
        
class Rectangle:
    
    def __init__(self, p_1, p_2):
        self.p_1 = p_1
        self.p_2 = p_2
    
    def get_area(self):
        garo = self.p_2.x - self.p_1.x
        sero = self.p_1.y - self.p_2.y
        return garo * sero
    
    def get_perimeter(self):
        garo = self.p_2.x - self.p_1.x
        sero = self.p_1.y - self.p_2.y
        return 2 * (garo + sero)
    
    def is_square(self):
        garo = self.p_2.x - self.p_1.x
        sero = self.p_1.y - self.p_2.y
        if garo == sero:
            return True
        else:
            return False


p1 = Point(1, 3)
p2 = Point(3, 1)
r1 = Rectangle(p1, p2)
print(r1.get_area())
print(r1.get_perimeter())
print(r1.is_square())
p3 = Point(3, 7)
p4 = Point(6, 4)
r2 = Rectangle(p3, p4)
print(r2.get_area())
print(r2.get_perimeter())
print(r2.is_square())

class Circle:
    pi = 3.14
    
    def __init__(self,r, x, y):
        self.r = r
        self.x = x
        self.y = y
        
    def area(self):
        return self.pi * self.r * self.r

    def circumference(self):
        return 2*self.pi *self.r
    
    def center(self):
        return (self.x, self.y)

c1 = Circle(3,2,4)

print(c1.area())
print(c1.circumference())

class Animal:
    def __init__(self, name):
        self.name = name
        

    def walk(self):
        print(f'{self.name}! 걷는다!')
        

    def eat(self):
        print(f'{self.name}! 먹는다!')

class Dog(Animal):

    def __init__(self, name):
        super().__init__(name)
    
    def walk(self):
        print(f'{self.name}! 달린다!')
    
    def bark(self):
        print(f'{self.name}! 짖는다!')

class Bird(Animal):

    def __init__(self, name):
        super().__init__(name)

    def fly(self):
        print(f'{self.name}! 푸드덕!')

dog = Dog('멍멍이')
dog.walk() # 멍멍이! 달린다!
dog.bark() # 멍멍이! 짖는다!

bird = Bird('구구')
bird.walk() # 구구! 걷는다!
bird.eat() # 구구! 먹는다!
bird.fly() # 구구! 푸드덕!

import random

class Pokemon:
    
    species = 'Pikachu'
    
    def __init__(self, name , level):
        self.name = name
        self.level = level
        h = self.level * 20
        self.hp = h
        self.exp = 0
        
    def poke_center(self):
        self.hp = self.level*20
        
    def bark(self):
        print(f'{self.name}: pikachu!')
    
    def body_attack(self, other):
        other.hp -=  self.level * 5
        print(f'{self.name}의 몸통박치기!')
        print(f'{other.name}에게 {self.level*5}의 대미지!')
        
    def thousand_volt(self, other):
        other.hp -= self.level * 7
        print(f'{self.name}의 10만볼트!')
        print(f'{other.name}에게 {self.level*7}의 대미지!')
        
    def get_status(self):
        status = 'live' if self.hp > 0 else 'dead'
        print(f'이름: {self.name}, 레벨: {self.level}, 체력 : {self.hp}, 경험치: {self.exp}, 상태: {status}')
    
    def battle(self, other):
        count = 1
        while self.hp*other.hp > 0:
            attacker = random.sample([0, 1], 1)
            if 0 in attacker:
                print(f'{count}번째 턴, {self.name}의 공격 차례')
                move = random.sample([0, 2], 1)
                if move == [0]:
                    self.body_attack(other)
                elif move == [1]:
                    self.thousand_volt(other)
                else:
                    self.bark()
            else:
                print(f'{count}번째 턴, {other.name}의 공격 차례')
                move = random.sample([0, 1], 1)
                if move == [0]:
                    other.body_attack(self)
                else:
                    other.thousand_volt(self)
            count += 1
            
        if self.hp >0:
            self.exp += 15
            print(f'{self.name}는 {other.name} 상대로 전투에서 승리하여 경험치 15를 얻었다!')
            print(f'{other.name}는 {self.name} 상대로 행동불능이 되어 전투에서 패배했다!')
            if self.exp >= 100 and self.level <100:
                self.level += 1
                print(f'{self.name}, {self.level}로 레벨업!')
                self.exp = 0
        else:
            other.exp += 15
            print(f'{other.name}는 {self.name} 상대로 전투에서 승리하여 경험치 15를 얻었다!')
            print(f'{self.name}는 {other.name} 상대로 행동불능이 되어 전투에서 패배했다!')
            if other.exp >= 100 and other.level <100:
                other.level += 1
                print(f'{other.name}, {other.level}로 레벨업!')
                other.exp = 0