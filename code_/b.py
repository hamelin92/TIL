def BubbleSort(arr): # O(N**2)
	for i in range(len(arr) - 1, 0, -1):
		for j in range(i):
			if arr[j] > arr[j + 1]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
	return None

def CountingSort(arr, k): # O(N+k)
	cnt_arr = [0] * (k + 1)
	for num in arr:
		cnt_arr[num] += 1
	for i in range(1, len(cnt_arr)):
		cnt_arr[i] += cnt_arr[i - 1]
	res_arr = [-1] * len(arr)
	for i in range(len(res_arr) - 1, -1, -1):
		cnt_arr[arr[i]] -= 1
		res_arr[cnt_arr[arr[i]]] = arr[i]
		return res_arr

def SelectionSort(arr, k = -1): #선택 정렬 O(N**2), k번쨰로 작은 원소 찾기
	n = len(arr) if k < 0 else k
	for i in range(n):
		min_idx = i
		for j in range(i, len(arr)):
			if arr[min_idx] > arr[j]:
				min_idx = j
		arr[i], arr[min_idx] = arr[min_idx], arr[i]
	return arr[n-1]

def QuickSort(arr):
	return pass

def InsertionSort(arr):
	return pass

def MergeSort(arr):
	return pass

def RowSearch(arr, key):
	n = len(arr)
	m = len(arr[0])
	for i in range(n):
		for j in range(m):
			if arr[i][j] == key:
				pass
	return pass

def ColSearch(arr, key):
	n = len(arr)
	m = len(arr[0])
	for j in range(m):
		for i in range(n):
			if arr[i][j] == key:
				pass
	return pass

def ZigzagSearch(arr, key):
	n = len(arr)
	m = len(arr[0])
	for i in range(n):
		for j in range(m):
			if arr[i][j + (m-1-2*j)*(i%2)] == key:
				pass
	return pass

def DeltaSearch(arr, direc = 1, k = 0):
	# direc = 0: 시계방향, 1: 상하좌우, 2:좌우상하 3: 반시계방향
	n = len(arr)
	m = len(arr[0])
	if direc == 0:
		di = [-1, 0, 1, 0]
		dj = [0, 1, 0, -1]
	elif direc == 1:
		di = [-1, 1, 0, 0]
		dj = [0, 0, -1, 1]
	elif direc == 2:
		di = [0, 0, -1, 1]
		dj = [-1, 1, 0, 0]
	else:
		di = [-1, 0, 1, 0]
		dj = [0, -1, 0, 1]
	for i in range(n):
		for j in range(m):
			for k in range(4):
				ni = i + di[k]
				nj = j + dj[k]
				if 0 <= ni < n and 0<= nj < m:
					pass #test(arr[ni][nj]
	return pass

def Conjugate(arr): # 정사각 행렬(2차 리스트)의 전치
	n = len(arr)
	for i in range(n):
		for j in range(n):
			if i < j:
				arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
	return pass

def CountSubset(arr,m = -1, subarr = []):
	n = len(arr)
	for i in range(1<<n): # 1<< n = 2^n 부분집합의 총 개수
		for j in range(n):
			if i & (1<<j): # j번째 비트 연산 and
				subarr.append(arr[j])
	return None

def SequentialSearch(arr, key): # O(n)
	i = 0
	n = len(arr)
	while i < n and arr[i] != key:
		i = i+1
	if i < n:
		return i
	else:
		return -1
	
def BinarySearch(arr, key):
	start = 0
	end = len(arr) - 1
	while start <= end:
		middle = (start + end)//2
		if arr[middle] == key: # 검색 성공
			return True
		elif arr[middle] > key: # 키값이 중앙값의 왼쪽에 있는 경우(작은 경우)
			end = middle - 1
		else: # 키 값이 중앙값의 오른쪽에 있는 경우 (중앙값보다 큰 경우)
			start = middle + 1
	return False # 검색 실패

def BinarySearch2(arr, low, high, key): #재귀함수로 구현한 이진 탐색
	if low > high: # 검색 실패
		return False
	else:
		middle = (low + high)//2
		if key == arr[middle]: #검색 성공
			return True
		elif key < arr[middle]:
			return BinarySearch2(arr, low, middle-1, key)
		elif a[middle] < key:
			return BinarySearch2(arr, middle+1, high, key)
		
def BruteForce(sentence, pattern): #완전 탐색 문자열 탐색 알고리즘
	for i in range(len(sentence)-len(pattern)+1):
		for j in range(len(pattern)):
			if sentence[i+j] != pattern[j]:
				break
		else:
			pass # 패턴 존재 확인!
	return pass
def skip(pattern):
	M = len(pattern)
	lps = [0] * M
	j=0
	for i in range(1, M):
		if pattern[i] == pattern[j]:
			lps[i] = j + 1
			j += 1
		else:
			j=0
			if pattern[i] == pattern[j]:
				lps[i] = j+1
				j+=1
	return lps

def KMPSearch(sentence, pattern, lps):
	N = len(sentence)
	M = len(pattern)
	
	i, j = 0, 0
	pos = -1
	while i < N:
		if pattern[j] == sentence[j]:
			i+=1
			j+=1
		else:
			if j != 0:
				j = lps[j-1]
			else:
				i += 1
		if j == M:
			pos = i-j
			break
	return pos

def pre_process(P):
    from collections import defaultdict

    M = len(P)

    # skip 배열 대신 딕셔너리
    PI = defaultdict(int)

    # 실 사용은 M - value로 할 예정.
    for i in range(M-1):
        PI[P[i]] = 1 + i
    return PI


def boyer_moore(T, P, PI):

    N = len(T)
    M = len(P)

    i = 0
    # 실패할 경우 -1 return
    pos = -1

    while i <= N - M:
        # skip 잘 되고있나 확인
        print(i)

        #
        # M번째 인덱스
        j = M - 1
        k = i + M - 1

        # 비교할 j가 남아있고, text와 pattern이 같으면 1씩 줄여 왼쪽 비교
        while j >= 0 and P[j] == T[k]:
            j -= 1
            k -= 1
        # 비교 성공
        if j == -1:
            pos = i
            break
        # i를 M - value만큼 스킵
        i = i + M - PI[T[i + M - 1]]

    return pos
