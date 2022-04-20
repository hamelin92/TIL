



[TOC]



# Django 개론

- web

  - 인터넷에 연결된 컴퓨터를 통해 정보를 공유할 수 있는 정보공간

- Static web page(정적 웹 페이지)

  - 서버에 미리 저장된 파일이 사용자에게 그대로 전달되는 웹페이지
  - 서버가 정적 웹 페이지에 대한 요청을 받은 경우 서버는 추가적인 처리 과정 없이 클라이언트에게 응답을 보냄
  - 모든 상황에서 모든 사용자에게 동일한 정보를 표시
  - 일반적으로 HTML, CSS, Java Script 로 작성됨
  - flat page라고도 함

- Dynamic web page(동적 웹 페이지)

  - 웹 페이지에 대한 요청을 받은 경우 서버는 추가적인 처리 과정 이후 클라이언트에게 응답을 보냄
  - 동적 웹 페이지는 방문자와 상호작용하기 때문에 페이지 내용은 그때그때 다름
  - 서버 사이드 프로그래밍 언어(파이썬, 자바, 씨쁠쁠)가 사용되며, 파일을 처리하고데이터베에스와의 상호작용이 이루어짐

- Web framework

  - 웹페이지를 개발하는 과정에서 겪는 어려움을 줄이는 것이 주 목적으로 데이터베이스 연동, 템플릿 형태의 표준, 세션 관리, 코드 재사용 등의 기능을 포함
  - 동적인 웹페이지나, 웹 어플리케이션, 웹 서비스 개발 보조용으로 만들어지는 Application framework의 일종

- Framework Architecture

  - MVC Design Pattern (model -veiw - controller)
  - 소프트웨어 공학에서 사용되는 디자인 패턴 중 하나
  - 사용자 인터페이스로부터 프로그램 로직을 분리하여 애플리케이션의 시각적 요소나 이면에서 실행되는 부분을 서로 영향 없이 쉽게 고칠 수 있는 애플리케이션을 만들 수 있음
  - Django는 MTV Patter이라고 함

- MTV Pattern

  - Model
    - 응용프로그램의 데이터 구조를 정의하고 데이터베이스의 기록을 관리(추가, 수정, 삭제)
  - Template
    - 파일 구조나 레이아웃을 정의
    - 실제 내용을 보여주는 데 사용(presentation)
  - View
    - HTTP 요청을 수신하고 HTTP 응답을 반환
    - Model을 통해 요청을 충족시키는데 필요한 데이터 접근
    - template에게 응답 서식 설정을 맡김

  

