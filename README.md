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
> 로그인 유저 자신의 프로필에서만 회원탈퇴 버튼이 보인다 

```python
{% if user.is_authenticated %}
	{{ form.content|attr:"placeholder:댓글 내용을 입력해주세요."|add_class:"cp-input" }}
    <button class="cp-button small" type="submit">등록</button>
{% else %}
   <a href="{% url 'account_login' %}?next={% url 'review-detail' review.id %}">
   {{ form.content|attr:"placeholder:댓글을 작성하려면 로그인이 필요합니다."|add_class:"cp-input"|attr:"disabled"}}
</a>
```
> 로그인 유저만 댓글 작성이 가능하다
> 비로그인 유저는 댓글 작성 폼을 클릭하면 로그인 창으로 이동한다

![비로그인](https://user-images.githubusercontent.com/117843786/221466000-2c46e169-fb56-463a-a6ed-d84ec5a11e47.gif)

<br/>
<br/>


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
> 로그인 유저만 게시글과 댓글 좋아요 버튼을 누룰 수 있다

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
> 다른 유저를 팔로우 했다면 버튼이 언팔로우로 바뀐다

---

## CRUD

#### 게시글 작성
- review_form.html
```html
{% block content %}
<main class="site-body">
  <form class="review-form max-content-width" method="post" autocomplete="off" enctype="multipart/form-data">
    {% csrf_token %}
    <div class="title">
      {{ form.title|add_class:"cp-input"|attr:"placeholder:제목"}}
      {% for error in form.title.errors %}
        <div class="error-message">{{ error }}</div>
      {% endfor %}
    </div>
    <div class="golf-name">
      {{ form.golf_name|add_class:"cp-input"|attr:"placeholder:골프장 이름"}}
      {% for error in form.golf_name.errors %}
        <div class="error-message">{{ error }}</div>
      {% endfor %}
    </div>
    <div class="golf-link">
      {{ form.golf_link|add_class:"cp-input"|attr:"placeholder:골프장 주소 링크"}}
      {% for error in form.golf_link.errors %}
        <div class="error-message">{{ error }}</div>
      {% endfor %}
    </div>
    <div class="rating">
      <div class="cp-stars">
        {% for radio in form.rating %}
          {{radio}}
        {% endfor%}
      </div>
      {% for error in form.radio.errors %}
      <div class="error-message">{{ error }}</div>
      {% endfor %}
    </div>
    <div class="content">
      {{ form.content|add_class:"cp-input"|attr:"placeholder:리뷰를 작성해 주세요."}}
      {% for error in form.title.errors %}
        <div class="error-message">{{ error }}</div>
      {% endfor %}
    </div>
    <div class="file">
      <div class="file-content">
        {% if review.image1 %}
          <img src="{{ review.image1.url }}"
        {% endif %}
        <div>
          {{ form.image1 }}
          {% for error in form.image1.errors %}
            <div class="error-message">{{ error }}</div>
          {% endfor %}
        </div>
      </div>
    </div>
    <div class="file">
      <div class="file-content">
        {% if review.image2 %}
          <img src="{{ review.image2.url }}"
        {% endif %}
        <div>
          {{form.image2}}
          {% for error in form.image2.errors %}
            <div class="error-message">{{ error }}</div>
          {% endfor %}
        </div>
      </div>
    </div>
    <div class="file">
      <div class="file-content">
        {% if review.image3 %}
          <img src="{{ review.image3.url }}"
        {% endif %}
        <div>
          {{form.image3}}
          {% for error in form.image3.errors %}
            <div class="error-message">{{ error }}</div>
          {% endfor %}
        </div>
      </div>
    </div>
    <div class="buttons">
      <a
      class="cp-button secondary cancel"
      href="{% if review %}{% url 'review-detail' review.id %}{% else %}{% url 'index' %}{% endif %}">
      취소
    </a>
      <button class="cp-button submit" type="submit">완료</button>
    </div>
  </form>
</main>
{% endblock content %}
```

![리뷰 달기 ](https://user-images.githubusercontent.com/117843786/221465881-bc5425c7-d890-4fc6-b995-d902ec559df4.gif)

<br/>
<br/>

#### 게시글 수정
```html
{% block content %}
<main class="profile-form">
  <form method="post" enctype="multipart/form-data" autocomplete="off">
    {% csrf_token %}
    <div class="profile">
      <div class="profile-pic cp-avatar large" style="background-image: url('{{ user.profile_pic.url }}')"></div>
      <div class="file">
        {{ form.profile_pic }}
      </div>
    </div>
    <div class="nickname">
      {{ form.nickname|add_class:"cp-input"|add_error_class:"error"|attr:"placeholder:닉네임" }}
      {% for error in form.nickname.errors %}
        <div class="error-message">{{ error }}</div>
      {% endfor %}
    </div>
    <div class="content">
      {{ form.intro|add_class:"cp-input"|add_error_class:"error"|attr:"placeholder:자신을 소개해 주세요!" }}
      {% for error in form.intro.errors %}
        <div class="error-message">{{ error }}</div>
      {% endfor %}
    </div>
    <div class="buttons">
      <a class="cp-button secondary cancel" href="{% url 'profile' user.id %}">취소</a>
      <button class="cp-button" type="submit">완료</button>
    </div>
  </form>
</main>
{% endblock content %}
```

![리뷰수정](https://user-images.githubusercontent.com/117843786/221471804-2a321d1c-ad0e-4b20-a79f-8e4c2777dd49.gif)
<br/>
<br/>

#### 게시글 삭제
```html
{% block content %}
<main class="site-body">
  <form class="cp-dialog review-confirm-delete" method="post">
    {% csrf_token %}
    <span class="content">정말 리뷰를 삭제하시겠습니까?</span>
    <button class="cp-button warn" type="submit">삭제</button>
    <a class="cp-button secondary" href="{% url 'review-detail' review.id %}">취소</a>
  </form>
</main>
{% endblock content %}
```
<br/>
<br/>

#### 댓글 작성
```html
{% block content %}
<main class="site-body">
  <form class="comment-update-form" method="post">
    {% csrf_token %}
    {{ form.content|attr:"placeholder:댓글 내용을 입력해주세요."|add_class:"cp-input" }}
    <div class="buttons">
      <button class="cp-button small" type="submit">완료</button>
      <a class="cp-button small secondary" href="{% url 'review-detail' usercomment.review.id %}">취소</a>
    </div>
  </form>
</main>
{% endblock content %}
```
![댓글작성](https://user-images.githubusercontent.com/117843786/221471850-0a8fde65-d9a1-45d0-a93c-4403834f50ce.gif)

<br/>
<br/>

#### 댓글 수정
```html
{% block content %}
<main class="site-body">
  <form class="comment-update-form" method="post">
    {% csrf_token %}
    {{ form.content|attr:"placeholder:댓글 내용을 입력해주세요."|add_class:"cp-input" }}
    <div class="buttons">
      <button class="cp-button small" type="submit">완료</button>
      <a class="cp-button small secondary" href="{% url 'review-detail' usercomment.review.id %}">취소</a>
    </div>
  </form>
</main>
{% endblock content %}
```
![댓글수정](https://user-images.githubusercontent.com/117843786/221471870-8dc6758b-5d12-4878-8409-88e43fb34ed7.gif)
<br/>
<br/>

#### 댓글 삭제
```html
{% block content %}
<main class="site-body">
  <form class="cp-dialog review-confirm-delete" method="post">
    {% csrf_token %}
    <span class="content">정말 댓글을 삭제하시겠습니까?</span>
    <button class="cp-button warn" type="submit">삭제</button>
    <a class="cp-button secondary" href="{% url 'review-detail' usercomment.review.id %}">취소</a>
  </form>
</main>
{% endblock content %}
```
##### 댓글, 게시물 삭제

![댓글게시물삭제](https://user-images.githubusercontent.com/117843786/221465614-e3e34781-36a8-4867-9559-e79faec2e905.gif)
<br/>
<br/>

---

## 검색 기능

- search_results.html
```html
{% block content %}
<main class="site-body">
  <div class="content-list max-content-width">
    <form class="search-form" action="{% url 'search' %}" method="get">
      <input class="search-input" name="query" value="{{ query }}" type="text" placeholder="식당, 음식 등을 검색해보세요" required>
      <button class="cp-button search-button" type="submit">검색</button>
    </form>
    <div class="header">
      <h2>"{{ query }}"에 대한 겸색 결과 ({{ paginator.count }})</h2>
    </div>
    {% include 'components/review_list.html' with reviews=search_results empty_message="검색 결과가 없어요 :" %}
    {% if is_paginated %}
      {% include 'components/pagination.html' with page_obj=page_obj %}
    {% endif %}
  </div>
</main>
{% endblock content %}
```

- urls.py
```python
path('search/', views.SearchView.as_view(), name='search')
```

- views.py
```python
from django.db.models import Q

class SearchView(ListView):
    model = Review
    context_object_name = 'search_results'
    template_name = 'golf/search_results.html'
    paginate_by = 8
  
    def get_queryset(self):
        query = self.request.GET.get('query', '')
        return Review.objects.filter(
            Q(title__icontains=query)
            | Q(golf_name__icontains=query)
            | Q(content__icontains=query)
        )
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('query', '')
        return context
```

![검색기능](https://user-images.githubusercontent.com/117843786/221471885-77c9fb4e-7a0b-445e-9260-975703a9094f.gif)


---
## 조건 제어
- validators.py
```python
import string
from django.core.exceptions import ValidationError


def contains_special_character(value):
    for char in value:
        if char in string.punctuation:
            return True
    return False


def contains_uppercase_letter(value):
    for char in value:
        if char.isupper():
            return True
    return False


def contains_lowercase_letter(value):
    for char in value:
        if char.islower():
            return True
    return False


def contains_number(value):
    for char in value:
        if char.isdigit():
            return True
    return False


class CustomPasswordValidator:
    def validate(self, password, user=None):
        if (
                len(password) < 8 or
                not contains_uppercase_letter(password) or
                not contains_lowercase_letter(password) or
                not contains_number(password) or
                not contains_special_character(password)
        ):
            raise ValidationError("8자 이상의 영문 대/소문자, 숫자, 특수문자 조합이어야 합니다.")
            
    def get_help_text(self):
        return "8자 이상의 영문 대/소문자, 숫자, 특수문자 조합을 입력해 주세요."


def validate_no_special_characters(value):
    if contains_special_character(value):
        raise ValidationError("특수문자를 포함할 수 없습니다.")


def validate_golf_link(value):
    pass
    # if "place.naver.com" not in value and "place.map.kakao.com" not in value:
    #     raise ValidationError("place.naver.com 또는 place.map.kakao.com이 들어가야 합니다.")
```
---

## 좋아요
- urls.py
```python
    path(
        'like/<int:content_type_id>/<int:object_id>/',
        views.ProcessLikeView.as_view(),
        name='process-like'
    )
```

- views.py
```python
class ProcessLikeView(LoginAndVerificationRequiredMixin, View):
    http_method_names = ['post']
    def post(self, request, *args, **kwargs):
        like, created = Like.objects.get_or_create(
            user= self.request.user,
            content_type_id = self.kwargs.get('content_type_id'),
            object_id=self.kwargs.get('object_id'),
        )
        if not created:
            like.delete()
        return redirect(self.request.META['HTTP_REFERER'])
```

![댓글좋아요](https://user-images.githubusercontent.com/117843786/221473598-e0b9f27e-2417-4183-a281-cd98acfc648a.gif)

<br/>
<br/>

---


# 팔로잉, 팔로워
- urls.py
```python
path(
        'users/<int:user_id>/follow/',
        views.ProcessFollowView.as_view(),
        name='process-follow'
    ),
    
path('users/<int:user_id>/following/', views.FollowingListView.as_view(), name='following-list'),

path('users/<int:user_id>/followers/', views.FollowerListView.as_view(), name='follower-list'),
```

- views.py (팔로잉 리스트)
```python
class FollowingListView(ListView):
    model = User
    template_name = 'golf/following_list.html'
    context_object_name = 'following'
    paginate_by = 10
  
    def get_queryset(self):
        profile_user = get_object_or_404(User, pk=self.kwargs.get('user_id'))
        return profile_user.following.all()
  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile_user_id'] = self.kwargs.get('user_id')
        return context
```

- views.py (팔로워 리스트)
```python
class FollowerListView(ListView):
    model = User
    template_name = 'golf/follower_list.html'
    context_object_name = 'followers'
    paginate_by = 10
  
    def get_queryset(self):
        profile_user = get_object_or_404(User, pk=self.kwargs.get('user_id'))
        return profile_user.followers.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile_user_id'] = self.kwargs.get('user_id')
        return context
```

![팔로워](https://user-images.githubusercontent.com/117843786/221473737-bb772fe9-4021-42ee-bb15-62a3b68a8d92.gif)
