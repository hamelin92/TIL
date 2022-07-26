

# 0. 출처

https://mangkyu.tistory.com/89

# 2. 자료구조

## 자료구조와 알고리즘

자료구조는 데이터를 원하는 규칙 또는 목적에 맞게 저장하기 위한 구조이고, 알고리즘이란 자료구조에 쌓인 데이터를 활용해 어떠한 문제를 해결하기 위한 여러 동작들의 모임이다.



## 스택, 큐, 트리, 힙

- 스택: 선입후출 / **F**irst **I**n **L**ast **O**ut(후입선출 / **L**ast **I**n **F**irst **O**ut), 자료를 위로 쌓는 구조(세로로 위에서만 넣고 뺄 수 있는 통).
- 큐: 선입선출 / **F**irst **I**n **F**irst **O**ut, 자료를 줄 서듯이 쌓는 구조(가로로 양쪽이 뚫린 (일방통행) 통)
- 트리:  정점 node와 간선 edge로 이루어진 싸이클이 없는 그래프의 일종. 계층이 있는 데이터를 표현하기에 적합.
- 힙: 최댓값 혹은 최솟값을 찾아내는 연산을 쉽게 하기 위해 고안된 구조로 각 노드의 키값이 자식의 키값보다 작지 않거나(최대 힙) 크지 않은 (최소힙) 완전 이진 트리.

![F**irst **I**n **L**ast **O**ut](https://blog.kakaocdn.net/dn/bOP2BG/btqIXgehSAU/KVOz4pzZOwZqlH20wZsBC0/img.png)



## 우선 순위 큐와 내부 구조 및 시간 복잡도

- 우선순위 큐는 가장 우선 순위가 높은 데이터를 먼저 꺼내기 위해 고안된 자료구조이다. 우선순위 큐를 구현하기 위해서 일반적으로 힙을 사용하고, 힙은 완전 이진트리를 통해 구현되었기 때문에 시간복잡도는 O(logN)이다.



## 해시 테이블과 해시 테이블의 시간 복잡도

해시 테이블은 key, value로 데이터를 저장하는 자료구조 중 하나로 빠른 데이터 검색이 필요할 때 유용하다. 해시 테이블은 key 값에 해시함수를 적용해 고유한 index를 생성하여 그 index에 저장된 값을 꺼내오는 구조이다.

![https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fcmb93t%2FbtqITt7eR8A%2FmGgrbmF8XUo38BG1SiYLi1%2Fimg.png](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fcmb93t%2FbtqITt7eR8A%2FmGgrbmF8XUo38BG1SiYLi1%2Fimg.png)

해시 테이블은 고유한 index로 값을 조회하기 때문에 평균적으로 O(1)의 시간복잡도를 가진다. 하지만 해시의 index값이 충돌을 일으키는 경우 연결된 데이터들을 조회하여 원하는 값을 조회하기 때문에 O(N)까지 커질 수 있다.

참고: [[자료구조] 해시 테이블(Hash Table) 이란? | 해시 알고리즘 | 해시 함수](https://code-lab1.tistory.com/14?category=1213002)



## LinkedList 연결리스트와 ArrayList 차이

ArrayList는 데이터들이 순서대로 늘어선 배열의 형식을 취하고 있지만, LinkedList는 자료의 주소값으로 서로 연결된 형식을 가지고 있다. 이러한 구조에 의해 둘은 각각의 장단점이 있다.

- ArrayList
  
  - 원하는 데이터에 무작위로 접근 가능
  
  - 리스트의 크기가 제한되어 있으며, 리스트의 크기를 재조정하는 것은 많은 연산 필요
  
  - 데이터의 추가/삭제를 위해서 임시 배열을 생성하여 복제하고 있어 시간이 걸림

- LinkedList
  
  - 리스트의 크기에 영향없이 데이터를 추가할 수 있다.
  
  - 데이터를 추가할 때 새로운 노드를 생성하여 연결하기 떄문에 추가/삭제 연산 빠름
  
  - 무작위 접근이 불가능



## 큐와 스택의 구현

- 큐(Queue): Array로 구현하면 dequeue 연산 이후 객체를 앞당기는 작업이 필요하다. 하지만 LinkedList로 구현하면 객체 1개만 제거하면 되므로 삽입 삭제가 용이한 LinkedList로 구현하는 것이 좋다.

- 스택(Stack): LinkedList로 구현하면 객체를 제거하는 작업이 필요하다. 하지만 ArrayList로 구현하면 삭제할 필요 없이 index를 줄이고 초기화만 하면 되므로, ArrayList로 구현하는 것이 좋다.



# 2. 자료구조 - 고급



## AVL 트리

AVL트리란 한 쪽으로 값이 치우치는 이진 균형트리(Balanced Search Tree, BST)의 한계점을 보완하기 위해 만들어진 균형 잡힌 이진 트리이다. AVL은 항상 좌/우로 데이터를 균형잡힌 상태로 유지하기 위해 추가 연산을 진행한다.

참고: [[자료구조] AVL트리란? AVL트리 쉽게 이해하기, AVL트리 시뮬레이터](https://code-lab1.tistory.com/61)



## 레드블랙 트리

레드블랙 트리는 모든 노드를 빨간색 또는 검은색으로 칠하고 연결된 노드들은 색이 중복되지 않도록 관리한다. 

참고: [[자료구조] 레드-블랙 트리(Red-Black Tree)란? | 레드-블랙 트리 쉽게 이해하기](https://code-lab1.tistory.com/62)