- 프로젝트 구조

  - **init**.py

    - python에게 이 디렉토리를 하나의 파이썬 패키지로 다루도록 지시

  - [asgi.py](http://asgi.py)

    - Asynchronous Server Gateway interface
    - Django 애플리케이션이 비동기식 웹 서버와 연결 및 소통하는 것을 도움

  - [settings.py](http://settings.py)

    - 애플리케이션의 모든 설정을 포함

  - [urls.py](http://urls.py)

    사이트의 url과 적절한 views의 연결을 지정

  - [wsgi.py](http://wsgi.py)

    - Web Server Gateway Interface
    - django 애플리케이션이 웹서버와 연결 및 소통하는 것을 도움

  - [manage.py](http://manage.py)

    Django 프로젝트와 다양한 방법으로 상호작용 하는 커맨드라인 유틸리티

- Application 구조

  - admin.py
    - 관리자용 페이지를 설정하는 곳
  - apps.py
    - 앱의 정보가 작성된 곳
  - models.py
    - 앱에서 사용하는 Model 을 정의하는 곳
  - tests.py
    - 프로젝트의 테스트 코드를 작성하는 곳
  - views.py
    - view 함수들이 정의 되는 곳

- Project & Application

  - project
    - project는 Application의 집합
    - 프로젝트에는 여러개의 앱이 포함될 수 있음
    - 앱은 여러 프로젝트에 있을 수 있음
  - application
    - 앱은 실제 요청을 처리하고 페이지를 보여주고 하는 등의 역할 담당
    - 하나의 프로젝트는 여러 앱을 가짐
    - 일반적으로 앱은 하나의 역할 및 기능 단위로 작성함

- 앱등록

  - 프로젝트에서 앱을 사용하기 위해서는 반드시 INSTALLED_APPS리스트에 추가해야함
  - INSTALLED_APPS
    - Django installation에 활성화 된 모든 앱을 지정하는 문자열 목록


```python
#settings.py
INSTALLED_APPS = [
    'articles',]
```

- URLs

  - HTTP 요청을 알맞은 view로 전달

```python
#articles/urls.py
app_name = 'articles'
from . import views
path('index/', views.index, name='index'),
```

- View
  - HTTP 요청을 수신하고 HTTP 응답을 반환하는 함수 작성
  - Model을 통해 요청에 맞는 필요 데이터 접근
  - Template 에게 HTTP 응답 서식을 맡김

```python
#articles/views.py
def index(request):
    context={
    }
    return render(request, 'articles/index.html', context)
```

- Template

  - 실제 내용을 보여주는데 사용되는 파일
  - 파일의 구조나 레이아웃을 정의(ex, HTML)
  - Template 파일 경로의 기본 값은 app 폴더 안의 templates 폴더로 저장되어 있음

- 추가설정

  - LANGUAGE_CODE
    - 모든 사용자에게 제공되는 번역을 결정
    - 이 설정이 적용되려면 USE_I18N이 활성화 되있어야 함
  - TIME_ZONE
    - 데이터베이스 연결의 시간대를 나타내는 문자열 지정
    - USE_TZ 가 True이고 이 옵션이 설정된 경우 데이터베이스에서 날짜 시간을 읽으면 UTC 대신 새로 설정한 시간대의 인식 날짜&시간이 반환됨

  ```python
  #settings.py
  LANGUAGE_CODE = 'ko-kr'
  TIME_ZONE = 'Asia/Seoul'
  ```

  ### 

  - 

# TEMPLATE

### Django Template

- 데이터 표현을 제어하는 도구이자 표현에 관련된 로직
- 사용하는 built-in system
  - Django template language

### Djang Template Language(DTL)

- Djnago tempalte에서 사용되는 built-in template system
- 조건, 반복, 치환, 변수, 필터 등의 기능을 제공
- 단순히 Python이 HTML에 포함 된 것이 아니며, 단순히 프로그래밍적 로직이 아니라 프레젠테이션을 표현하기 위한 것
- Python 처럼 일부 프로그래밍 구조(if, for 등)를 활용할 수 있지만, 이것은 해당 Python 코드로 실행되는 것이 아님

### DTL Syntax

1. Variable
2. Filters
3. Tags
4. Comments

### DTL Syntax-Variable

{{ variable }}

- render()를 사용하여, [`views.py`](http://views.py)에서 정의한 변수를 template 파일로 넘겨 사용하는 것
- 변수명은 영어, 숫자와 밑줄(_)의 조합으로 구성될 수 있으나 밑줄로는 시작될 수 없음
  - 공백이나 구두점 문자 사용할 수 없음
- dot(.)을 사용하여 변수 속성에 접근할 수 있음
- render()의 세번째 인자로 {’key’: value} 와 같이 딕셔너리 형태로 넘겨주며, 여기서 정의한 key에 해당하는 문자열이 template에서 사용 가능한 변수명이 됨

### DTL Syntax-Filters

{{ variable|filter }}

- 표시할 변수를 수정할 때 사용
- 예시)
  - name 변수를 모두 소문자로 출력
  - {{  name|lower  }}
- 60개 bulit-in template filters를 제공
- chained 가 가능하며 일부 필터는 인자를 받기도 함
  - {{ variable|trunvateword:30 }}

### DTL Syntax-Tags

{% tag %}

- 출력 텍스트를 만들거나, 반복 또는 논리를 수행하여 제어 흐름을 만드는 등 변수보다 복잡한 일들을 수행
- 일부 태그는 시작과 종료태그가 필요
  - {%  if  %}{%  endif  %}
- 약 24개의 built-in template tags를 제공

### DTL Syntax-Comments

{#  #}

- Djnago template에서 라인의 주석을 표현하기 위해 사용
- 여러줄 주석은 {%  comment  %}{%  endcomment  %} 사용

## 코드작성순서

- 데이터 흐름에 맞추어 작성

1. `urls.py`
2. `views.py`
3. `templates`

### Template ingeritance(템플릿 상속)

- 템플릿 상속은 기본적으로 코드의 `재사용성`에 초점을 맞춤

- 템플릿 상속을 하면 사이트의 모든 공통 요소를 포함하고, 하위 템플릿이 `재정의(override)`할 수 있는 블록을 정의하는 기본 “skeleton” 템플릿을 만들 수 있음

- `{% extends=''%}`

  - 자식 템플릿이 부모 템플릿을 확장한다는 것을 알림
  - 반드시 템플릿 최상단에 작성 되어야 함

- `{%blcok content%} {%endblock%}`

  - 하위 템플릿에서 `재지정(overridden)`할 수 있는 블록을 정의
  - 즉 하위 템플릿이 채울 수 있는 공간

- app_name/templates 디렉토리 외 템플릿 추가경로 설정

  ```python
  #procjec_name/settings.py
  TEMPLATES=[
  	'DIRS' : [BASE_DIR / 'templates'] ,
  ]
  ```

  ```html
  <!--folder_name/templates/base.html-->
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="<https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css>" rel="stylesheet" integrity="sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We" crossorigin="anonymous">
    <title>Document</title>
  </head>
  <body>
    <div class="container">
      {% block content %}
      {% endblock content%}
    </div>
    <script src="<https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.bundle.min.js>" integrity="sha384-U1DAWAznBHeqEIlVSCgzq+c9gqGAJn5c/t99JyeKa9xxaYpSvHU5awsuZVVFIhvj" crossorigin="anonymous"></script>
  </body>
  </html>
  ```

- `Template Tag -”include”`

  - `{% include ‘’ %}`
  - 템플릿을 로드하고 현재 페이지로 렌더링
  - 템플릿 내에 다른 템플릿을 포함하는 방법
  - ex) templates 폴더에 nav.html을 만들고, base.html에서 include를 하는 것이다.

### Django template system(Django 설계철학)

- `표현`과 `로직(view)`을 분리
  - 템플릿 시스템은 표현을 제어하는 도구이자 표현에 관련된 로직일 뿐이라고 생각한다.
  - 즉, 템플릿 시스템은 이러한 기본 목표를 넘어서는 기능을 지원하지 말아야 한다.
- 중복을 배제
  - 대다수의 동적 웹사이트는 공통 header, footer, navbar 같은 사이트 공통 디자인을 갖는다.
  - Django 템플릿 시스템은 이러한 요소를 한 곳에 저장하기 쉽게 하여 중복 코드를 없애야 한다.
  - 이것이 템플릿 상속의 기초가 되는 철학이다.

# URL

### Django URLs

- Dispatcher(발송자, 운항 관리자)로서의 URL
- 웹 애플리케이션은 URL을 통한 클라이언트의 요청에서부터 시작됨

### Varialbe Routing

- URL 주소를 변수로 사용하는 것

- URL의 일부를 변수로 지정하여 view 함수의 인자로 넘길 수 있음

- 즉, 변수 값에 따라 하나의 path()에 여러 페이지를 연결시킬 수 있음

- ex)

  - path(’accounts/user/

    int:user_pk

    /’,...)

    - accounts/user/1 → 1번 user 페이지
    - accounts/user/2 → 2번 user 페이지

- `str`

  - ‘/’를 제외하고 비어있지 않은 모든 문자열과 매치
  - 작성하지 않은 경우 기본값

- `int`

  - 0 또는 양의 정수와 매치

- `slug`

  - ASCII 문자 또는 숫자, 하이픈 및 밑줄 문자로 구성된 모든 슬러그 문자열과 매치
  - ex) building-your-1st-django-site

### App URL mapping

- app의 view 함수가 많아지면서 사용하는 paht() 또한 많아지고, app 또한 더 많이 작성되기 때문에 프로젝트의 urls.py에서 모두 관리하는 것은 프로젝트 유지보수에 좋지 않음
- 이제는 각 app에 `urls.py` 를 작성하게 됨

```python
#project_name/urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')), #이제 articles.urls에서 관리해라
]

#app_name/urls.py
app_name = 'articles' #이름설정해주기
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name="new"),
    path('create/', views.create, name="create"),
    #pk는 database의 id값
    path('<int:pk>/', views.detail, name="detail"),
    path('<int:pk>/delete/', views.delete, name="delete"),
    path('<int:pk>/edit/', views.edit, name="edit"),
    path('<int:pk>/update/', views.update, name="update"),
]
```

- `include( )`
  - 다른 URLconf(app1/urls.py)들을 참조할 수 있도록 도움
  - 함수 include()를 만나게 되면, URL의 그 시점까지 일치하는 부분을 잘라내고, 남은 문자열 부분을 후속 처리를 위해 include된 URLconf로 전달
- Djnago는 명시적 상대경로(from .module import ..)를 권장



### Naming URL patterns

- 이제는 링크에 url을 직접 작성하는 것이 아니라 `path( )`함수의 name 인자를 정의해서 사용
- Django Template Tag 중 하나인 url 태그를 사용해서 `path( )` 함수에 작성한 name을 사용할 수 있음
- url 설정에 정의된 특정한 경로들의 의존성을 제거할 수 있음

```python
path('index/',views.index,name='index'),

<a href="{%url 'index'%}">메인페이지</a>
```

- {%url ‘’%}
  - 주어진 URL 패턴 이름 및 선택적 매개 변수와 일치하는 절대 경로 주소를 반환
  - 템플릿에 URL을 하드 코딩하지 않고도 DRY원칙을 위반하지 않으면서 링크를 출력하는 방법

# 2022 03/08~3/10

## 1. 기본세팅

1) vs코드 열기, 가상화면 `python -m venv venv`

2) 가상환경 실행 `source  venv/Scripts/activate`

3) 인터프리터 설정 

