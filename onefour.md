

# GIT 조작하기

mkdir - 디렉토리(폴더 생성) 명령어

ls - 현재 위치에 있는 파일들 리스트 나열

cd - change directory 위치를 옮김

. - 현재위치를 의미 / .. -  부모디렉토리를 의미

touch 파일명.확장자 - 파일을 만드는 명령어 ex) a.txt 라는 식으로 이름과 확장명까지 정확하게 입력

start 파일명.확장자 - 파일 실행 명령어

mv 파일명1.확장 파일명2.확장 - 파일명1의 이름을 파일명2로 변경 (move)

mv 파일명.확장 디렉토리명 - 파일을 해당 디렉토리로 옮김

mv 디렉1 디렉2 - 디렉1을 디렉2로 옮김/

rm 파일명.확장 - 해당파일을 삭제(remove) - 휴지통 x 바로 완전 삭제

rm -r 디렉토리명 - 디렉토리를 r(ecursive, 재귀적)으로 삭제(앞초성을 입력후 tab을 누르면 자동완성)

clear 화면 청소

git config --global user.name hamelin92 / 유저이름 등록 

git config --global user.email hamelin92@gmail.com / 이메일 등록

git config --global -l    // 현재 입력된 것들 확인 

git init   / 깃 시작 / 이미 git init을 실행한 디렉토리나 홈 디렉토리에서는 절대 x

git status / 깃 관리 상태 

git add 파일명   // 깃 관리 목록에 추가 (staging area에 추가) 파일명 대신 . (현재 디렉토리 전체)

git commit -m / 메세지를 남기고(변경사항) commit으로 넘긴다.

git log / 깃 로그 확인 --oneline 명령어 추가로 요약해서 출력

rm *.txt / txt 형식 전부 삭제

git remote add origin(변경가능) (giturl) 해당 로컬 디렉토리와 깃허브의 해당 레포지토리와 연결

git remote -v / 연결된것 확인

git push -u origin master / 레포지토리에 업데이트 내용 업로드하기

git clone url / 해당 url 레포지토리 클론 생성 ( 깃 설정까지)

git pull / 깃 업데이트 내용  내려받기

esc - escape

git commit 후 엔터 / 



# Branch

commit 후 git branch (이름) 명령어를 통해 생성

"멀티버스"랑 비슷

git switch 브랜치이름  해당 브랜치로 변경



master 브랜치에서 git merge new(합칠 브랜치 이름)으로 브랜치 합병

서로 기존 내용에 영향을 주지 않는다면 각각의 변경점은 모두 합쳐진다.



master 브랜치에서 git branch -d 브랜치명 으로 브랜치 삭제.



### conflict 에러



만약 브랜치1 과 브랜치2가 충돌할 경우 

ex: 동시점 기준으로 파일 A를 브랜치 1에서는 A+로 , 2에서는 A&로 수정한 경우

이때 merge를 실행한 경우 merging 으로 브랜치에 상태가 표시되고

직접 그 파일을 수정해줘야한다.

vscode로 해당 충돌파일을 실행하여 최종버전을 선택하고 git add와 commit 을 실행하면 정상적으로

처리된다.



---

```
GUI

graphic user interface그래픽 유저 인터페이스 상호작용하는 방법

CLI

command line interface



- ~ : 홈 디렉토리
  - 내 계정이 있는 디렉토리를 의미합니다. C:\Users\{유저이름}입니다.



- 상대경로 : 내 위치에 따라서 접근하는 곳이 바뀔 수 있어요

  어떠한 위치를 기준을 잡아서 상대적으로 경로를 설정합니다.

  ex) 아파트 203호

- 절대경로 : 어디서 접근하던지 변하지 않아요

  위치를 기준으로 잡지 않고 모든 경로를 표현해줍니다

  ex) 대전광역시 유성구 ??동 ??아파트 ??동 ??호

  

- `..`은 부모 디렉토리를 가르킵니다

- `.`은 현재 디렉토리를 가리킵니다







- ls
  - list segment
  - 현재 폴더에 어떤 파일이 있는지 확인

- cd
  - change directory
  - cd {폴더}
    - {폴더}로 이동하겠어!
  - `cd ..`을 하게 되면 부모 디렉토리로 이동하게 됩니다!
- mkdir
  - make directory
  - mkdir {폴더}
    - {폴더}를 생성하겠어!
- touch
  - touch {파일}
    - {파일}을 생성하겠어!
    - 확장자를 반드시 포함해야 합니다!

- mv
  - mv {파일1} {파일2}
    - {파일1}의 이름을 {파일2}로 변경하겠어!
  - mv {파일} {폴더}
    - 파일을 폴더로 옮기겠어!
- rm
  - rm {파일}
    - 파일 지우기
      - 휴지통으로 가지 않고 바로 지워짐.
  - rm -r {폴더}
    - 폴더 지우기 -r(recursive)
```



