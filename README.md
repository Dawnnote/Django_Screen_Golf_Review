## :golf: Django 이용해서 골프 리뷰 사이트 구현하기 :golf:

## 개요

- HTML
- CSS
- Python
- Django

#### Django frame work 기술을 활용하여 골프 리뷰(커뮤니티) 사이트를 구현하는 프로젝트입니다.

- 직접 구현한 Main Page

<img src="https://user-images.githubusercontent.com/117843786/221415476-34a5d737-2146-4c8e-afb9-3a2c74cee008.png" width="70%" height="70%"/>

## [:pencil2: 프로젝트 결과 사이트 입장하기](http://dawnnote.pythonanywhere.com/)

## :pencil: Mini Project (2023/02/22 ~ 2023/02/27) :date:

### 팀명: UJS

#### > :family: 팀원

- [양효준](https://github.com/Hyojoon-Yang)
- [이재영F](https://github.com/pt0108)
- [이상훈](https://github.com/Dawnnote)
- [고석주](https://github.com/SeokJuGo)
- [지우근](https://github.com/UGeunJi)
- [강동엽](https://github.com/kdy1493)

### 시연 영상

[Main Page 시연 영상](#main-page-시연-영상)

[Navigation Bar 바 시연 영상](#navigation-bar-시연-영상)

[Side Bar 시연 영상](#side-bar-시연-영상)

---

## :dart: Trouble Shooting

---

## :stars: 더 구현하고 싶은 기능

- 소셜 로그인 기능 추가
- 스토어 만들기

---

## Code 및 시연 영상

## User Model 정의

```python
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    nickname = models.CharField(
        max_length=15,
        unique=True,
        null=True,
        validators = [validate_no_special_characters],
        error_messages={"unique":"이미 사용중인 닉네임입니다"},
    )

    profile_pic = models.ImageField(
        default="default_profile_pic.jpg", upload_to="profile_pics"
    )

    intro = models.CharField(max_length=60, blank=True)
    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        blank=True,
        related_name='followers'
    )

    def __str__(self):
        return self.email
```

---

## 회원가입

```python
# settings.py
ACCOUNT_AUTHENTICATION_METHOD = "email"
```

> `email` 로 로그인 설정 `(default는 username)`

```python
# project app 안에 있는 urls.py
path("", include('allauth.urls'))
```

> allauth url을 지정

```python
# settings.py
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
```

> 이메일 인증은 console창으로 받게 설정

- allauth url 은 다음과 같이 이동할 수 있다
  - `/login/`로그인, `/logout/`로그아웃, `/signup/`회원가입

#### signup.html

```html
<div class="account-background">
  <main class="account">
    <div class="title">
      <a href="{% url 'index' %}">
        <img
          class="logo"
          src="{% static 'golf/assets/golf-logo.svg' %}"
          alt="Coplate Logo"
        />
      </a>
    </div>

    <form method="post">
      {% csrf_token %}
      <div>
        {{
        form.email|add_class:"cp-input"|attr:"placeholder:이메일"|add_error_class:"error"
        }} {% for error in form.email.errors %}
        <div class="error-message">{{ error }}</div>
        {% endfor %}
      </div>
      {% comment %}
      <div>
        {{
        form.nickname|add_class:"cp-input"|attr:"placeholder:닉네임"|add_error_class:"error"}}
        {% for error in form.nickname.errors %}
        <div class="error-message">{{ error }}</div>
        {% endfor %}
      </div>
      {% endcomment %}
      <div>
        {{
        form.password1|add_class:"cp-input"|attr:"placeholder:비밀번호"|add_error_class:"error"}}
        {% for error in form.password1.errors %}
        <div class="error-message">{{ error }}</div>
        {% endfor %}
      </div>
      <div>
        {{ form.password2|add_class:"cp-input"|attr:"placeholder:비밀번호
        확인"|add_error_class:"error"}} {% for error in form.password2.errors %}
        <div class="error-message">{{ error }}</div>
        {% endfor %}
      </div>
      <button class="cp-button" type="submit">회원가입</button>
    </form>

    <div class="info">
      이미 회원이신가요?<a class="link" href="{% url 'account_login' %}"
        >로그인</a
      >
    </div>
  </main>
</div>
```

#### profile_set_form.html

```html
<div class="account-background">
  <main class="profile-form">
    <div class="logo">
      <img
        class="logo"
        src="{% static 'golf/assets/golf-logo.svg' %}"
        alt="Golf Logo"
      />
    </div>
    <p class="welcome-message">
      환영합니다! <strong>프로필</strong>을 작성해주세요
    </p>
    <form method="post" enctype="multipart/form-data" autocomplete="off">
      {% csrf_token %}
      <div class="profile">
        <div
          class="profile-pic cp-avatar large"
          style="background-image: url('{{ user.profile_pic.url }}')"
        ></div>
        <div class="file">{{ form.profile_pic }}</div>
      </div>
      <div class="nickname">
        {{
        form.nickname|add_class:"cp-input"|add_error_class:"error"|attr:"placeholder:닉네임"
        }} {% for error in form.nickname.errors %}
        <div class="error-message">{{ error }}</div>
        {% endfor %}
      </div>
      <div class="content">
        {{
        form.intro|add_class:"cp-input"|add_error_class:"error"|attr:"placeholder:자신을
        소개해 주세요!" }} {% for error in form.intro.errors %}
        <div class="error-message">{{ error }}</div>
        {% endfor %}
      </div>
      <div class="buttons">
        <button class="cp-button" type="submit">완료</button>
      </div>
    </form>
  </main>
</div>
```

<div align="center">
<img src="https://user-images.githubusercontent.com/117843786/221419655-bdb6c5da-994b-47d7-bf5a-6acd6e79786c.png" width="50%" height="50%"/>
<img src="https://user-images.githubusercontent.com/117843786/221420154-c6697b01-d653-41b2-8eed-e86ac00d412c.png" width="35%" height="35%"/>
</div>

---

## 로그인

#### login.html

```html
<div class="account-background">
  <main class="account">
    <div class="title">
      <a href="{% url 'index' %}">
        <img
          class="logo"
          src="{% static 'golf/assets/golf-logo.svg' %}"
          alt="Golf Logo"
        />
      </a>
    </div>

    <form method="post">
      {% csrf_token %} {% for error in form.non_field_errors %}
      <div class="form-error error-message">{{ error }}</div>
      {% endfor %}

      <div>
        {{
        form.login|add_class:'cp-input'|attr:"placeholder:이메일"|add_error_class:"error"
        }} {% for error in form.login.errors %}
        <div class="form-error error-message">{{ error }}</div>
        {% endfor %}
      </div>
      <div>
        {{
        form.password|add_class:'cp-input'|attr:"placeholder:비밀번호"|add_error_class:"error"
        }} {% for error in form.password.errors %}
        <div class="form-error error-message">{{ error }}</div>
        {% endfor %}
      </div>
      <button class="cp-button" type="submit">로그인</button>
    </form>

    <div class="info">
      <a class="item" href="{% url 'account_reset_password' %}"
        >비밀번호 찾기</a
      >
      <a class="item" href="{% url 'account_signup' %}">회원가입</a>
    </div>
  </main>
</div>
```

<img src="https://user-images.githubusercontent.com/117843786/221420848-a80c9a13-3afc-40e8-a841-9d9c7aa02e4c.png" width="50%" height="50%"/>

---

## 회원탈퇴

#### urls.py

```python
path('delete/<int:user_id>/', views.UserDeleteView.as_view(), name="user-delete")
```

#### view.py

```python
class UserDeleteView(DeleteView):
    model = User
    template_name = "golf/user_delete.html"
    pk_url_kwarg = "user_id"

    def get_success_url(self):
        return reverse("index")
```

#### user_delete.html

```html
<main class="site-body">
  <form class="cp-dialog review-confirm-delete" method="post">
    {% csrf_token %}
    <span class="content">정말 탈퇴 하시겠습니까?</span>
    <button class="cp-button warn" type="submit">탈퇴</button>
    <a class="cp-button secondary" href="{% url 'profile' user.id %}">취소</a>
  </form>
</main>
```

<img src="https://user-images.githubusercontent.com/117843786/221421221-d1d2c2c1-9480-4c68-a156-790819ec87ff.png" width="20%" height="20%"/>
- 유저 프로필 하단 아래 회원탈퇴 버튼이 있다

<img src="https://user-images.githubusercontent.com/117843786/221421198-9dee54f2-0605-429a-b59b-356ceeeb248d.png" width="70%" height="70%"/>
- 정말 탈퇴할 것인지 물어본다

---

## 접근제어(권한)
```python
{% if user.is_authenticated and user == profile_user %}
<div align="right" style="padding-right:200px">
  <p  class="cp-chip intro" >
    <a href="{% url 'user-delete' profile_user.id %}">
      회원탈퇴
    </a>
  </p>
</div>
{% endif %}
```
- 로그인 유저 자신의 프로필에서만 회원탈퇴 버튼이 보인다 

```python
{% if user.is_authenticated %}
	{{ form.content|attr:"placeholder:댓글 내용을 입력해주세요."|add_class:"cp-input" }}
    <button class="cp-button small" type="submit">등록</button>
{% else %}
   <a href="{% url 'account_login' %}?next={% url 'review-detail' review.id %}">
   {{ form.content|attr:"placeholder:댓글을 작성하려면 로그인이 필요합니다."|add_class:"cp-input"|attr:"disabled"}}
</a>
```
- 로그인 유저만 댓글 작성이 가능하다
- 비로그인 유저는 댓글 작성 폼을 클릭하면 로그인 창으로 이동한다

```python
{% if user.is_authenticated %}
	<form action="{% url 'process-like' comment_ctype_id comment.id %}" method="post">{% csrf_token %}
	<button class="like-button" type="submit">
	{% if comment in liked_comments %}
	<img width="21px" src="{% static 'golf/icons/ic-heart-orange.svg' %}" alt="filled like icon">
	{% else %}
	<img width="21px" src="{% static 'golf/icons/ic-heart.svg' %}" alt="like icon">
	{% endif %}
	<span> 좋아요 {{ comment.likes.count }}</span>
	</button>
	</form>
{% else %}
    <a class="like-button" href="{% url 'account_login' %}?next={% url 'review-detail' review.id %}" >
    <img width="21px" src="{% static 'golf/icons/ic-heart.svg' %}" alt="like icon">
    <span> 좋아요 {{ comment.likes.count }}</span>
    </a>
{% endif %}
```
- 로그인 유저만 게시글과 댓글 좋아요 버튼을 누룰 수 있다

```python
{% if user.is_authenticated and user != profile_user%}
      <form class="follow-button" action="{% url 'process-follow' profile_user.id %}" method="post">
        {% csrf_token %}
        {% if is_following %}
          <button class="cp-button small secondary" type="submit">
            언팔로우
          </button>
        {% else %}
          <button class="cp-button small" type="submit">
            팔로우
          </button>
        {% endif %}
```
- 다른 유저를 팔로우 했다면 버튼이 언팔로우로 바뀐다


## 추가하고싶은기능
- 스토어 nav 기능 구현 -> Item, Cart클래스 만들어서 manytomany로 유저마다 담은 카트가 다르게
- 스크린골프 장소 map에서 현재 위치 기준으로 검색 할 수 있게끔