4) 장고 설치 `pip install django==3.2.12`

5) `django-admin startproject '프로젝트 이름'`

6) `python manage.py startapp '앱 이름'`

7) `INSTALLED_APPS` 에 '앱 이름' 추가

8) `URLS` 작성

9) 프로젝트에서

   ``` python
   #project/urls.py
   #아티클즈의 urls은 아티클즈가 관리해
       path('articles/', include('articles.urls')),
   ```

   

10) '앱'에 `urls.py` 설정해주기

    ```python
    #articles/urls.py
    app_name = 'articles'
    from . import views
    path('index/', views.index, name='index'),
    ```

10. `app`의 `view` 함수 설정

    ```python
    #articles/views.py
    def index(request):
        context={
        }
        return render(request, 'articles/index.html', context)
    ```

11. templates / 앱이름 폴더 만들고 안에 `index.html` 생성

    ```django
    <!--articles/templates/articles/index.html-->
    {% extends 'base.html' %}
    
    {% block content %}
    <h1>인덱스야 !</h1>
    
    {% endblock content %}
    ```

    

12. 상위 폴더에서 templates 만들고, 안에 base.html 생성

    ```django
    <!--/templates/articles/base.html-->
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Document</title>
    </head>
    <body>
      {% block content %}
      
      
      {% endblock content %}
    </body>
    </html>
    ```

    

13. throw 를 `urls` 설정, `view`함수로 만들기

    ```python
    #app/urls.py
    	path('throw/', views.throw, name='throw'),
        path('catch/', views.catch, name='catch'),
        
    #app/views.py
    
    def throw(request):
    
        context={
    
        }
        return render(request, 'articles/throw.html', context,)
    def catch(request):
        data = request.GET.get("content")
        context={
            "data" : data,
        }
        return render(request, 'articles/catch.html', context)	
    ```

14. 각각 `html` 작성

    ```python
    #app/templates/app/throw.html
    
    {% extends 'base.html' %}
    
    {% block content %}
    <h1>throw!</h1>
    <form action="{% url 'articles:catch' %}">
      <label for="content">content</label>
      <input type="text", id="content" name="content">
      <br>
      <input type="submit">
    </form>
    
    {% endblock content %}
    
    #app/templates/app/catch.html
    {% extends 'base.html' %}
    
    {% block content %}
    <h1>catch 야!</h1>
    <p>{{ data }}</p>
    
    
    {% endblock content %}
    ```

    

<hr> 

## 2. Database

- `데이터 베이스`

  - 체계화된 데이터의 모임

    

- `쿼리`

  - 데이터를 `조회`하기 위한 `명령어`

  - 조건에 맞는 데이터를`추출`하거나 `조작`하는 `명령어`

  - Query를 날린다 -> DB를 조작한다.

    

- `스키마`

  - 데이터 베이스에서 자료의 구조 , 표현방법, 관계 등을 `정의`한 구조(structure)

    

- `테이블`

  - 열과 행의 모델을 사용해 조직된 데이터 요소들의 집합, SQL데이터 베이스에서는 테이블을 관계 라고도 한다.

  - `열(column) : 필드(field) or 속성` x축

  - `행(row) : 레코드(record) or 튜플` y축

    - 테이블의 데이터는 행에 저장된다.

  - `기본키(PK)` 각 행의 `고유값`으로 Primary Key로 불린다. 반드시 설정하여야하며, 데이터베이스 관리 및 관계 설정시 주요하게 활용된다.

    

- `모델`

  - 단일한 데이터에 대한 정보를 가짐

    - 사용자가 저장하는 데이터들의 필수적인 필드들과 동작들을 포함

  - 저장된 데이터베이스의 구조(layout)

  - Django는 `model`을 통해 데이터에 접속하고 관리

  - 일반적으로 각각의 model은 하나의 데이터베이스 테이블에 매핑 됨

    

- `ORM`

  - Object-Relational-Mapping

  - 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템간에 (Django-SQL) 데이터를 변환하는 프로그래밍 기술

  - OOP 프로그래밍에서 RDBMS을 연동할 때, 데이터베이스와 객체 지향 프로그래밍 언어 간의 호환되지 않는 데이터를 변환하는 프로그래밍 기법

  - django는 내장 django ORM을 사용함

    

- ORM의 장점과 단점

  - 장점

    - SQL을 잘 알지 못해도 DB 조작이 가능
    - SQL의 절차적 접근이 아닌 객체 지향적 접근으로 인한 높은 생산성

  - 단점

    - ORM만으로 완전한 서비스를 구현하기 어려움

  - 현대 웹 프레임워크의 요점은 웹 개발의 속도를 높이는 것(**생산성**)🤣

    

