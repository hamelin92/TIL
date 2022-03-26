## Django

​	0. 기본세팅

1.  가상환경을 만든다

   ```bash
   python -m venv venv
   ```

   

1. 가상환경을 활성화시킨다

   ```bash
   source ./venv/Scripts/activate
   ```

   

2. 장고프로젝트를 만든다

   ```bash
   django-admin startproject {projectname} .
   ```

   

3. 장고 애플리케이션을 만든다

   ```bash
   python manage.py startapp articles(앱 명칭 복수형 권장)
   ```

   

5. settings.py의 INSTALLED_APPS 애플리케이션을 등록한다.

   Local app -> Third party app -> Django app  순서로 작성하길 권장

   ```python
   INSTALLED_APPS = [
       'articles(애플리케이션 이름)', #반드시 애플리케이션 먼저 생성 후 등록하기
       ...,
       ...,
   ]
   ```

   

5. urls.py로 url과 view를 매핑한다.

   ```python
   from articles import views # articles : 어플리케이션 이름
   
   urlpatterns = [
       path('admin/', admin.site.urls)
       path('index/', views.index)
   ]
   ```

   

6. view함수를 작성한다. -> 관련된 html 파일을 렌더한다.

   ```python
   from django.shortcuts import render
   
   def index(request):
       return render(request, 'index.html')
   ```

   

7. html파일을 만들어준다.

   1. 이때 앱 안에 templates라는 폴더 안에 해당 html파일을 만들어준다.



## 1.

### Web Framework

- Static web page (정적 웹페이지)
  - 서버에 미리 저장된 파일이 사용자에게 그대로 전달되는 웹 페이지
  - 서버가 정적 웹페이지에 대한 요청을 받은 경우 서버는 추가적인 처리과정 없이 클라이언트에게 응답을 보냄
  - 모든 상황에서 모든 사용자에게 동일한 정보를 표시
  - 일반적으로 HTML, CSS, JavaScript로 작성, flat page라고도 한다.
- Dynamic web page (동적 웹 페이지)
  - 웹 페이지에 대한 요청을 받은 경우 서버는 추가적인 처리 과정 이후 클라이언트에게 응답을 보냄
  - 동적 웹페이지는 방문자와 상호작용하기 때문에 페이지 내용은 그때그때 다름
  - 서버 사이드 프로그래밍 언어 (Python, Java, C++ 등)가 사용되며, 파일을 처리하고 데이터베이스와의 상호작용이 이루어짐.
- Framework
  - 프로그래밍에서 특정 운영 체제를 위한 응용 프로그램 표준 구조를 구현하는 클래스와 라이브러리 모임
  - 재사용할 수 있는 수많은 코드를 프레임워크로 통합함으로써 개발자가 새로운 애플리케이션을 위한 표준 코드를 다시 작성하지 않아도 같이 사용할 수 있도록 도움.
  - Application framework 라고도 함
  - Web framework - 웹 페이지를 개발하는 과정에서 겪는 어려움을 줄이는 것이 주 목적
  - 데이터베이스 연동, 템플릿 형태의 표준, 세션 관리, 코드 재사용 등의 기능을 포함
  - 동적인 웹 페이지나 웹 애플리케이션, 웹 서비스 개발 보조용으로 만들어지는 Application framework 의 일종
- Framework Architecture
  - MVC Design Pattern ( model - view - controller) / Django는 MTV라고 부름( model -template-view )
  - 소프트웨어 공학에서 사용되는 디자인 패턴 중 하나
  - 사용자 인터페이스로부터 프로그램 로직을 분리하여 애플리케이션의 시각적 요소나 이면에서 실행되는 부분을 서로 영향없이 쉽게 고칠 수 있는 애플리케이션을 만들 수 있음
- MTV Pattern
  - Model
    - 응용 프로그램의 데이터 구조를 정의하고 데이터베이스의 기록을 관리 ( 추가 수정 삭제 )
  - Template
    - 파일의 구조나 레이아웃을 정의
    - 실제 내용을 보여주는 데 사용 presentation
  - View
    - http 요청을 수신하고 http 응답을 반환
    - Model을 통해 요청을 충족시키는데 필요한 데이터에 접근
    - template에게 응답의 서식 설정을 맡김.
  - Model / View - Template / Controller - View
  - ![img](https://mdn.mozillademos.org/files/13931/basic-django.png)

​		

### Django Intro 구조

- Project
  - Project는 Application의 집합(collection of apps)
  - 프로젝트에는 여러 앱이 포함될 수 있음
  - 앱은 여러 프로젝트에 있을 수 있음
  - init.py  : 파이썬에서 이 디렉토리를 하나의 파이썬 패키지로 다루도록 지시
  - asgi.py : Asynchronous Server Gateway Interface
    - Django 애플리케이션이 비동기식 웹 서버와 연결 및 소통하는 것을 도움
  - settings.py : 애플리케이션의 모든 설정을 포함
  - urls.py : 사이트의 url과 적절한 views의 연결을 지정
  - wsgi.py : Web Server Gateway Interface
    - Django 애플리케이션이 웹서버와 연결 및 소통하는 것을 도움
  - manage.py : Django 프로젝트와 다양한 방법으로 상호작용하는 커맨드라인 유틸리티
    - python manage.py <command> [options]
- Application
  - 앱은 실제 요청을 처리하고 페이지를 보여주고 하는 등의 역할을 담당
  - 하나의 프로젝트는 여러 앱을 가짐
  - 일반적으로 앱은 하나의 역할 및 기능 단위로 작성함
  - admin.py : 관리자용 페이지를 설정 하는 곳
  - apps.py : 앱의 정보가 작성된 곳
  - models.py : 앱에서 사용하는 Model을 정의하는 곳
  - tests.py : 프로젝트의 테스트 코드를 작성하는 곳
  - views.py : view 함수들이 정의되는 곳

### 요청과 응답

- URLs

  - ```

