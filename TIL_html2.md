# HTML (Hyper Text Markup Language)

- HTML 문서의 기본구조(!+tab)
- DOM
- 시맨틱 태그
- 주요 태그와 속성
  - ~~table, form, input~~


# CSS

- 단위 (크기, 속성)
- 선택자 및 우선순위
- 박스 모델
- 인라인, 블록 요소 특징
- Position
  - static
  - relative
  - absolute(out of flow)
  - fixed(out of flow)
  - sticky
- ~~Float~~
- Flex
  - axis, container - item
  - 각 속성

# 반응형 웹

- Bootstrap
  - Grid System
  - Breakpoint



## html 기본 구조

- html : 문서의 최상위 요소
- head : 문서 메타데이터 요소
  - 문서 제목, 인코딩, 스타일, 외부 파일 로딩 등
  - 일반적으로 브라우저에 나타나지 않는 내용
- body : 문서 본문 요소
  - 실제 화면 구성과 관련된 내용

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
</head>
<body>
	
</body>
</html>
```



###### head 예시

- title : 브라우저 상단 타이들
- meta : 문서 레벨 메타데이터 요소
- link : 외부 리소스 연결 요소 (CSS 파일, favicon 등)
- script : 스크립트 요소 (JavaScript 파일/코드)
- style : CSS 직접 작성



## Dom(Document Object Model) 트리

- 텍스트 파일인 HTML 문서를 브라우저에서 렌더링 하기 위한 구조
  - HTML 문서에 대한 모델을 구성함
  - HTML 문서 내의 각 요소에 접근 / 수정에 필요한 property와 method 제공

---

- element : 요소,  attribute: 속성, 
- Document
  - root element <html>
    - Element <head>
      - Element: <title>
        - text: "My titme"
    - Element<body>
      - Element: <h1>
        - text: "A heading"
      - Element:<a> / Attribute: href
        - text: "Link text"
    - ...

## 시맨틱 태그

- HTML5에서 의미론적 요소를 담은 태그의 등장(별도의 기능은 없음)
  -  기존 영역을 의미하는 div 태그를 대체하여 사용
- 대표적인 태그 목록
  - header: 문서 전체나 섹션의 헤더(머리말 부분)
  - nav : 내비게이션
  - aside : 사이드에 위치한 공간, 메인 콘텐츠와 관련성이 적은 콘텐츠
  - section : 문서의 일반적인 구분, 컨텐츠의 그룹을 표현
  - article : 문서, 페이지, 사이트 안에서 독립적으로 구분되는 영역
  - footer : 문서 전체나 섹션의 푸터(마지막 부분)
- h1~6 같은 태그들도 시맨틱 태그라고 볼 수 있다.
- div, span 등은 Non semantic
- 테그를 단순히 구역을 나누기보다 의미를 가지고 활용하기 위한 노력
- 요소의 의미가 명확해져 코드 가독성을 높이고 유지보수를 쉽게 함



## 요소들

텍스트 요소

```html
<a></a> href 속성을 활용하여 다른 url로 연결하는 하이퍼링크 생성

<b></b> 굵은 글씨 요소
<strong></strong> 중요한 강조하고자 하는 요소 (보통 굵은 글씨로 표현)

<i></i> 기울임 글씨 요소
<em></em> 중요한 강조하고자 하는 요소 (보통 기울임 글씨로 표현)

<br> 텍스트 내 줄바꿈

<img> src 속성을 활용, 이미지 표현

<span></span> 의미없는 인라인 컨테이너
```

그룹 컨텐츠

```html
<p></p> 하나의 문단 paragraph
<hr> 문단 레벨 요소에서 주제의 분리를 의미, 수평선으로 표현(Horizontal Rule)
<ol></ol> 순서 있는 리스트 (ordered)
<ul></ul> 순서 없는 리스트 (unordered)
<pre></pre> HTML에 작성한 내용을 그대로 표현. 보통 고정폭 글꼴이 사용되고 공백 문자를 유지
<blockquote></blockquote> 텍스트가 긴 인용문 주로 들여쓰기를 한 것으로 표현
<div></div> 의미없는 블록 레벨 컨테이너