- 왜 ORM을 사용하는가

  - 우리는 DB를 객체로 조작하기 위해 ORM을 사용한다.

  

- 각 모델은 django.models.Model 클래스의 서브 클래스로 표현됨

  - django.db.models 모듈의 Model 클래스를 상속받음

  - models 모듈을 통해 어떠한 타입의 DB 컬럼을 정의할 것인지 정의

    - title과 content은 모델의 `필드`를 나타냄
    - 각 필드는 클래스 속성으로 지정되어 있으며, 각 속성은 각 데이터베이스의 열에 `매핑`

    ```python
    #articles/models.py
    
    class Articles(models.Model):
    	title = models.CharField(max_length=10)
    	content = models.TextField()
    ```

    

- 사용 모델 필드

  - `CharField(max_length=10)`

  - `TextField(**options)`

    - 글자의 수가 많을 때 사용
    - max_length 옵션 작성시 자동 양식 필드인 textarea 위젯에 

  - ```python
    #articles/models.py
    
    from django.db import models
    
    # Create your models here.
    # 장고의 데이터 베이스
    
    class Article(models.Model):
        title = models.CharField(max_length=10)
        content = models.TextField()
    ```

    

- `Migrations`

  - Django가 model에 생긴 `변화를 반영`하는 방법

  - Migration 실행 및 DB 스키마를 다루기 위한 몇가지 명령어

  - 앞에 `python manage.py +`

    

    - `makemigrations`

      - model을 `변경`한 것에 기반한 새로운 migration 생성

      - app/migrations/`__init__.py`이 살아있어야 함

      - 추가 모델 필드 작성 후 `makemigrations` 진행

        

    - `migrate`

      - 마이그레이션을 DB에 `반영`하기 위해 사용

      - 설계도를 DB에 반영하는 과정

      - 모델에서의 변경 사항들과 DB의 스키마 

        

    - `sqlmigrate`

      - 마이그레이션에 대한 `SQL 구문`을 보기 위해 사용

      - 마이그레이션이 SQL 문으로 어떻게 해석되어서 동작할지 미리 `확인` 할 수 있음

        

    - `showmigrate`

      - 프로젝트 `전체의 마이그레이션 상태를 확인`하기 위해 사용

      - 마이그레이션 파일들이 migrate 됐는지 안됐는지 여부를 확인할 수 있음

        

    - `$ python manage.py makemigrations`

      - `migrations/0001_initial.py` 생성 확인

        
    
    - ```bash
      $ python manage.py makemigrations
      
      Migrations for 'articles':
        articles\migrations\0001_initial.py
          - Create model Article
      (venv) 
      
      
      ```
      
      - `0001_initial.py` 설계도를 실제 DB에 반영
      
      
      
    - migrations의 init - (연결) -migration - (연결) - db.sqlite3
    
    
    
    - DataField's options
    
      - `auto_now_add`
        - 최초 생성일자
        - django ORM이 최초 inset(테이블에 데이터 입력)시에만 현재 날짜와 시간으로 갱신 (테이블에 어떤 값을 최초로 넣을 때)
      - `auto_now`
        - 최종 수정 일자
        - django ORM이 save를 할 때마다 현재 날짜와 시간으로 갱신
    
      ```python
      #articles/models.py
      class Article(models.Model):
          #title 기록가능
          title = models.CharField(max_length=10)
          
          #content 기록가능
          content = models.TextField()
      
          #시간 자동생성
          created_at = models.DateTimeField(auto_now_add=True)
          updated_at = models.DateTimeField(auto_now=True)
      ```
      
      
    
    ![image-20220310095611228](readme.assets/image-20220310095611228.png)
    
    
    
    - 반드시 기억해야할 migration 3단계
      - 1.`models.py`
        - 모델 변경사항시
      - `$ python manage.py makemigrations`
        - migrations 파일 생성
      - `$ python manage.py migrate`
        - DB반영 (모델과 DB의 동기화)

<hr/>

## 2. DB API

-  DB를 조작하기 위한 `도구`
- Django 가 기본적으로 ORM을 제공함에 따른 것으로 DB를 편하게 조작할 수 있도록 도움
- Model 을 만들면 Django 는 객체를 만들고 읽고 수정하고 지울 수 있는 database-abstract API 를 자동으로 만듦
- database-abstract API
- `Manager`
  
  - Django 모델에 데이터 베이스 query 작업이 제공되는 인터페이스
  - 기본적으로 모든 Django 모델 클래스에 objects라는 Manager를 추가
- `QuerySet`
  
  - 데이터베이스로부터 전달받은 객체 목록
  - queryset안의 객체는 0개 , 1개 혹은 여러 개일 수 있음
  - 데이터베이스로부터 조회, 필터, 정렬 등을 수행할 수 있음
  
- `Article.objects.all( )`

  - Class Name Manager QuerySet Api

- `django Shell`

  - 일반 Python shell을 통해서는 장고 프로젝트 환경에 접근할 수 없음

  - 그래서 장고 프로젝트 설정이 load 된 Python shell을 활용해 DB API 구문 테스트 진행

  - 기본 django Shell 보다 더 많은 기능을 제공하는 `shell_plus`를 사용하여 진행

    - `Django-extensions` 라이브러리의 기능 중 하나

  - 라이브러리 설치

    ```bash
    $ pip install ipython
    $ pip install django-extensions
    
    #settings.py
    INSTALLED_APPS=[
    	'django-extensions',
    ]
    
    #shell 실행
    $ python manage.py shell_plus
    
    ```

<hr/> 

## 3. CRUD

- 대부분 컴퓨터 소프트웨어가 가지는 기본적인 데이터 처리기능인
  - `Create, Read, Update, Delete`를 일컫는 말

- `Article.objects.all( )`

### 1) Create

```shell
#추가하는 세가지 방법

In [3]: article = Article()

In [4]: article.title = "first"

In [5]: article.content = "1st content"

In [6]: article.save()

##############################################

In [7]: article = Article(title="second", content="2nd content")     

In [8]: article.save()

##############################################

In [9]: Article.objects.create(title="third", content="3rd content") 
   ...: 
```

### create 관련 메서드

