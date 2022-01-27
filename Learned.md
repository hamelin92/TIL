[toc]





# Learned

## Python

### 1. 

### No. 객체 지향 프로그래밍 OOP

- 객체object 는 특정 타입의 인스턴스(instance)(사례) 이다.
- 타입(type) : 어떤 연산자와 조작이 가능한가?
- 속성(attribute) : 어떤 상태(데이터)를 가지는 가?
- 조작법(method) : 어떤 행위(함수)를 할 수 있는 가?
- 절차지향 프로그래밍 -> 객체지향 프로그래밍

####  Subno. OOP 기초

- 클래스 정의  class Myclass:
- 인스턴스 생성 my_instance = MyCalss()
- 메소드 호출 my_instance.my_method()
- 속성 my_instance.my_attribute
- 클래스 : 객체들의 분류
- 인스턴스 : 하나하나의 실체/예
- 속성 : 특정 데이터 타입/클래스의 객체들이 가지게 될 상태/ 데이터를 의미
- 메소드 : 특정 데이터 타입/클래스의 객체에 공통적으로 적용 가능한 행위(함수)
- 객체 비교하기
  -  == 동등한 / 변수가 참조하는 객체가 동등한(내용이 같은) 경우 True
  -  is 동일한 / 두 변수가 동일한 객체를 가리키는 경우 True



#### 인스턴스

- 인스턴수 변수

  - 인스턴스가 개인적으로 가지고 있는 속성
  - 각 인스턴스들의 고유한 변수

- 생성자 메소드에서 self.<name>으로 정의

- 인스턴스가 생성된 이후 <instance>.<name> 으로 접근 및 할당

- 인스턴스 메소드

  - 인스턴스 변수를 사용하거나, 인스턴스 변수에 값을 설정하는 메소드
  - 클래스 내부에 정의되는 메소드의 기본
  - 호출 시, 첫번째 인자로 인스턴스 자기자신(self)이 전달됨

- self

  - 인스턴스 자기자신
  - 파이썬에서 인스턴스 메소드는 호출 시 첫번째 인자로 인스턴스 자신이 전달되게 설계
  - 매개변수 이름으로 self를 첫번째 인자로 정의
  - 다른 단어로 써도 작동하지만, 파이썬의 암묵적인 규칙

- 생성자 메소드

  - 인스턴스 객체가 생성될 때 자동으로 호출되는 메소드

  - 인스턴스 변수들의 초깃값을 설정

    - 인스턴스 생성

    - \__init__ 메소드 자동 호출

    - ```python
      class Person:
          
          def __init__(self):
              print('인스턴스 생성')
      ```

    - ```python
      person1 = person()
      #인스턴스 생성
      ```

    - ```python
      class Person:
          
          def __init__(self, name):
              print(f'인스턴스 생성. {name}')
      person1 = Person('지민')
      #인스턴스 생성. 지민
      ```

- 소멸자(destructor) 메소드

  - 인스턴스 객체가 소멸(파괴)되기 직전에 호출되는 메소드

  - ```python
    class Person:
        
        def __del__(self):
            print('인스턴스가 사라졌습니다.')
    person1 = Person()
    del person1
    #인스턴스가 사라졌습니다.
    ```

- 매직 메소드

  - Double underscore(__) 가 있는 메소드는 특수한 동작을 위해 만들어진 메소드로, 

  - 스페셜 메소드 혹은 매직 메소드로 불림. / 특정상황에 자동으로 불리는 메소드

  - ```python
    __str__(self), __len(self)__, __repr__(self)
    __lt__(self, other), __le__(self, other), __eq__(self, other)
    __gt__(self, other), __ge__(self, other), __ne__(self, other) ...
    ```

  - 객체의 특수 조작 행위를 지정(함수, 연산자 등)

    - \__str__ : 해당 객체의 출력 형태를 지정

      - 프린트 함수를 호출할 때, 자동으로 호출
      - 어떤 인스턴스를 출력하면 \__str__의 return 값이 출력
      - \__gt__ : 부등호 연산자(> , greater than)

    - ```python
      class Circle:
          
          def __init__(self, r):
              self.r = r
              
          def area(self):
              return 3.14 * self.r * self.r
      	
          def __str__(self):
              return f'[원] radius : {self.r}'
          
          def __gt__(self, other):
              return self.r > other.r
      ```

      ```python
      c1 = Circle(10)
      c2 = Circle(1)
      print(c1) # [원] radius : 10
      print(c2) # [원] radius : 1
      c1 > c2 #True
      c1 < c2 #False
      ```

#### 클래스

- 클래스 변수 : 한 클래스의 모든 인스턴스라도 똑같은 값을 가지고 있는 속성

  - 클래스 이름 대신 인스턴스 이름을 쓰면 인스턴스 변수

- 클래스 선언 내부에서 정의, <classname>.<name>으로 접근 및 할당

- 클래스 메소드

  - 클래스가 사용할 메소드

  - @classmethod 데코레이터를 사용하여 정의

    - 데코레이터 : 함수를 어떤 함수로 꾸며서 새로운 기능을 부여

  - 호출 시, 첫번째 인자로 클래스(cls)가 전달됨

  - ```python
    class MyClass:
        
        @classmethod
        def class_method(cls, arg1, ...):
    MyClass.class_method(...)
    ```

- 스태틱 메소드

  - 스태틱메소드 : 인스턴스 변수, 클래스 변수를 전혀 다루지 않는 메소드

  - 언제? 속성을 다루지 않고 기능만을 하는 메소드를 정의할 때 사용.

  - 클래스가 사용할 메소드, @staticmethod 데코레이터를 사용하여 정의

  - 호출 시 어떠한 인자도 전달되지 않음 ( 클래스 정보에 접근/ 수정 불가)

  - ```python
    class MyClass:
        
        @staticmethod
        def class_method(arg1, ...):
    MyClass.static_method(...)
    ```

- 인스턴스와 클래스 간의 이름 공간(namespace)

  - 클래스를 정의하면, 클래스와 해당하는 이름 공간 생성
  - 인스턴스를 만들면, 인스턴스 객체가 생성되고 이름 공간 생성
  - 인스턴스에서 특정 속성에 접근하면, 인스턴스-클래스 순으로 탐색
  - 

#### 메소드

### No. 객체지향의 핵심개념

#### 추상화

#### 상속

#### 다형성

#### 캡슐화