```



## CSS 단위

크기 단위 

- px (픽셀, 모니터 해상도의 한 화소 픽셀 기준) 
- rem (root element의 사이즈 기준으로 배수 단위, 보통 1rem = 16px), 
- em (바로 위, 부모요소에 대한 상속받음, 요소에 지정된 사이즈에 상대적인 사이즈로 배수 단위)
- % (크기의 % 비율, 가변적 레이아웃에서 자주 사용)
- viewport ( 웹페이지를 방문한 유저에게 바로 보이게 되는 웹 컨텐츠의 영역 (디바이스 화면))
- 디바이스의 viewport를 기준으로 상대적인 사이즈가 결정됨 
- vw, vh, vmin, vmax

색상 단위

- 색상 키워드
  - 대소문자 구분 X
  - red, blue, black 과 같은 특정 색을 직접 글자로 나타냄
- RGB 색상
  - 16진수 표기법 혹은 함수형 표기법을 사용해서 특정 색 표현
  - #FFFFFF 와 같이 #+16진수표현 혹은 rgb(255,255,255) / rgba(255,255,255,0)
- HSL 색상
  - 색상, 채도, 명도를 통해 특정 색을 표현하는 방식
  - hsl(120,100%,0) 같은 식으로. / hsla(120,100%,0,100)
  - a는 alpha(투명도)

## 속성

- height
- width
- font-size
- color
- background-color
- display
- box-sizing
- border
- padding
- margin
- 등등



## 선택자 및 우선순위

### 유형

- 기본 선택자
  - 전체 선택자(*) 요소 선택자 *, p, h1, div, table 등등
  - 클래스 선택자, 아이디 선택자, 속성 선택자 .class, #id, 
- 결합자
  - 자손 결합자, 자식 결합자
  - 일반 형제 결합자, 인접 형제 결합자
- 의사 클래스/요소
  - 링크, 동적 의사 클래스
  - 구조적 의사 클래스, 기타 의사 클래스, 의사 엘리먼트, 속성 선택자

- 요소 선택자
  - HTML 태그를 직접 선택
- 클래스 선택자
  - 마침표 문자로 시작하며, 해당 클래스가 적용된 항목을 선택
- 아이디 선택자
  - #문자로 시작하며, 해당 아이디가 적용된 항목을 선택
  - 일반적으로 하나의 문서에 1번만 사용, 여러번 사용해도 동작하지만 단일 id를 사용하는 것을 권장

### 우선순위

1. 중요도(importance) 속성에 !important
2. 우선순위
   - 인라인 > id > class, 속성, pseudo-class > 요소, pseudo-element
3. CSS 파일 로딩 순서

- 인라인 선택자 ( ex: <h1 style="font-size: 80px">)

## 결합자

- 자손 결합자
  - selectorA selectorB {} : selectorA 하위의 모든 selectorB 요소
- 자식 결합자
  - selctorA > selectorB {} : selectorA 바로 아래의 selectorB요소
- 일반 형제 결합자
  - selectorA ~ selectorB {} : selectorA의 형제 요소(같은 라인에 있는) 중 뒤에 위치하는 selectorB 요소 모두 선택
- 인접 형제 결합자
  - selectorA + selectorB {} : selectorA의 형제 요소중 바로 뒤에 위치하는 selectorB요소를 선택



## 박스 모델

모든 요소는 네모( 박스 모델 )이고, 위에서부터 아래로, 왼쪽에서 오른쪽으로 쌓인다. (normal flow)

모든 html 요소는 box 형태로 되어있음. 하나의 박스는 4 영역으로 이루어짐.

- 마진 margin : 테두리 바깥의 외부 여백, 색지정 X
- 보더 border : 테두리 영역
- 패딩 padding : 테두리 안쪽의 내부 여백, 요소에 적용된 배경색, 이미지까지는 적용됨.
- 컨텐트 content : 글이나 이미지 등 요소의 실제 내용
- margin, padding size(shorthand) - 상 하 좌 우(1개 - 전부, 2개 상하/ 좌우, 3개 - 상 좌우 하, 4개 - 상 우 하 좌(시계방향))

- margin-top, right, bottom, left
- border: width, style, color (shorthand)
- style - dashed (점선) , solid(꽉 채워진 선)
- box-sizing
  - 기본적으로 content-box : padding을 제외한 순순 contents 영역만을 box로 지정
  - border 기준으로 전체 사이즈를 정하고 싶다면 border-box로 설정



## 인라인 / 블록 요소

- display: block
  - 줄 바꿈이 일어나는 요소
  - 화면 크기 전체의 가로폭을 차지함.
  - 블록 레벨 요소 안에 인라인 레벨 요소가 들어갈 수 있음.
- display: inline
  - 줄 바꿈이 일어나지 않는 해의 일부 요소
  - content 너비만큼 가로 폭을 차지함.
  - width, height, margin-top, margin-bottom을 지정할 수 없다.
  - 상하 여백은 line-height로 지정.
- 블로의 기본 너비는 가질 수 있는 너비의 100% / 인라인은 기본 컨텐츠 영역까지.
- 너비를 가질 수 없다면 자동으로 margin 부여
  - 속성에 따른 수평 정렬: 
    - margin-right: auto; / text-align: left; : 왼쪽에 붙임.
    - margin-left: auto;/text-align: right: 오른쪽에 붙임
    - margin-right: auto; margin-left: auto; / text-align: center :중앙에 배치
- display: inline-block
  - block과 inline 레벨 요소의 특징을 모두 가짐
  - inline처럼 한 줄에 표시 가능하고, block처럼 width, height, margin 속성을 모두 지정할 수 있음.
- display: none
  - 해당 요소를 화면에 표시하지 않고, 공간조차 부여되지 않음.
  - 이와 비슷한 visibility: hidden은 해당요소가 공간은 차지하나 화면에 표시만 하지 않는다.



## Position

- static: 모든 태그의 기본 값
  - 일반적인 요소의 배치 순서에 따름
  - 부모 요소 내에서 배치될 때는 부모 요소의 위치를 기준으로 배치됨
- relative:  상대 위치
  -  자기 자신의 static 위치를 기준으로 이동 ( normal flow 유지)
  - 레이아웃에서 요소가 차지하는공간은 static일 때와 같음. (normal position대비 offset)
- absolute: 절대 위치
  - 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음 (normal flow에서 벗어남)
  - static이 아닌 가장 가까이 있는 부모/ 조상 요소를 기준으로 이동, 없는 경우 body
- fixed : 고정 위치
  - 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음 (normal flow에서 벗어남)
  - 부모 요소와 관계없이 viewport를 기준으로 이동
    - 스크롤 시에도 같은 위치



## float

- float속성 
  - none , left, right
- flexbox, Grid 대비 용도 낮아짐.

## Flexbox

행과 열 형태로 아이템들을 배치하는 1차원 레이아웃 모델 

- 축
  - main axis (메인 축)
  - cross axis (교차 축)
- 구성 요소
  - Flex Container (부모 요소)
    - flexbox 레이아웃을 형성하는 가장 기본적인 모델
    - .flex-container { display : flex; }
    - flex item들이 놓여있는 영역
    - display 속성을 flex 혹은 inline-flex로 지정
  - Flex Item (자식 요소)
    - 컨테이너에 속해있는 컨텐츠(박스)
- Flex 속성
  - 배치 설정
    - flex-direction : 메인 축 기준 방향 설정
      - 1. row :  가로, 좌에서 우측방향으로
        2. row-reverse : 가로 우에서 좌측 방향으로
        3. column : 세로 위(좌측)에서 아래로
        4. column-reverse : 세로 아래에서 위로
    - flex-wrap : 아이템이 컨테이너를 벗어나는 경우 해당 영역내에 배치되도록 설정.
      - 1. wrap : 넘치면 그 다음줄에 배치
        2. nowrap : 강제로 한줄에 배치. 기본 설정
        3. wrap-reverse: wrap과 반대 방향으로.
    - flex-flow
      - flex-direction과 flex-wrap의 shorthand, direction과 wrap 값을 차례로 작성
  - 공간 나누기
    - justify-content (main axis) : 메인 축 기준으로 공간 배분
      - 1. flex-start : 시작 지점에 붙어서 배치
        2. flex-end : 끝 지점에 붙어서 배치
        3. center : 중앙에 배치
        4. space-between : 양쪽 끝 배치 후 사이에 같은 간격으로 배치
        5. space-around : 1:2:...:2:1 간격으로 배치
        6. space-evenly: 1:1:1:1 간격으로 배치
    - align-content (cross axis) : 크로스 축 기준으로 공간배분
      - 위와 같음
  - 정렬
    - align-items ( 모든 아이템을 cross axis 기준으로)
      - 1. stretch : 꽉 채워서  배치
        2. flex-start : 시작지점에 붙어서 배치
        3. flex-end: 끝 지점에 붙어서 배치
        4. center : 중앙에 배치
        5. baseline : baseline 기준으로 배치
    - align-self (개별 아이템)
  - 기타
    - flex-grow : 남은 영역을 아이템에 분배
    - order : 배치 순서



# 반응형 웹

## bootstrap

- 각종 디테일한 기본 설정들이 커스텀 되어있다.
- 각종 편의를 위한 클래스들이 정의되어있다. ( my-0, m-0, px-2 등등)
- Media Queries, Flexbox, Bootstrap grid system, the viewport meta tag

## Gridsystem

- Container : Column들을 담고 있는 공간
- gutter : 칼럼과 칼럼사이의 공간 (사이 간격)
- row : 행
- col : 실제 컨텐츠를 포함하는 부분
- 12개의 column
- row-col-숫자 : 1개의 row에서 col의 최대 수용 갯수
- col-1~12: 각각의 col에 대해 칸수 지정
- col-md-6, row-col-lg-6 : breakpoint를 넣어서 사이즈에 따라 칸 배치를 지정해줄 수 있다.
- offset-숫자: 숫자칸 만큼 빈칸을 띄움

## Breakpoint

- 6개의 grid breakpoints : xs(576px 미만) , sm(576픽셀 이상), md(768픽셀 이상), lg(992픽셀 이상), xl(1200픽셀 이상), xxl(1400픽셀 이상)





# 마크업

- 각 태그별 속성
  - 인라인, 블록
  - li -> list-style



# 스타일링



# 레이아웃

display를 가지고 있는지 분석, Box model

- Position
  - 네모위 네모 => absolute
  - 브라우저 기준 => fixed, sticky

- flex
- Bootstrap Grid System



# 스타일

- color
- size
- 각 태그별 속성...



## 웹 개발