- `save( ) method`
  
  - saving object
  - `객체`를 데이터 베이스에 `저장`함
  - 데이터 생성 시 save()를 호출하기 전에는 객체의 ID값이 무엇인지 알 수 없음
    - ID 값은 Django가 아니라 DB에 계산되기 때문
  - 단순히 모델을 인스턴스화 하는 것은 DB에 영향을 미치지 않기 때문에 반드시 save()가 필요
  
- `str method`

  ```python
  #model.py
  
  def __str__(self):
          return f"제목 : {self.title}"
  ```

  - 표준 파이썬 클래스 메소드인 str()을 정의하여 각각의 object가 사람이 읽을 수 있는 문자열을 반환하도록 할 수 있음
  - 작성 후 반드시 shell_plus를 재시작해야 반영됨

  

### 2) Read

- `all( )`

  - 현재 `QuerySet`의 복사본을 반환

- `get( )` 

  - 주어진 `lookup 매개변수와 일치하는 객체를 반환`
  - 객체를 찾을 수 없으면 DoesNotExist 예외를 발생시킴
  - `Article.objects.get(title="second")`
  - id값이 중복된경우
    - get() returned more than one 
      Article -- it returned 2!
    - 가져올 수 없음

- `filter( )`

  - 주어진 lookup

  ```shell
  In [8]: Article.objects.get(title="second")
  Out[8]: <Article: 제목 : second>
  
  In [9]: Article.objects.filter(title="second")        
  Out[9]: <QuerySet [<Article: 제목 : second>]>
  
  In [10]: type(Article.objects.get(title="second"))    
  Out[10]: articles.models.Article
  
  In [11]: type(Article.objects.filter(title="second")) 
      ...: 
  Out[11]: django.db.models.query.QuerySet
  ```

  

### 3) Update

```shell
In [12]: article = Article.objects.get(pk=1)

In [13]: article.pk
Out[13]: 1

In [14]: article.title
Out[14]: 'first'

In [15]: article.title = "change"

In [16]: article.content = "changed content"

In [17]: article.title
Out[17]: 'change'
#값을 저장해줘야함 article.save()
```



### 4) Delate

- QuerySet의 모든 행에 대해 SQL 삭제 쿼리를 수행하고 삭제된 객체 수와 객체 유형당 삭제 수가 포함된 딕셔너리를 반환

  ```shell
  article.delete()
  ```

### Field lookups

- 조회시 특정 검색 조건을 지정
- QuerySet 메서드 filter(), exclude() 및 get()에 대한 키워드 인수로 지정됨
- 사용예시)
  - Articles.objects.filter(pk__gt=2)
  - Articles.objects.filter(content__contains='ja')



<hr/>

## 4. Admin site

### 개요

- 사용자가 아닌 서버의 관리자가 활용하기 위한 페이지

- Model class를 `admin.py`에 등록하고 관리

- django.contib.auth 모듈에서 제공됨

- record 생성 여부 확인에 매우 유용하며, 직접 record를 삽입할 수 있음

  

### 생성

```bash
#실행
$ python manage.py createsuperuser

##
Username: hangkim
Email address: 
Password:

#여기서 주의할 점은, 패스워드는 입력해도 터미널창에 뜨지 않는다. 이것 때문에 계속 안되는줄 알았다.😂
```

- 관리자 계정 생성 후 서버를 실행한 다음 /admin 페이지로 가서 로그인

  - 계정만 만든 경우 Django 관리자 화면에서 아무것도 보이지 않음

- 내가 만든 Model을 보기 위해서는 admin.py에 작성하여 Django 서버에 등록

- [주의] auth에 관련된 기본 테이블이 생성되지 않으면 관리자 계정을 생성할 수 없음

  

### 등록

```python
#articles/admin.py
from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','content','pk','created_at','updated_at')
    
admin.site.register(Article, ArticleAdmin)
```

- admin.py는 관리자 사이트에 Article 객체가 관리자 인터페이스를 가지고 있다는 것을 알려주는 것

- models.py에 정의한  `__Str__ `의 형태로 객체가 표현됨

  

### 옵션

- `list_display`
  - models.py 정의한 각각의 속성(컬럼)들의 값(레코드)을 admin 페이지에 출력하도록 설정
- `list_filter, list_display_lins` 등 다양한 ModelAdmin 옵션 참고

### index.html

```django
<!--articles/templates/articles/index.html-->

{% extends 'base.html' %}

{% block content %}
  <h1>Articles</h1>
  <hr>
  {% for article in articles %}
    <p>제목 : {{  article.title  }}</p>
    <p>내용 : {{ article.content  }}</p>
    <hr>
  {% endfor %}
{% endblock content%}

```

### 실행

- `makemigration, migrate`해주고 `showmigrations` 를 해줘야 한다.

### 기타

- url이랑 /랑 쓰이는 차이
- url
  - articles:index
  - url로 요청
- render : articles/index.html 
  - 물리적인 위치
  - html 파일을 실행시켜줘





## 5. CRUD 직접해보기

1) 프로젝트 이름
   - crud
2) 앱이름
   - articles
3) 앱등록
   - base 템플릿 작성 및 TEMPLATES에서 경로 등록

4. `index 페이지` 작성

   ```django
   <!--articles/templates/articles/index.html-->
   
   {% extends 'base.html' %}
   
   {% block content %}
     <h1>Articles</h1>
     
     <hr>
     <a href="{%url 'articles:new' %}">게시글 작성</a>
     <hr>
     {% for article in articles %}
       <p>제목 : 
   
         <a href="{%url 'articles:detail' article.pk%}">{{  article.title  }}</a>
       </p>
       <hr>
       
     {% endfor %}
   {% endblock content%}
   ```

