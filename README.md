## :computer: Bootstrap 이용해서 소품 구매 사이트 구현하기 :department_store:

### :clapper: 서비스 MockUp [템플릿 보기](https://imweb.me/theme)

- Our-Mind 템플릿 찾아서 클릭!

![bootstrap_mockup](https://user-images.githubusercontent.com/84713532/217990846-b18b808a-e326-44ea-bf22-9fbc58f937d5.gif)

## 개요

- HTML 5
- CSS 3
- JavaScript
- BootStrap

#### front-end 기술을 활용하여 소품 마켓 사이트를 구현하는 프로젝트입니다.

- 직접 구현한 Main Page

![image](https://user-images.githubusercontent.com/84713532/218035007-0d6ea8ee-5b49-4905-b423-a8332c888a8a.png)

## [:pencil2: 프로젝트 결과 사이트 입장하기](https://ugeunji.github.io/Front-end-Realization-Web-Site-with-Bootstrap/)

## :pencil: Mini Project (2023/02/09 ~ 2023/02/10) :date:

###  팀명: Paradiso

#### > :family: 팀원

- [양효준](https://github.com/Hyojoon-Yang)
- [이상훈](https://github.com/Dawnnote)
- [정제경](https://github.com/bmr03016)
- [지우근](https://github.com/UGeunJi)


### 시연 영상

[Main Page 시연 영상](#main-page-시연-영상)

[Navigation Bar 바 시연 영상](#navigation-bar-시연-영상)

[Side Bar 시연 영상](#side-bar-시연-영상)

---

## :dart: Trouble Shooting

1. 동시다발적인 작업으로 인해 충돌이 많이 일어났는데, 미숙한 처리로 코드가 계속 바뀌었습니다.
- 최종적으로 한 번 더 정리해서 마무리 지었습니다.

2. CSS file의 class name이 중첩되어 적용되어 사이트가 이상하게 구현이 되었습니다.
- 이름을 하나하나 수정해서 해결했습니다.

3. CSS와 Bootstrap이 함께 연동되어 사용되지 않았습니다.
- 겹치는 부분을 수정하여 해결하였습니다.

4. Navigation bar와 Side bar가 겹쳐보여서 떨어뜨리려고 padding을 설정한다거나, Bootstrap을 이용하여 시도해봤지만 실패하였습니다.

5. file 경로를 제대로 설정해줘도 페이지가 제대로 넘어가지 않았습니다.
- file 위치를 옮겨서 해결했습니다.

👩‍🦰 정제경: 메인페이지, 상세페이지 상단, 이미지 및 로그인 화면 구현
"유저들마다 구현되는 화면이 다르기 때문에 나타나는 문제점도 있었고, 개개인의 코드를 병합하면 또 화면에 문제가 생기니 그걸 수정하느라 애를 많이 먹었었다. 
또한 시각적인 것 뿐만 아니라 기능 구현에 대한 필요성을 많이 느꼈기도 하다."

---

## :stars: 더 구현하고 싶은 기능

- Bootstrap으로만 코딩한 웹 사이트
- 실제 로그인 기술
- 장바구니를 통한 결제 시뮬레이션

👩‍🦰 정제경: 장바구니와 q&a연결 부분

---

## Code 및 시연 영상

## Main Page

[main page code page](https://github.com/HyoJoon-Yang/web_site/tree/main/main)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" 
    rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" 
    crossorigin="anonymous">

    <link rel="stylesheet" href="main.css">
    <script src="https://kit.fontawesome.com/55287f411f.js" crossorigin="anonymous"></script>
    <link rel="stylesheet" type="text/css" href="style.css">
    <link rel="stylesheet" type="text/css" href="navigation_bar.css">
</head>
<body>
    <nav class="navbar bg-dark" data-bs-theme="dark">
        <div class="container-fluid col-10">
            <a class="navbar-brand " style="font-size: 0.95em; color: white; font-weight: bold;" href="#">>> NEW ARRIVALS 20% SALE !</a>
            <button class="navbar-toggler fa-sm" type="button" data-bs-toggle="collapse" data-bs-target="#navbarColor01" aria-controls="navbarColor01" aria-expanded="false" aria-label="Toggle navigation">
              <span class="navbar-toggler-icon"></span>
            </button>
            <ul class="navbar bg-dark">
              <li class="nav-item">
                <a class="nav-link navbar bg-dark" data-bs-toggle="modal"  data-bs-target="#staticBackdrop" href="#">Login</i></a>
              </li>
              <li class="nav-item">
                <a class="nav-link navbar bg-dark" href="join.html">Join</a>
              </li>
              <li class="nav-item">
                <a class="nav-link navbar bg-dark" href="shopping_cart.html">Cart</a>
              </li>
            </ul>
            </div>
          </div>
        </div>
      </nav>

      <div class="container-fluid">
        <div class="row flex-nowrap">
          <div class="col-3 bd-sidebar">
            <div class="d-flex flex-column flex-shrink-0 p-3 bg-light" style="width: 230px;">
              <h2></h2>
              <hr>
              <h3>Our mind Store</h3>
        
              <hr>
              <navi>
                <div class="navi-links">
                  <a href="main.html">ALL PRODUCT</a>
                  <a href="notice.html">NOTICE</a>
                  <a href="faq.html">FAQ</a>
                  <a href="contact.html">CONTACT</a>
                </div>
        
        
            </navi>
        
                  <hr>
                  <h3>Popular Products</h3>
                  <ul class="product-list">
                    <li><img src="images/cup1.jpg" alt="Product 1"></li>
                    <li><img src="images/plate1.jpg" alt="Product 2"></li>
                    <li><img src="images/glass-mug.jpg" alt="Product 3"></li>
                    <li><img src="images/blackcup.jpg" alt="Product 3"></li>
                    <li><img src="images/wood.jpg" alt="Product 3"></li>
                    <li><img src="./images/image1.png" alt="Product 3"></li>
                  </ul>
                  <hr>
                  <form action="https://www.google.com/search">
                    <input type="text" placeholder="Search..." name="q">
                    <button type="submit">Go</button>
                  </form>
            </div>
          </div>
          <main class="col-4" role="main">
          <div class="d-flex flex-row bd-highlight mb-5">
      <section>
          <figure> <img src="images/cup1.jpg" alt="" width="300" height="400">
              <figcaption>
                  <h2>Wave Glass</h2>
                  <p>17000원</p> <button class="btn" onclick=""><i id="heart"
                          class="fa-regular fa-heart my-xl my-cursor"></i></button> <button class="btn"
                      onclick=""><i class="fa-regular fa-comment my-xl my-cursor"></i></button> <button
                      class="btn" onclick="location.href='detailpage.html'"><i class="fa-solid fa-cart-shopping my-xl my-cursor"></i></button>
              </figcaption>
          </figure>
      </section>
      <section>
          <figure> <img src="images/plate1.jpg"  width="300" height="400">
              <figcaption>
                  <h2>Plate</h2>
                  <p>21000원</p> <button class="btn" onclick=""><i id="heart"
                          class="fa-regular fa-heart my-xl my-cursor"></i></button> <button class="btn"
                      onclick=""><i class="fa-regular fa-comment my-xl my-cursor"></i></button> <button
                      class="btn" onclick="location.href='detailpage.html'"><i class="fa-solid fa-cart-shopping my-xl my-cursor"></i></button>
                </figcaption>
          </figure>
      </section>
      <section>
          <figure> <img src="images/glass-mug.jpg" width="300" height="400">
              <figcaption>
                  <h2>Glass Mug</h2>
                  <p>13000원</p> <button class="btn" onclick=""><i id="heart"
                          class="fa-regular fa-heart my-xl my-cursor"></i></button> <button class="btn"
                      onclick=""><i class="fa-regular fa-comment my-xl my-cursor"></i></button> <button
                      class="btn" onclick="location.href='detailpage.html'"><i class="fa-solid fa-cart-shopping my-xl my-cursor"></i></button>
              </figcaption>
          </figure>
      </section>
    </div>
    <div class="d-flex flex-row bd-highlight mb-5">
      <section>
          <figure> <img src="images/blackcup.jpg" alt="" width="300" height="400">
              <figcaption>
                  <h2>Black Mug</h2>
                  <p>15000원</p> <button class="btn" onclick=""><i id="heart"
                          class="fa-regular fa-heart my-xl my-cursor"></i></button> <button class="btn"
                      onclick=""><i class="fa-regular fa-comment my-xl my-cursor"></i></button> <button
                      class="btn" onclick="location.href='detailpage.html'"><i class="fa-solid fa-cart-shopping my-xl my-cursor"></i></button>
              </figcaption>
          </figure>
      </section>
      <section>
          <figure> <img src="images/wood.jpg" alt="" width="300" height="400">
              <figcaption>
                  <h2>Wood Cutting Board</h2>
                  <p>38000원</p> <button class="btn" onclick=""><i id="heart"
                          class="fa-regular fa-heart my-xl my-cursor"></i></button> <button class="btn"
                      onclick=""></button><i class="fa-regular fa-comment my-xl my-cursor"></i></button> <button
                      class="btn" onclick="location.href='detailpage.html'"></button><i
                      class="fa-solid fa-cart-shopping my-xl my-cursor"></i></button>
              </figcaption>
          </figure>
      </section>
    </div>
          </main>
        </div>
      </div>
      <!--회사 정보-->
      <footer id="footer">
        <div class="timeinfo">
            <p>
            <h4>TIME INFO</h4>
            </p>
            <p>MON-FRI AM 09:00 - PM 06:00</p>
            <p>LUNCH PM 01:00-PM 02:00</p>
            <p>SAT.SUN.HOLIDAY OFF</p>
        </div>
        <div class="companyinfo">
            <p>
            <h4>COMPANY INFO</h4>
            </p>
            <p>Company: Paradiso l Company Registration No: 000-00-0000</p>
            <p>Mail-Order License: 0000-Seoul-0000 l Address: Seoul, Korea</p>
            <p>Tel: 00 000 0000 l Fax: 00 000 0000</p>
        </div>
        </footer>




        <!-- Modal -->
  <div class="modal fade" id="staticBackdrop" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="staticBackdropLabel">Login</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
            <body class="text-center">
    
                <main class="form-signin">
                  <form>
                    <h1 class="h3 mb-3 fw-normal">Please sign in</h1>
                
                    <div class="form-floating">
                      <input type="email" class="form-control" id="floatingInput" placeholder="name@example.com">
                      <label for="floatingInput">Email address</label>
                    </div>
                    <div class="form-floating">
                      <input type="password" class="form-control" id="floatingPassword" placeholder="Password">
                      <label for="floatingPassword">Password</label>
                    </div>
                
                    <div class="checkbox mb-3">
                      <label>
                        <input type="checkbox" value="remember-me"> Remember me
                      </label>
                    </div>
                    <button class="w-100 btn btn-lg btn-primary" type="submit">Sign in</button>
                    <p class="mt-5 mb-3 text-muted">&copy; 2022–2023</p>
                  </form>
                </main>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        </div>
      </div>
    </div>
  </div>




    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" 
  integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" 
  crossorigin="anonymous"></script>
  <script src="https://kit.fontawesome.com/70388619d3.js" crossorigin="anonymous"></script>
</body>
</html>
```

### Main Page 시연 영상

![main_page](https://user-images.githubusercontent.com/84713532/218036004-f677d35a-29c7-49f4-8a7b-0268146328e8.gif)

## Navigation Bar

[navigation bar code page](https://github.com/HyoJoon-Yang/web_site/tree/main/navigation%20bar)

```html
<!DOCTYPE html>
<html>

<head>
  <meta charset="UTF-8">
  <title>Navigation Bar Example</title>
  <link rel="stylesheet" type="text/css" href="navigation_bar.css">

</head>

<body>
  <header id="header">
    <nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">
      <div class="navbar">
        <ul>
          <li><a class="current" href="/css/intro">>> NEW ARRIVALS 20% SALE !</a></li>
          <ul style="float:right; list-style-type:none;">

            <li><a href="/bbs/login.php">Login</a></li>
            <li><a href="/bbs/register_form.php">Join</a></li>
            <li><a href="/bbs/cart.php">Cart</a></li>
          </ul>
        </ul>
      </div>
    </nav>
  </header>
</body>

</html>
```

### Navigation Bar 시연 영상

![navigation_bar](https://user-images.githubusercontent.com/84713532/218036392-d882375f-1ebb-483b-8057-df71b9e737bb.gif)

## Side bar

[side bar code page](https://github.com/HyoJoon-Yang/web_site/tree/main/sidebar)

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>Side bar</title>
    <link rel="stylesheet" type="text/css" href="style.css">
  </head>
  <body>
    <div class="sidebar">
      <h2></h2>
      <h3>Our mind Store</h3>

      <navi>
        <div class="navi-links">
          <a href="#">ALL PRODUCT</a>
          <a href="notice.html">NOTICE</a>
          <a href="faq.html">FAQ</a>
          <a href="contact.html">CONTACT</a>
        </div>


  
    </navi>

          <hr>
          <h3>Popular Products</h3>
          <ul class="product-list">
            <li><img src="./images/image1.png" alt="Product 1"></li>
            <li><img src="./images/image1.png" alt="Product 2"></li>
            <li><img src="./images/image1.png" alt="Product 3"></li>
            <li><img src="./images/image1.png" alt="Product 3"></li>
            <li><img src="./images/image1.png" alt="Product 3"></li>
            <li><img src="./images/image1.png" alt="Product 3"></li>
          </ul>
          <hr>
          <form action="https://www.google.com/search">
            <input type="text" placeholder="Search..." name="q">
            <button type="submit">Go</button>
          </form>
    </div>
    
    <div class="top-links">
      <a href="#">ALL PRODUCT</a>
      <a href="notice.html">NOTICE</a>
      <a href="faq.html">FAQ</a>
      <a href="contact.html">CONTACT</a>
    </div>
    
    <script src="app.js"></script>
  </body>
</html>
```

### Side bar 시연 영상

![side_bar](https://user-images.githubusercontent.com/84713532/218036630-8baab5f7-a9c0-4905-9b5a-05ac885201a9.gif)

## Detail Page

[detail page code page](https://github.com/HyoJoon-Yang/web_site/tree/main/detail)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
        integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <title>Product Page</title>
    <link rel="stylesheet" href="default.css">
</head>
<body>
    <div class="order_container">
    <div class="detail">
        <img src="images/cup1.jpg" alt=""></a>
    </div>
    <div class="product_view">
        <h2> Wave Glass</h2>
        <h6> 17,000원 </h6>
        <table>
            <colgroup>
            <col style="width:px;"> <!--한쪽은 짧고 한쪽은 길게, 유동적으로 움직일 수 있게-->
            <col>
            </colgroup>
        <tbody>
        <tr>
            <th>구매혜택</th>
            <td>&nbsp;1,700 Point 적립예정</td>
        </tr>
        <tr>
            <th>배송방법</th>
            <td>&nbsp;택배</td>
        </tr>
        <tr>
            <th>배송비</th>
            <td>&nbsp;2,500원(50,000원 이상 무료배송)</td>
        </tr>
        <tr>
            <th>수량</th>
            <td>&nbsp;
                <input type="number" name="number" id="number" min="0", placeholder="0">
                <a href="#a"></a>
                <a href="#a"></a>
            </td>
        </tr>
        <tr>
            <th>결제금액</th>
            <td>&nbsp;<span id="totalPrice"></span></td>
            </tr>
        </tbody>    
    </table>
    <br>
    <div>
        <button class= "purchase" onclick=""><a href="#a">구매하기</a></button>&nbsp;
        <button class= "cart" onclick=""><a href="#shoppingcart.html">장바구니</a></button>
    </div>
    
    <br>
    <br>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container">
            <a class="navbar-brand" href="#">Product Page</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav"
                aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <a class="nav-link" href="#product-info">상세정보</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#product-reviews">구매평 (0)</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#product-q-a">Q&A (0)</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <div class="container my-5">
        <section id="product-info">
            <h3 class="text-center">상세정보</h3>
            <p style="font-size: 15px;">상품명: ---<br>재질: --- <br>원산지: ---<br></p>
        </section>

        <hr>

        <section id="product-reviews">
            <h2 class="text-center">구매평 (0)</h2>
            <div class="row">
                <div class="col-md-12">
                    <ul class="list-group">
                        <li class="list-group-item">
                            <h5>Downnote</h5>
                            <p style="font-size: 15px;">바닥에 떨어뜨려고 깨지지 않고 아주 튼튼하네요! <br> 잘 쓰고 있습니다! ㅎㅎ</p>
                        </li>
                        <li class="list-group-item">
                            <h5>bmr03016</h5>
                            <p style="font-size: 15px;">2개월 째 배송되고 있지 않지만 너무 기대됩니다 ㅎㅎ</p>
                        </li>
                    </ul>
                </div>
            </div>
        </section>

        <hr>

        <section id="product-q-a">
            <h3 class="text-center">Q&A (0)</h3>
            <div class="row">
                <div class="col-md-12">
                    <ul class="list-group">
                        <li class="list-group-item">
                            <h5>UGeunJi</h5>
                            <p style="font-size: 15px;">200개 정도 추가 구매를 하고 싶습니다. 가능한가요?</p>
                            <p style="font-size: 15px;">네, UGeunJi님 <br>가능하십니다.</p>
                            <p>Answer content</p>
                        </li>
                        <li class="list-group-item">
                            <h5>HyoJoon-Yang</h5>
                            <p style="font-size: 15px;">주문한 상품이 1달째 오지 않고 있습니다. 배송 중인가요?</p>
                            <p style="font-size: 15px;">네, HyoJoon-Yang님 <br> 맞습니다. 조금만 더 기다려주세요.</p>
                            <p>Answer content</p>
                        </li>
                    </ul>
                </div>
            </div>
        </section>
    </div>

    </div>
    </div>


    <script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
    ​<script>
    let input = document.querySelector('#number');
    let totalPrice = document.getElementById('totalPrice');
    input.onchange = handleChange;
    function handleChange(e) {
        totalPrice.textContent = e.target.value * 17000
    }
    </script>
</body>
</html>
```

### Detail Page 시연 영상

![detail_page](https://user-images.githubusercontent.com/84713532/218038324-3e895b5f-c4a6-40a9-811d-4d7855a75b9f.gif)
