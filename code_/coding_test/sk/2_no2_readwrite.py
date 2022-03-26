def solution(arr, processes):
	from collections import deque
	def status(proces):
		if proces[0][0] == 'w':
			return 2
		elif proces[0][0] == 'r':
			return 1
		else:
			return 0
	answer = []
	processes = deque(processes)
	read_que = deque([])
	write_que = deque([])
	status = 0
	time = [0] *1001
	t = 1
	while processes or read_que or write_que:
		process = processes.popleft()
		process = process.split()
		time[int(process[1])] = [status(process), int(process[2]),]
		if status == 0 and not read_que and not write_que and int(process[1]) <= t:
			if process[0][0] == 'w':
				status = 2
				t += int(process[2])
				for i in range(int(process[3]), int(process[4])+1):
					arr[i] = process[5]
			else:
				status = 1
				t += int(process[2])
				read = ''
				for i in range(int(process[3]), int(process[4])+1):
					read += arr[i]
				answer.append(read)
		else:
			if process[0][0] == 'w':
				write_que.append(process)
			elif

	return answer
a = ['1', '2','3','2','1']
b = ''
for i in range(1,4):
	b += a[i]
print(b)


'''
["1","2","4","3","3","4","1","5"], ["read 1 3 1 2","read 2 6 4 7","write 4 3 3 5 2","read 5 2 2 5","write 6 1 3 3 9", "read 9 1 0 7"]
문제 설명
여러 프로세스가 다음 규칙에 따라 배열(arr) 하나에 접근하여 읽기(Read) 또는 쓰기(Write) 작업을 수행하려 합니다.

2번 문제 제한사항에 다음 내용이 추가되었습니다.
processes는 t1기준으로 정렬되어 있습니다.

한 번에 여러 프로세스가 배열에서 동시에 읽기 작업을 수행할 수 있습니다.
배열에 읽기 작업을 수행 중인 경우, 새로운 읽기 요청 프로세스는 즉시 작업을 수행할 수 있습니다.
한 번에 하나의 프로세스만 배열에서 쓰기 작업을 수행할 수 있습니다.
배열에 쓰기 작업을 수행 중인 경우, 새로운 읽기, 쓰기 요청 프로세스는 모두 대기해야 합니다.
배열에 읽기 작업을 수행 중인 경우, 새로운 쓰기 요청 프로세스는 모두 대기해야 합니다.
하나 이상의 쓰기 작업이 대기 중인 경우, 새로운 읽기 요청 또한 대기해야 합니다.
대기 중인 읽기, 쓰기 작업 중에서 다음으로 작업할 프로세스를 선택할 때
읽기 작업보다 쓰기 작업을 먼저 수행합니다.
쓰기 작업이 여러 개라면, 먼저 요청된 쓰기 작업을 먼저 수행합니다.
대기 중인 작업을 배열에서 수행하려 함과 동시에 새로운 작업 요청이 들어온다면, 새 작업 요청을 포함하여 다음으로 작업할 프로세스를 선택합니다.
예를 들어, 10초에 쓰기 작업이 끝났고, 읽기 작업만 대기 중인 경우, 10초에 새로운 쓰기 작업 요청이 들어왔다면, 쓰기 작업을 먼저 처리합니다.
위 규칙에 따라 읽기, 쓰기 작업을 처리한 후, 읽기 작업에서 읽은 내용과 전체 프로세스가 배열을 사용한 시간은 얼마나 되는지 알아보려 합니다.

초기 배열의 상태가 담긴 문자열 배열 arr과 읽기, 쓰기 작업 요청이 담긴 문자열 배열 processes가 매개변수로 주어집니다. 읽기 작업에서 읽은 내용을 processes에서 주어진 순서대로 정답 배열에 담은 뒤, 배열이 전체 프로세스에 의해 사용된 시간을 정답 배열의 마지막에 담아 return 하도록 solution 함수를 완성해주세요.

제한사항
5 ≤ arr의 길이 ≤ 1,000
1 ≤ arr의 원소 ≤ 9
arr의 원소는 1부터 9까지의 숫자가 문자열 형태로 담겨있습니다.
1 ≤ processes의 길이 ≤ 1,000
processes의 원소는 "read t1 t2 A B", 또는 "write t1 t2 A B C" 형태입니다.
t1은 요청 시각, t2는 해당 요청을 처리하는데 걸리는 시간입니다.
1 ≤ t1 ≤ 1,000
1 ≤ t2 ≤ 100
A, B는 데이터를 읽거나 쓸 구간으로, 배열의 인덱스를 나타냅니다.
0 ≤ A ≤ B < arr의 길이
C는 배열 구간에 쓸 한 자리 숫자입니다. arr[A] ~ arr[B]에 해당하는 구간의 값을 C로 바꾸면 됩니다.
1 ≤ C ≤ 9
t1, t2, A, B, C는 모두 정수입니다.
같은 시각에 요청된 작업은 없습니다(즉, 모든 문자열에 대해서 t1의 값은 서로 다릅니다).
processes에는 "read t1 t2 A B"가 적어도 하나 이상 들어있습니다.
processes는 t1기준으로 정렬되어 있습니다.
배열이 전체 프로세스에 의해 사용된 시간은 정답 배열의 마지막에 문자열 형태로 담아 return 하면 됩니다.
입출력 예
arr	processes	result
["1","2","4","3","3","4","1","5"]	["read 1 3 1 2","read 2 6 4 7","write 4 3 3 5 2","read 5 2 2 5","write 6 1 3 3 9", "read 9 1 0 7"]	["24","3415","4922","12492215","13"]
["1","1","1","1","1","1","1"]	["write 1 12 1 5 8","read 2 3 0 2","read 5 5 1 2","read 7 5 2 5","write 13 4 0 1 3","write 19 3 3 5 5","read 30 4 0 6","read 32 3 1 5"]	["338","38","8888","3385551","38555","29"]
입출력 예 설명
입출력 예 #1

다음은 주어진 입력의 각 시각별 작업, 대기 프로세스를 나타낸 예시입니다.

시각(초)	작업 프로세스	대기 프로세스
0	[]	[]
1	[processes[0]]	[]
2	[processes[0],processes[1]]	[]
3	[processes[0],processes[1]]	[]
4	[processes[1]]	[processes[2]]
5	[processes[1]]	[processes[2],processes[3]]
6	[processes[1]]	[processes[2],processes[3],processes[4]]
7	[processes[1]]	[processes[2],processes[3],processes[4]]
8	[processes[2]]	[processes[3],processes[4]]
9	[processes[2]]	[processes[3],processes[4],processes[5]]
10	[processes[2]]	[processes[3],processes[4],processes[5]]
11	[processes[4]]	[processes[3],processes[5]]
12	[processes[3],processes[5]]	[]
13	[processes[3]]	[]
14	[]	[]
1초에 processes[0]가 배열에서 데이터를 읽기 시작합니다.
2초에 새로운 작업 processes[1]이 배열에서 데이터를 읽기 시작합니다.
3초에는 두 프로세스가 배열에서 데이터를 읽고 있습니다.
4초가 되면 processes[0]의 작업이 끝납니다. processes[2]가 쓰기 작업을 하려 하지만, 아직 읽기 작업이 진행 중이므로 대기합니다.
processes[0]는 1초부터 3초간 작업하므로, 4초가 되면 종료됩니다.
5초에는 processes[3]이 읽기 작업을 하려 하지만, 쓰기 작업(processes[2])이 대기 중이므로 대기합니다.
6초에는 processes[4]가 쓰기 작업을 하려 하지만, 읽기 작업이 진행 중이므로 대기합니다.
8초가 되면 processes[1]의 읽기 작업이 끝납니다. 대기 중인 작업 중 쓰기 작업(processes[2], processes[4])를 수행해야 하며, 더 먼저 요청된 processes[2]의 쓰기 작업을 진행합니다.
9초가 되면 processes[5]가 읽기 작업을 하려 하지만, processes[2]가 쓰기 작업 중이므로 대기합니다.
11초가 되면 processes[2]의 작업이 종료되고, 대기 중인 작업 중 쓰기 작업인 processes[4]를 수행합니다.
12초에는 processes[4]의 작업이 종료되며, 대기 중인 작업 중 읽기 작업인 processes[3],processes[5]를 수행합니다.
읽기 작업은 여러 개를 동시에 수행할 수 있으므로, 두 작업을 동시에 시작할 수 있습니다.
13초가 되면 processes[5]의 작업이 종료됩니다.
14초에는 processes[3]의 작업이 종료됩니다.
위 작업 진행 과정에서 읽기(read) 작업인 processes[0], processes[1], processes[3], processes[5]에서 읽은 내용은 순서대로 ["24","3415","4922","12492215"]가 됩니다. 또, 1초 ~ 14초까지 배열에서 작업을 진행했으므로 배열이 전체 프로세스에 의해 사용된 시간은 13초입니다. 따라서, 13을 문자열 형태로 정답 배열 제일 마지막에 추가하여 ["24","3415","4922","12492215","13"]을 return 하면 됩니다.

입출력 예 #2

1초 ~ 13초까지 processes[0]가 쓰기 작업을 수행합니다.
processes[1], processes[2], processes[3]가 읽기 작업을 요청하지만, 쓰기 작업이 진행 중이므로 대기합니다.
13초에 processes[0]의 쓰기 작업 수행이 종료됩니다.
동시에 13초에 processes[4]의 쓰기 작업이 요청되므로, 다음으로 작업할 프로세스는 읽기 작업 3개와 쓰기 작업 1개 중에서 선택해야 합니다.
쓰기 작업을 먼저 수행해야 하므로, processes[4]의 쓰기 작업을 수행합니다.
13초 ~ 17초까지 processes[4]의 쓰기 작업을 수행합니다.
17초부터 대기중인 읽기 작업 3개를 동시에 시작합니다.
19초에 processes[5]가 쓰기 작업을 요청하지만, 현재 읽기 작업이 진행 중이므로 대기합니다.
22초에 모든 읽기 작업이 종료되면, processes[5]의 쓰기 작업을 수행합니다.
25초가 되면 processes[5]의 쓰기 작업이 종료됩니다. 현재 대기 중인 작업은 없습니다.
30초에 processes[6]의 읽기 작업이 요청됩니다. 현재 대기 중 또는 수행 중인 작업은 없으므로 바로 읽기 작업을 수행합니다.
32초에 processes[7]의 읽기 작업이 요청됩니다.
34초에 processes[6]의 읽기 작업이 종료됩니다.
35초에 processes[7]의 읽기 작업이 종료됩니다.
배열이 전체 프로세스에 의해 사용된 시간은 1초 ~ 25초(24초간 사용), 30초 ~ 35초(5초간 사용)이므로, 총 29초 동안 사용되었습니다
'''