5. `views.py` 작성

   ```python
   #articles/view.py
   
   def index(request):
       #모든 글을 조회(거꾸로 가져오기)
       articles = Article.objects.all()[::-1]
       #컨텍스트에 넣어줌
       context={
           'articles' : articles
       }
       return render(request, 'articles/index.html',context)
   ```

   1) HTTP method

   - `GET`

     - 특정 리소스를 `가져오도록 요청`할 때 사용

     - 반드시 데이터를 가져올 때만 사용해야함

     - DB 에 변화를 주지 않음

     - CRUD에서 `Read` 역할을 담당

       

   - `POST`

     - 서버로 데이터를 `전송`할 때 사용

     - 리소스를 생성/변경하기 위해 데이터를 HTTP body에 담아 전송

     - 서버에 변경사항을 만듦

     - CRUD에서 `Create/Update/Delete` 역할을 담당

       

   2) 사이트간 요청 위조

      - 웹 애플리케이션 취약점 중 하나로 사용자가 자신의 의지와 무관하게 공격자가 의도한 행동을 하여 특정 웹페이지를 보안에 취약하게 하거나 수정, 삭제 등의 작업을 하게 만드는 방법

      - Django는 CSRF에 대항하여 `middleware`와 `template tag`를 제공

      - `CSRF`라고도 함

        

   3) CSRF 공격 방어

   - Security Token 사용 방식(CSRF Token)

     - 사용자의 데이터에 임의의 난수 값을 부여해,  매 요청마다 해당 난수 값을 포함시켜 전송 시키도록 함

     - 이후 서버에서 요청을 받을 때마다 전달된 token 값이 유효한지 검증

     - 일반적으로 데이터 변경이 가능한 POST, PATCH, DELETE Method 등에 적용(GET은 제외)

     - Django는 CSRF token 템플릿 태그를 제공

     - csrf_token template tag

       

   - `{% csrf_token %}`

     - input type이 hidden으로 작성되며 value는 Django에서 생성한 hash 값으로 설정됨

     - 해당 태그 없이 요청을 보낸다면 Django 서버는 403 forbidden을 응답

     - CsrfViewMiddleware

     - CSRF 공격 관련 보안 설정은 settings.py 에서 MIDDLEWARE에 작성 되어 있음

     - 실제로 요청 과정에서 urls.py 이전에 Middleware의 설정 사항들을 순차적으로 거치며 응답은 반대로 하단에서 상단으로 미들웨어를 적용시킴

       

   - MiddleWare

     - 공통 서비스 및 기능을 애플리케이션에 제공하는 소프트웨어
     
     - 데이터 관리, 애플리케이션 서비스, 메시징, 인증 및 API 관리를 주로 미들웨어를 통해 처리
     
     - 개발자들이 애플리케이션을 보다 효율적으로 구축할 수 있도록 지원하며, 애플리케이션, 데이터 및 사용자 사이를 연결하는 요소처럼 작동
     
       

6. new 페이지 작성

   - new 페이지는 글제목, 내용 작성하는 페이지임

   ```django
   #articles/templates/articles/new.html
   {% extends 'base.html' %}
   
   {% block content %}
     <h1>New</h1>
   	<!--create로 내용을 쏴준다. POST방식으로-->
     <form action="{% url 'articles:create' %}" method="POST">
       <!--csrf_token으로 보안화-->
       {% csrf_token %}
       <label for="title">제목 : </label>
       <input type="text" name="title" id="title"></br></br>
       <label for="content">내용 : </label>
   	
   	<!--textarea는 글상자-->
       <textarea name="content" id="content" cols="30" rows="10"></textarea></br></br>
       <input type="submit">
     </form>
   {% endblock content %}
   ```

   ```python
   #articles/view.py
   def create(request):
       #new에서 넘긴걸 받는
       title = request.POST.get('title')
       content = request.POST.get('content')
   
       article = Article()
       article.title = title
       article.content = content
       article.save()
   
       #return render(request, 'articles/index.html')
       return redirect('articles:detail', article.pk)
   ```

   - render를 안쓰는 이유
     1) 글을 작성 후 index 페이지가 출력되지만 게시글이 조회되지 않음
     2) URL은 여전히 create에 머물러 있음
        - 단순히 index 페이지만 render 되었을 뿐
        - create view 함수에서 다루고 있는 데이터로 index 페이지가 render됨
     
   - `redirect( )`
     
     - 새 URL로 요청을 다시 보냄
     
     - 인자에 따라 HttpResponseRedirect를 반환
     
     - 브라우저는 현재 경로에 따라 전체 URL 자체를 재구성(reconstruct)
     
     - 사용 가능한 인자
       1. model
       
       2. view name: viewname can be URL pattern name or callable view object
       
       3. absolute or relative URL
       
          

   10. 게시글 상세 페이지 Detail 페이지 작성

     ```python
     #articles/urls.py
      path('<int:pk>/', views.detail, name="detail"),
     ```

     - 글번호 pk를 활용해서 각각 페이지를 따로 구현해야함
     - Variable Routing 활용

     ```python
     #articles/views.py
     def detail(request, pk):
         #all이 아닌 이유는 한개만 가져올거여서
         article = Article.objects.get(pk=pk)
         context = {
             'article' : article,
         }
         return render(request, 'articles/detail.html', context)
     ```

     - 오른쪽 pk는 variable routing을 통해 받은 pk
     - 왼쪽 pk는 DB에 저장된 레코드의 pk(id)

     ```django
     <!-- articles/template/detail.html-->
     {% extends 'base.html' %}
     
     {% block content %}
       <h1>{{ article.pk }}번째 글</h1>
       <hr>
       <p>제목 : {{  article.title  }}</p>
       <p>내용 : {{  article.content  }}</p>
       <p>작성시간 : {{  article.created_at  }}</p>
       <p>수정시간 : {{  article.updated_at  }}</p>
       <hr>
       <!-- article:delete로 요청-->
       <form action="{% url 'articles:delete' article.pk %}" method="POST">
         {% csrf_token %}
         <button>삭제하기</button>
       </form>
       
       </br>
       <a href="{% url 'articles:edit' article.pk%}">
         <button>수정하기</button>
       </a>
       <a href="{% url 'articles:index' %}">
         <button>처음으로</button>
       </a>
     {% endblock content %}
     ```

     

11. DELETE 구현

    ```python
    #article/views.py
    def delete(request,pk):
        #가져온다음
        article = Article.objects.get(pk=pk)
        if request.method == "POST":
            
            #포스트일 경우만 지움
            article.delete()
    
        #redirect는 path가 들어가야함
            return redirect('articles:index')
        else:
            #아니면 글 detail로
            return redirect('articles:detail', article.pk)
    ```

    ```django
    <!-- articles/detail.html 에서 delete 버튼 만들기--!
    <!-- article:delete로 요청-->
      <form action="{% url 'articles:delete' article.pk %}" method="POST">
        {% csrf_token %}
        <button>삭제하기</button>
      </form>
    
    ```

