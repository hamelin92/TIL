# 0. 출처

https://mangkyu.tistory.com/90

# 2. 알고리즘

## 버블 정렬

버블소트는 서로 인접한 두 원소를 비교하여 정렬하는 알고리즘입니다. 0번 인덱스부터 n-1번 인덱스까지 n번까지의 모든 인덱스를 비교하며 정렬합니다. 시간복잡도는 $O(n^2)$ 입니다.

![https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcqNUzB%2FbtqITvdyGGF%2Fwu13gRsZ8myIkDlk0WAmx0%2Fimg.png](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcqNUzB%2FbtqITvdyGGF%2Fwu13gRsZ8myIkDlk0WAmx0%2Fimg.png)

## 힙 정렬

힙소트는 주어진 데이터를 힙 자료구조로 만들어 최대값 또는 최소값부터 하나씩 꺼내서 정렬하는 알고리즘입니다. 힙소트가 가장 유용한 경우는 전체를 정렬하는 것이 아니라 가장 큰 값 몇개만을 필요로 하는 경우입니다. 시간복잡도는 $O(nlog_2n)$ 입니다.

![  ](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FPgySh%2FbtqITur6oYn%2FhLYHRVgkKimBNG6rwd5Q6k%2Fimg.png)

## 머지 정렬

머지소트는 주어진 배열을 크기가 1인 배열로 분할하고 합병하면서 정렬을 진행하는 분할/정복 알고리즘입니다. 시간복잡도는 $O(nlog_2n)$ 입니다.

![ ](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FMaPX2%2FbtqIWS0GAuO%2FigmIkXQjYxm5ObNcVaSp71%2Fimg.png)

## 퀵 소트

퀵소트는 매우 빠른 정렬 속도를 자랑하는 분할 정복 알고리즘 중 하나로 합병정렬과 달리 리스트를 비균등하게 분할합니다. 피봇을 설정하고 피봇보다 큰값과 작은값으로 분할하여 정렬을 합니다. 시간복잡도는 $O(nlog_2n)$ 이며 리스트가 계속해서 불균등하게 나눠지는 경우 시간복잡도가 $O(n^2)$까지 나빠질 수 있습니다.

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