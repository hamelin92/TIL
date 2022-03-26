def solution(goods):
    from collections import deque # deque 모듈 사용
    N = len(goods)
    answer = []
    for k in range(N): # goods의 인덱스에 대해 순회
        tmp_ans = set() # 각각 goods의 원소들을 저장할 set
        lst = [[_, _+1] for _ in range(len(goods[k]))] # 큐에 들어갈 문자열 슬라이싱 인덱스값들을 생성
        que = deque(lst)
        key_length = len(goods[k]) # 최소길이의 고유 검색어만 저장하기위한 초기 변수
        while que:
            word = que.popleft() # 큐에서 슬라이싱 인덱스를 뽑는다.
            if key_length < word[1]-word[0]: # 만약 큐에서 뽑은 것의 슬라이싱 길이가 key_length보다 크다면 while문을 탈출한다.
                break
            for i in range(N): # 다시 goods의 인덱스에 대해 순회
                if i == k: # 현재 문자열을 뽑아온 goods의 원소와 탐색할 원소의 인덱스가 같다면 스킵
                    continue
                if goods[k][word[0]:word[1]] in goods[i]: # 만약 큐에서 뽑은 값으로 슬라이싱한것이 다른 원소에 들어있다면.
                    if word[1] < len(goods[k]): # 그중 만약 문자열을 더 붙일 수 있다면 하나 더붙여서 (슬라이싱 뒷자리 +1 ) 큐에 다시 넣고 break.
                        que.append([word[0], word[1]+1])
                    break
            else: # for문이 break 없이 종료됬다면 고유 검색어 이므로 슬라이싱하여 문자열로 변환하고 정답에 넣어준다.
                tmp_ans.add(goods[k][word[0]:word[1]])
                key_length = word[1]-word[0] # 이떄 key_length값을 해당 슬라이싱의 길이로 재설정한다.
        tmp_ans = sorted(list(tmp_ans)) # while문이 끝나면 set으로 모아둔 검색어들을 리스트로 변환하고 정렬해서 저장한다.
        keywords = ' '.join(tmp_ans) # 그것들을 띄어쓰기로 구분하여 하나의 문자열로 합쳐서 answer에 넣는다.
        if keywords == '': # 만약 그 결과가 빈 문자열이면 None으로 바꿔서 넣는다.
            keywords = 'None'
        answer.append(keywords)
    return answer
print(solution(["pencil","cilicon","contrabase","picturelist"]))






'''
문제 설명
당신은 쇼핑몰에서 상품을 검색할 수 있습니다. 검색어를 입력하면 검색어를 부분 문자열로 갖는 모든 상품들이 검색됩니다.
부분 문자열이란, 문자열의 연속된 일부를 의미합니다. 예를 들어 abcde의 부분 문자열로 abc나 bcde 등이 있고, ac나 ea는 부분 문자열이 아닙니다.

특정 단어로 검색해서 검색된 상품의 개수가 하나일 때, 해당 단어를 상품의 고유 검색어라고 합니다. 당신은 상품마다 고유 검색어 중 가장 짧은 고유 검색어 목록을 구하려 합니다.

검색어 목록은 사전 순서대로 빠른 순으로 정렬되고, 중복되지 않아야 합니다. 검색어 목록은 공백 하나로 검색어들을 구분하는 형태입니다. 만약 고유 검색어가 없다면 None을 목록에 담습니다.

예를 들어, 쇼핑몰에 pencil, cilicon, contrabase, picturelist 네 가지 상품이 있다면, 각 상품의 가장 짧은 고유 검색어 목록은 다음과 같습니다.

pencil : en nc pe 
cilicon : ico ili lic 
contrabase : a b 
picturelist : u 
pencil의 고유 검색어를 예시로 들어보겠습니다.

pencil의 고유 검색어 중 길이가 1인 검색어는 존재하지 않습니다.
p를 검색어로 검색하면 pencil과 picturelist 두 가지 상품이 검색되므로 p는 pencil의 고유 검색어가 아닙니다.
e,n,c,i,l도 마찬가지로, pencil과 다른 상품이 함께 검색되므로 pencil의 고유 검색어가 아닙니다.
en,nc,pe중 하나를 검색했을 때 pencil 하나만 검색됩니다. 따라서 pencil의 가장 짧은 고유 검색어는 en,nc,pe 3가지입니다.
enc, nci, pencil 등도 고유 검색어지만, 더 짧은 고유 검색어가 존재하므로 가장 짧은 고유 검색어에서 제외됩니다.
쇼핑몰에 등록된 상품의 이름을 담은 문자열 배열 goods가 매개변수로 주어졌을 때, 가장 짧은 고유 검색어 목록을 순서대로 문자열 배열에 담아 return 하도록 solution 함수를 완성해 주세요.

제한사항
2 ≤ goods의 길이 ≤ 100
2 ≤ goods의 원소의 길이 ≤ 20
goods의 원소는 알파벳 소문자로 이루어져 있습니다.
입출력 예
goods	result
["pencil","cilicon","contrabase","picturelist"]	["en nc pe","ico ili lic","a b","u"]
["abcdeabcd","cdabe","abce","bcdeab"]	["abcd eabc","be da","ce","None"]
입출력 예 설명
입출력 예 #1

문제 예시와 동일합니다.
입출력 예 #2

abcdeabcd : abcd eabc
cdabe : be da
abce : ce
bcdeab : None
4가지 상품의 가장 짧은 고유 검색어의 목록은 위와 같습니다.
bcdeab는 고유 검색어가 없으므로 None을 목록에 담습니다.
'''