12. EDIT 구현

    - 수정은 기존에 입력 되어 있던 데이터를 보여주는 것이 좋기 때문에 html 태그의 value 속성을 사용
    - textarea 태그는 value 속성이 없으므로 태그 내부 값으로 작성

    ```python
    # article/urls.py
    path('<int:pk>/edit/', views.edit, name="edit"),
    ```

    ```python
    #article/views.py
    def edit(request, pk):
        article = Article.objects.get(pk=pk)
        context={
            'article' : article
        }
        return render(request, 'articles/edit.html', context)
    ```

    ```django
    <!-- article/edit.html-->
    {% extends 'base.html' %}
    
    {% block content %}
      <h1>Edit</h1>
    
      <form action="{% url 'articles:update' article.pk %}" method="POST">
        {% csrf_token %}
        <label for="title">제목 : </label>
        <input type="text" name="title" id="title" value="{{ article.title }}"></br></br>
        <label for="content">내용 : </label>
        <textarea name="content" id="content" cols="30" rows="10">{{ article.content }}</textarea></br></br>
        <input type="submit">
      </form>
    {% endblock content %}
    ```

    - detail.html 에 edit 링크 작성

    ```django
    <!--articles/templates/detail.html-->
    <a href="{% url 'articles:edit' article.pk%}">
        <button>수정하기</button>
      </a>
    ```

13. 느낀점
    - 이것을 일일히 계속해서 바꿔나가기보다는 처음부터 구상을 한 후 같다 붙이는 것이 효율적으로 생각된다.
    - 따라서 개념을 익히되 나만의 템플릿으로 활용하는 편이 좋다고 생각된다.



# **DATABASE**

- 데이터베이스는 **체계화된 데이터**의 모임
- 여러 사람이 공유하고 사용할 목적으로 통합 관리되는 정보의 집합
- 논리적으로 연관된(하나 이상의) 자료의 모음으로 그 내용을 고도로 구조화 함으로서 검색과 갱신의 효율화를 꾀한 것
- 즉, **몇개의 자료 파일을 조직적으로 통합하여 자료 항목의 중복을 없애고 자료를 구조화하여 기억시켜 놓은 자료의 집합체**

- 데이터 베이스로 얻는 장점들
  - 데이터 중복 최소화
  - 데이터 무결성(정확한 정보를 보장)

## 관계형 데이터베이스(RDB)

- Relation Database
- key 와 value 값들의 간단한 관계를 table 형태로 정리한 데이터 베이스
- 관계형 모델에 기반
- ex)엑셀

- 스키마(schema) : 데이터베이스에서 자료의 구조, 표현방법, 관계등 전반적인 명세를 기술한 것.
- 테이블 : 열(컬럼/필드)과 행(레코드/값)의 모델을 사용해 조직된 데이터 요소들의 집합
- -이미지

- 열(column) : 각 열에는 고유한 데이터 형식이 지정됨.
- 아래의 예시에서는 name이란 필드에 고객의 이름(TEXT)이 저장됨

- 행(row) : 실제 데이터가 저장되는 형태
- 아래의 예시에서는 총 3명의 고객정보가 저장되어 있음(레코드가 3개)

- 기본키(Primary Key) : 각 행(레코드)의 고유값
- 반드시 설정해야 하며, 데이터베이스 관리 및 관계 설정 시 주요하게 활용 됨



## RDBMS

- 관계형 데이터 베이스 관리 시스템
- ex)
  - MySQL
  - SQLite
  - ORACLE
  - MS SQL

### SQLite

- 서버 형태가 아닌 파일 형식으로 응용프로그램에 넣어서 사용하는 비교적 가벼운 데이터 베이스
- 구글 안드로이드 운영체제에 기본적으로 탑재된 데이터베이스이며, 임베디드 소프트웨어에도 많이 활용됨
- 로컬에서 간단한 DB 구성을 할 수 있으며, 오픈소스 프로젝트이기 때문에 자유롭게 사용가능

### Sqlite Data Type

1. NULL (파이썬에서는 None)
2. INTEGER
   - 크기에 따라 0,1,2,3,4,5 또는 8바이트에 저장된 부호 있는 정수
3. REAL
   - 8바이트 부동 소수점 숫자로 저장된 부동 소수점 값
4. TEXT
5. BLOB
   - 입력된 그대로 정확히 저장된 데이터(별다른 타입 없이 그대로 저장)

### Sqlite Type Affinity

- Type Affinity

  - 특정 칼럼에 저장하도록 권장되는 데이터 타입

  1. INTEGER
  2. TEXT
  3. BLOB
  4. REAL
  5. NUMERIC



## 1.SQL (Structured Query Language)

- 관계형 데이터베이스 관리시스템(RDMBS)의 데이터관리를 위해 설계된 특수 목적 프로그래밍 언어

- 데이터베이스 스키마 생성 및 수정

- 자료의 검색 및 관리

- 데이터베이스 객체 접근 조정 관리

  

- **SQL 문법의 세가지 종류**

  - `DDL - 데이터 정의 언어`
    - CREATE
    - DROP
    - ALTER
  - `DML - 데이터 조작 언어`
    - INSERT : 새로운 데이터 삽입
    - UPDATE : 저장되어있는 데이터 갱신
    - DELETE : 저장되어있는 데이터 삭제
    - SELECT : 저장되어있는 데이터 조회
  - `DCL - 데이터 제어 언어`
    - GRANT
    - REVOKE
    - COMMIT
    - ROLLBACK

- 

  

## 2. Database 생성

> 해당하는 데이터베이스 파일이 있으면 해당DB를 콘솔로 연다. 
>
> 만약 해당하는 파일이 없으면 새로 생성하고, 해당 DB를 콘솔로 연다.

```sqlite
$ sqlite3 database

ex)
$ sqlite3 tutorial.sqlite3    // 1. 콘솔로 DB를 열고,
sqlite> .databases            // 2.데이터베이스 목록을 확인한다.
```



**CSV 파일 불러오는 명령어**

> 주의사항)
>
> `.`으로 시작하는 모든 명령어는 SQLite에서 데이터베이스를 조금 더 편리하게 다루기 위해 제공하는 명령어이며, SQL 문법에 속하지 않습니다.