```
- 초기세팅
  - git config --global user.name {유저네임}
  - git config --global user.email {유저이메일}
  - git config --global -l
    - 설정 확인
- git init
  - 깃을 시작한다!
- git add {파일}
  - 파일을 staging area에 올려 놓는다!
  - (처음 만든 파일은 깃이 관리를 하기 시작한다)
  - git add .
    - 을 하게되면 해당 폴더의 모든 아이들을 추가합니다!
- git status
  - 깃이 관리하고 있는 파일들의 상태를 확인한다
- git commit -m "메시지"
  - "메시지"라는 변경사항을 담아서 코밋을 남긴다
- git commit
  - 만 한 경우에는 vim 에디터가 나옵니다
  - `i`를 입력하시면 insert 모드가 되어 입력이 가능합니다.
  - `esc`를 눌러 insert모드에서 나옵니다
  - `:wq`를 입력하여 저장하고 나옵니다.
  - enter를 누번 눌러 내용을 구체적으로 작성 가능합니다!(additional)
- git log
  - 코밋 상태를 확인한다
  - git log --oneline
    - 코밋 상태를 한줄로 확인한다
  - git log -{숫자}
    - 숫자개의 코밋만 확인한다



#### 깃허브와 연결

- git init

- 깃허브 레포 만들기
  - 레포의 주소 복사하기( 가운데에 버튼이 있씁니다!)

- git remote add origin {url}
  - 깃허브 주소를 'origin'이라는 별명으로 원격으로 연결할거야!
  - git remote -v
    - 원격으로 어디에 연결되어있는지 확인할게!
- git push origin master
  - origin이란 별명을 가진 깃허브 레포의 master브랜치에 push 할꺼야!
  - git push -u origin master
    - origin master는 계속 사용하니 설정을 저장하여 이후에는 생략할꺼야!
    - 이후에는 `git push`만 해도 push가 가능합니다!



### clone

- git clone {url}

  - 깃이 아닌 상태에서 깃허브의 레포지토리를 복사해 오는 것
  - 최초 1회만 하면 됩니다!

  1. `git clone {url}` -> 레포 이름으로 폴더를 생성하여서 clone
  2. `git clone {url} .` -> git bash가 실행된 폴더에 clone
  3. `git clone {url} {폴더이름}` -> 폴더이름을 생성하여 clone

- git pull

  - 최초의 clone 이후 (또는 이미 깃인 상태에서) 깃허브의 코밋으로 최신화 시킨다

### branch

- git branch
  - 어떤 브랜치가 존재하는지, *이 있는게 현재 브랜치
- git branch {브랜치이름}
  - 브랜치를 만듦
- git switch {브랜치이름}
  - 해당 브랜치로 옮김
  - git switch -c {브랜치이름}
    - 브랜치를 만듦과 동시에 해당 브랜치로 옮김
- git branch -d {브랜치이름}
  - 브랜치 삭제

- git merge {브랜치이름} 
  - 현재 브랜치에서 {브랜치이름}을 병합시킴
  - CONFLICT (pull도 마찬가지)
    - A'B + AB' = A'B'
    - A' +Ã = CONFLICT!
      - 해결 후 add, commit
```



````
## 마크다운

#### 1. 제목

# 사용할 수 있습니다

\# 띄어쓰기로 사용할 수 있습니다. #의 개수로 제목의 사이즈(중요도)조절

글씨를 키우려고 #을 사용하는게 아니라, 문서의 구조를 확립하기 위해 사용합니다.

[toc]를 사용해서 목차를 만들 수 있습니다.



#### 2. 리스트

\-, \*, \+ 뒤에 띄어쓰기로 순서 없는 리스트를 사용할 수 있습니다.

- 순서 없는 리스트
  - 탭을 한번 누르면 리스트 안에 다시 리스트를 만들 수 있어요!
    - 여러번도 가능합니다!
  - shift tab을 누르게 되면 인덴테이션이 한칸 물러나게 됩니다!



1\. 띄어쓰기를 하면 순서가 있는 리스트를 사용할 수 있습니다.

1. 순서 있는 리스트

   1. 마찬가지로 탭을 누르면 리스트 안에 리스트가 만들어 져요!
      1. 여러번도 가능하죠!
   2. - shift tab을 누르게 되면 인덴테이션이 한칸 물러나게 됩니다!

   

#### 3. 코드 블럭

\`\`\`에 사용하는 프로그래밍 언어를 입력하게 되면 해당 언어에 맞게 코드블럭이 표시됩니다!

```python
print('hello world!')
```



\`로 둘러싸게 되면 문장 안에서 코드를 표현할 수 있습니다!

나는 `print()`함수를 사용할거야!



#### 4. 이미지

\!\[이미지의 이름](이미지의 주소)

입력하면 됩니다!

옵션을 잘 설정하셨으면 해당 md(마크다운)파일의 이름.assets라는 폴더가 생기고, 그 안에 사진 파일이 저장됩니다!

그리고 마크다운은 해당 파일의 주소만 가지고 있습니다!



#### 5. 링크

\[보여질 이름](url)

[naver](https://www.naver.com)

ctrl + 클릭을 하시게 되면 해당 링크로 이동할 수 있습니다!



#### 6. 테이블

\|를 사용하여 컬럼을 구분합니다! 마지막 \|를 닫고 엔터를 누르면 테이블이 생성됩니다!

ctrl + enter를 누르시면 아래에 추가적인 정보를 적을 수 있습니다

| 컬럼1  | 컬럼2    | 컬럼3       |
| ------ | -------- | ----------- |
| 이렇게 | 테이블이 | 생성됩니다! |
|        |          |             |



#### 7. 기타

##### 	인용문

	\>을 사용하여 인용문을 아래와 같이 표시할 수 있습니다

> 이렇게 말이죠!

##### 	수평선

	\-\-\-를 이용하여 수평선을 넣을 수 있습니다!

---

	\- 대신에 \* 혹은 _를 사용할 수 있지만, shift를 눌러야하기 때문에 많이 사용하진 않아요



	##### 	강조

	\* 하나로 둘러싸게 되면 *이텔릭체*를 사용할 수 있습니다!

	\* 두개로 둘러싸게 되면 **볼드체**를 사용할 수 있습니다!

	\* 세개로 둘러싸게 되면 ***볼드+이텔릭체***를 사용할 수 있습니다.



\\는 ecape 시퀸스로, 뒤에 있는 아이는, '글자'그대로 로 판단할 것이다. 라는 의미입니다.

\-이라는 단어를 쓰고 싶은데, 자동으로 리스트가 되어버려

\\\-를 사용하면 \-만 표시가 됩니다.
````