```sqlite
sqlite> .mode csv
sqlite> .import 파일명.csv 테이블명

ex)
sqlite> .import users.csv users_user
```



## 3. 테이블 생성 및 삭제 

> 데이터 타입의 종류는 INTEGER, TEXT, REAL, NUMERIC, BLOB 등이 존재한다.
>
> 자세한 내용은 [SQLite3 공식문서](https://sqlite.org/datatype3.html)를 참조한다.



**테이블 생성 (CREATE)**

```sql
CREATE TABLE table (
	column1 datatype PRIMARY KEY,
  column2 datatype,
  ...
);
```



**테이블 생성 with NOT NULL 조건 예시**

```sql
CREATE TABLE table (
	id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  age INT NOT NULL,
  ...
);
```

 

**테이블 및 스키마 조회 명령어** **(!= SQL)**

```sqlite
sqlite> .tables          // 테이블 목록 조회
sqlite> .schema table    // 특정 테이블 스키마 조회
```



**테이블 제거 (DROP)**

```sql
sqlite> DROP TABLE classmates;
sqlite> .tables // 테이블 제거 확인
```



## 4. 데이터 추가, 읽기, 수정 및 삭제

**추가 (INSERT)**

```sql
INSERT INTO table (column1, column2, ...)
VALUES(value1, value2);
```

- SQLite 는 따로 PRIMARY KEY 속성의 컬럼을 작성하지 않으면 값이 자동으로 증가하는 PK옵션을 가진 rowid 컬럼을 정의

**조회 (SELECT)**

> 참고)
>
> SQL은 세미콜론(;)을 만나기 전까지 절대 실행되지 않습니다.
>
> 따라서 아래 LIMIT 예시와 같이 들여쓰기를 비교적 자유롭게 할 수 있습니다.

```sql
-- 모든 컬럼 가져오기 --
SELECT * FROM table;

-- 특정 컬럼 가져오기 --
SELECT column1, column2 FROM table;

-- LIMIT: 원하는 개수(num)만큼 가져오기 -- 
SELECT column1, column2
FROM table
LIMIT num;

-- OFFSET: 특정 위치에서부터 가져올 때 --
-- (맨 위부터 num만큼 떨어진 값부터 가져온다는 의미, 6번째 행부터, 10개 행을 조회, 0부터 시작함)
SELECT column1, column2
FROM table
LIMIT 10 OFFSET 5;

-- WHERE: 조건을 통해 값 가져오기 --
SELECT column1, column2
FROM table
WHERE column=value;

-- DISTINCT: 중복없이 가져오기 -- 
SELECT DISTINCT column FROM table;
```



**삭제 (DELETE)**

- 테이블에서 행 제거

```sql
DELETE FROM 테이블 이름
WHERE 조건;

ex)
DELETE FROM classmates
WHERE name='김싸피';
```



**수정 (UPDATE)**

- 기존 행의 데이터를 수정

```sql
UPDATE 테이블이름
SET column1=value1, column2=value2, ...
WHERE 조건;

ex)
-- 김싸피의 이름을 김삼성으로 바꾼다고 하면... --
UPDATE classmates
SET name='김싸피', address='대한민국'
WHERE name='김삼성';
```



**예시와 함께하는 WHERE문 심화 (READ)**

```sql
-- Q.users에서 age가 30이상인 사람만 가져온다면? --

SELECT * FROM users
WHERE age >= 30;
```

```sql
-- Q.users에서 age가 30이상인 사람의 이름만 가져온다면? --

SELECT first_name FROM users
WHERE age >= 30;
```

```sql
-- Q.users에서 age가 30이상이고 성이 김인 사람의 성과 나이만 가져온다면? --
SELECT age, last_name FROM users
WHERE age >= 30 and last_name='김';
```



## 5. 심화 SQL문

### Expressions

- COUNT (레코드 값들의 개수 반환)

  ```sql
  SELECT COUNT(*) FROM users;
  ```

- AVG (레코드 값들의 평균값 반환)

  ```sql
  #나이가 30 이상인 사람의 평균나이
  SELECT AVG(age)
  FROM users
  WHERE age >= 30;
  ```

- MAX (레코드 값들의 최대값 반환)

- MIN (레코드 값들의 최소값 반환)

- SUM (레코드 값들의 합 반환)



### LIKE

> LIKE는 두 가지 와일드 카드(언더스코어 그리고 퍼센트 기호)와 함께 동작한다.

- `-` (반드시 이 자리에 한 개의 문자가 존재해야 한다는 뜻)

  ```sql
  -- 20대인 사람들만 가져올 때 --
  SELECT *
  FROM users
  WHERE age LIKE '2_';
  ```

- `%` (이 자리에 문자열이 있을 수도, 없을 수도 있다. 0개 이상이라는 뜻)

  ```sql
  -- 지역번호가 02인 사람만 가져올 때 --
  SELECT *
  FROM users
  WHERE phone LIKE '02-%';
  ```

- 두 개를 조합해서 사용할 수도 있다.

  ```sql
  -- 핸드폰 중간 번호가 반드시 4자리면서 511로 시작되는 사람들 --
  
  SELECT * FROM users
  WHERE phone LIKE '%-511_-%';
  ```



**정렬 (ORDER BY)**

```sql
SELECT columns FROM table
ORDER BY column1, column2 ASC | DESC;

-- ASC: 오름차순 / DESC: 내림차순 --
```

```sql
-- 나이, 성 순서로 오름차순 정렬하여 상위 10개만 뽑아보면? --
SELECT * 
FROM users
ORDER BY age, last_name ASC
LIMIT 10;
```





**GROUP BY**

> 지정된 기준에 따라 행 세트를 그룹으로 결합한다.
>
> 데이터를 요약하는 상황에서 주로 사용한다.

```sql
SELECT column1, aggregate_function(column_2)
FROM table
GROUP BY column1, column2;
```

```sql
-- 성(last_name)씨가 몇 명인지 조회할 때 --
SELECT last_name, COUNT(*)
FROM users
GROUP BY last_name;
```



**ALTER**

- 테이블명 변경

  ```sql
  ALTER TABLE 기존테이블명
  RENAME TO 새로운테이블명;
  ```

- 새로운 컬럼 추가

  ```sql
  ALTER TABLE 테이블명
  ADD COLUMN 컬럼명 datatype;
  ```

  

