# CSS

CSS는 웹 페이지의 스타일을 별도의 파일로 저장할 수 있게 해주므로 사이트의 전체 스타일을 손쉽게 제어할 수 있습니다.

또한, 웹 사이트의 스타일을 일관성 있게 유지할 수 있게 해주며, 그에 따른 유지 보수 또한 쉬워집니다.

이러한 외부 스타일 시트는 보통 확장자를 .css 파일로 저장합니다.



HTML만으로 웹 페이지를 제작할 경우 HTML 요소의 세부 스타일을 일일이 따로 지정해 주어야만 합니다.

이 작업은 매우 많은 시간이 걸리며, 완성한 후에도 스타일의 변경 및 유지 보수가 매우 힘들어집니다.

이러한 문제점을 해소하기 위해 W3C(World Wide Web Consortium)에서 만든 스타일 시트 언어가 바로 CSS입니다.

 

CSS는 웹 페이지의 스타일을 별도의 파일로 저장할 수 있게 해주므로 사이트의 전체 스타일을 손쉽게 제어할 수 있습니다.

또한, 웹 사이트의 스타일을 일관성 있게 유지할 수 있게 해주며, 그에 따른 유지 보수 또한 쉬워집니다.

이러한 외부 스타일 시트는 보통 확장자를 .css 파일로 저장합니다.



## CSS 문법

CSS의 문법은 선택자(selector)와 선언부(declaratives)로 구성됩니다.

선택자는 CSS를 적용하고자 하는 HTML 요소(element)를 가리킵니다.

선언부는 하나 이상의 선언들을 세미콜론(;)으로 구분하여 포함할 수 있으며, 중괄호({ })를 사용하여 전체를 둘러쌉니다.

각 선언은 CSS 속성명(property)과 속성값(value)을 가지며, 그 둘은 콜론(:)으로 연결됩니다.

이러한 CSS 선언(declaration)은 언제나 마지막에 세미콜론(;)으로 끝마칩니다.

![image-20220123183454579](CSS_basic.assets/image-20220123183454579.png)



- CSS 선택자
  - HTML 요소 선택자
  - 아이디(id) 선택자
  - 클래스(class) 선택자
  - 그룹(group) 선택자



HTML 요소 선택자

```html
<style>

    h2 { color: teal; text-decoration: underline; }

</style>

...

<h2>이 부분에 스타일을 적용합니다.</h2>

```



아이디(id) 선택자 -> #을 사용해 아이디를 지정

```html
<style>

    #heading { color: teal; text-decoration: line-through; }

</style>

...

<h2 id="heading">이 부분에 스타일을 적용합니다.</h2>
```



클래스 선택자 -> 특정 집단의 여러 요소를 한번에 선택할 때 사용

```html
<style>

    .headings { color: lime; text-decoration: overline; }

</style>

...

<h2 class="headings">이 부분에 스타일을 적용합니다.</h2>

<p>class 선택자를 이용하여 스타일을 적용할 HTML 요소들을 한 번에 선택할 수 있습니다.</p>

<h3 class="headings">이 부분에도 같은 스타일을 적용합니다.</h3>
```



그룹 선택자 -> 언급한 여러 선택자를 사용하고자 할 때 사용

```html
<style>

    h1 { color: navy; }

    h1, h2 { text-align: center; }

    h1, h2, p { background-color: lightgray; }

</style>
```



다른 예시

```html
  <style>
        
        p{
            background-color: coral;
        }
    </style>
    <link rel="stylesheet" href="resources_01/css/css01.css" type="text/css">
</head>
<body>

    <h1>css 기본 문법</h1>

    <b style="color: red;">1. 인라인 스타일</b>

    <p>
        <span>2. 내부 스타일 시트 : html 내부에서 간단하게 작성</span>
        <br>
        <b>3.외부 스타일시트 : *.css파일</b>
    </p>
    
</body>
</html>
```



선택자 예시(타입, id, class, 전체, 자식,인접,하위,속성,가상클래스)

```html

    <link rel="stylesheet"
         href="resources_01/css/css02.css"
         type="text/css">
</head>
<body>

    <h1>선택자</h1>
    <article>
        <h3>타입 선택자</h3>
        <pre>태그 이름을 지정하여 선언</pre>
    </article>

    <article>
        <h3>id 선택자</h3>
        <ul>
            <li id="s-id01">요소에 id를 지정하고</li>
            <li id="s-id02">지정된 id값을 사용하여 선택</li>
            <li id="s-id03">#으로 구분</li>
        </ul>
    </article>

    <article>
        <h3>class 선택자</h3>
        <ol>
            <li class="s-cls01">요소에 class를 지정하고</li>
            <li class="s-cls01">지정된 class 값을 사용하여 선택</li>
            <li class="s-cls02">.(dot)으로 구분</li>
        </ol>
    </article>

    <article>
        <h3>전체 선택자</h3>
        <b>*</b>
    </article>

    <article id="atc">
        <h3>자식 선택자</h3>
        <p>자식!</p>
        <div>
            <p>자식?</p>
        </div>
    </article>

    <article>
        <h3>인접 선택자</h3>
        <b>지정한 요소</b>
        <span>다음에 나오는 요소를 선택</span>
        <pre>인접?</pre>
    </article>

    <article id="atc02">
        <h3>하위 선택자</h3>
        <div>
            <p>
                <span>특정 요소 하위의</span>
            </p>
            <span>요소를 지정할 때 선택</span>
        </div>
        <span>하위?</span>
    </article>

    <article>
        <h3>속성 선택자</h3>
        <p title="a">속성이 정의된</p>
        <p title="b">태그만 선택</p>
        <p>속성 없음</p>
    </article>

    <article>
        <h3>가상 클래스 선택자</h3>
        <ul>
            <li>특정 이벤트가 발생한 태그 선택</li>
            <li><a href="https://www.naver.com">네이버</a></li>
            <li><a href="https://www.ubuntu.com">우분투</a></li>
            <li><input type="checkbox">체크하면 커짐!</li>
        </ul>
    </article>

    
</body>
</html>
```



"resources_01/css/css02.css"

```css
/*주석다는법*/

/*타입*/
pre{
    text-align: center;
}


/*id*/
#s-id01{
    color:hotpink;
}

#s-id02{
    color:darkred
}

/*class*/
.s-cls01{
    background-color: black;
    color:white;
}

/*전체*/
*{
    text-align: center;
}

/* 자식 */
/*article의 자식인 p를 찾기*/
#atc > p {
    color:yellowgreen;
}

/*인접*/
/*span 태그 뒤에 나오는 pre태그*/
span + pre {
    background-color: cornflowerblue;

}


/*하위*/
#atc02 span{
    color:chocolate;
}


/*속성*/
p[title]{
    background-color: gray;
}

/*가상 클래스 선택자*/
/*접속하지 않은 곳 색깔 바꾸기*/
a:link{
    color:green;
    font-size: 20pt;
}
/*가본곳도 바꾸기*/
a:visited{
    color:gold;
}

/*마우스 올리기*/
a:hover{
    background-color: black;
    color:white
}

/*마우스 누르고 있을때*/
a:active{
    background-color: yellow;
    color:tomato;
}

/*체크하면 커짐*/
input:checked{
    width:100px;
    height:100px;
}
```



## CSS 기본 요소

- font-family 사용 및 외부 src에 등록하여 사용

  ```html
   <style type="text/css">
          div >h1{
              font-weight: bold;
              font-style: italic;
              font-variant: small-caps;
              
  
              font-size: 25px;
              line-height: 500%;
              
              font-family: "궁서";
          }
  
          /* 폰트 등록*/
          @font-face{
              font-family: "Goyang";
              src:url("resources_01/font/Goyang.ttf")
          }
  
          div+h1{
              font-family: "Goyang";
  
          }
  
      </style>
  ```



- 박스 모델

  ![image-20220123191010099](CSS_basic.assets/image-20220123191010099.png)

  ​	1. 내용(content) : 텍스트나 이미지가 들어있는 박스의 실질적인 내용 부분입니다.

  2. 패딩(padding) : 내용과 테두리 사이의 간격입니다. 패딩은 눈에 보이지 않습니다.

  3. 테두리(border) : 내용와 패딩 주변을 감싸는 테두리입니다.

  4. 마진(margin) : 테두리와 이웃하는 요소 사이의 간격입니다. 마진은 눈에 보이지 않습니다.

  ```html
  <style type="text/css">
          dl , dt , dd , p {
              margin : 0px;
              padding : 0px;
          }
          /*00(red) 00(green) 00(blue) -> 16진수로 찾기*/
          .box{
              width: 600px;
              border : 3px #123456 double;
  
          }
          dt{
              background : #abcdef;
              text-align: center;
              font-size: 20px;
              letter-spacing: 15px;
              padding: 15px;
              border-bottom: #123456 5px double;
          }
          dd{
              padding : 10px;
          }
          .line{
              border-bottom: #123456 1px dotted;
          }
  
      </style>
  </head>
  <body>
      <dl class="box">
          <dt>드래곤 라자 명언</dt>
          <dd class="line">
              <h2>샌슨 네드발</h2>
              <p>저와 말이 함께 후치를 타면 됩니다</p>
          </dd>
          <dd>
              <h2>핸드레이크</h2>
              <p>나는 단수가 아니다.</p>
          </dd>
      </dl>
  ```

- float 

  - float 속성은 해당 HTML 요소가 주변의 다른 요소들과 자연스럽게 어울리도록 만들어 줍니다.

    이 속성은 본래 위와 같은 목적으로 만들어졌지만, 현재는 웹 페이지의 레이아웃(layout)을 작성할 때 자주 사용됩니다.

  ```html
  <style>
          body{
              width: 300px;
          }
          img{
              width: 100px;
              height: 200px;
          }
          h1{
              float:left;
              background: orange;
          }
          p{
              text-align: justify;
          }
          p span{
              border:3px dotted red;
              float: right;
          }
      </style>
  </head>
  <body>
  
      <h1>드래곤라자</h1>
      <p>"우리는 별이오."
          "별?"
          "무수히 많고 그래서 어쩌면 보잘것없어 보일 수도 있지. 바라보지 않는 이상 우리는 서로를 잊을 수도 있소. 영원의 숲에서처럼 우리들은 서로를, 자신을 돌보지 않는 한 언제라도 그 빛을 잊어버리고 존재를 상실할 수도 있는 별들이지."
          숲은 거대한 암흑으로 변했고 그 위의 밤하늘은 온통 빛무리들 뿐이었다. 칼의 말은 이어졌다.
          "그러나 우리는 서로를 바라볼 줄 아오. 밤하늘은 어둡고, 주위는 차가운 암흑 뿐이지만, 별은 바라보는 자에겐 반드시 빛을 주지요. 우리는 어쩌면 서로를 바라보는 눈동자 속에 존재하는 별빛 같은 존재들이지. 하지만 우리의 빛은 약하지 않소. 서로를 바라볼 때 우리는 우리의 모든 빛을 뿜어내지."
          "나 같은 싸구려 도둑도요?"
          네리아의 목소리는 슬프지 않았다. 그리고 칼의 대답도 평온했다.
          "이제는 아시겠지? 네리아 양. 당신들 주위에 우리가 있고, 우리는 당신을 바라본다오. 그리고 당신은 우리들에게 당신의 빛을 뿜어내고 있소. 우리는 서로에게 잊혀질 수 없는 존재들이오. 최소한 우리가 서로를 바라보는 이상은."
          어둠 속에서 네리아의 눈이 별처럼 아름답게 반짝였다.
          <span>
              <img src="https://w.namu.la/s/c182412ae18194dc4945588a576d1991b12e6ffd025b4742f7d4482b0e8ccdcbce3f96e251ab3a45b56c00816bf3dfd07e3558b6f859bbdc08d80136bba43018f6305ff1defb7e0669bdda51e60ca9df2daadf0a36a454ffeea7cdfdd177723de570461eb4fc1577949cb399863be5e4">
          </span>
          나는 혹시 반짝인 것은 그녀의 눈물이 아닐까 따위의 생각은 관두기로 했다. 그래서 고개를 돌려 밤하늘을 바라보았다.
          내가 바라보자, 별들은 나에게 빛을 주었다.
          - 본문 중-</p>
      
  </body>
  </html>
  ```



- clear : float의 성질을 없애줌

  ```html
  <style type="text/css">
          *{
              margin : 0px;
              padding : 0px;
          }
          #wrapper{
              width: 600px;
              border : 1px dotted red;
          }
          #box01{
              float:right;
              width: 200px;
              padding: 15px;
              background: #ccc;
          }
          #box02{
              float:left;
              width:200px;
              padding:15px;
              background-color: cadetblue;
          }
          #box03{
              /* -> clear을 함으로써 right와 left 사이에 끼지 않고 밑에 배치됨(float 성질 없앰) */
              clear: right; 
              background-color: gray;
              padding: 10px;
  
          }
      </style>
  </head>
  <body>
  
      <!--lorem ipsum 인터넷에서 찾기-->
      <h1>lorem Ipsum</h1>
      <div id="wrapper">
          <div id="box01">
              Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
          </div>
          <div id="box02">
              Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.
              The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from "de Finibus Bonorum et Malorum" by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham.
          </div>
          <div id="box03">
              There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.
          </div>
      </div>
      
  </body>
  </html>
  ```

- overflow : 콘텐츠에 흘러 넘치는 부분을 가려줌

  - overflow : hidden
  - overflow : scroll

  ```html
  <style>
          #body{
              width: 300px;
              height: 100px;
              border: 1px solid red;
              overflow: hidden;
              /* 콘텐츠에 흘러넘치는 부분을 숨겨줌 */
              /* overflow:scroll */
              
  
          }
      </style>
  </head>
  <body>
  
      <div id="body">
          <blockquote>드래곤라자</blockquote>
          <p>"우리는 별이오."
              "별?"
              "무수히 많고 그래서 어쩌면 보잘것없어 보일 수도 있지. 바라보지 않는 이상 우리는 서로를 잊을 수도 있소. 영원의 숲에서처럼 우리들은 서로를, 자신을 돌보지 않는 한 언제라도 그 빛을 잊어버리고 존재를 상실할 수도 있는 별들이지."
              숲은 거대한 암흑으로 변했고 그 위의 밤하늘은 온통 빛무리들 뿐이었다. 칼의 말은 이어졌다.
              "그러나 우리는 서로를 바라볼 줄 아오. 밤하늘은 어둡고, 주위는 차가운 암흑 뿐이지만, 별은 바라보는 자에겐 반드시 빛을 주지요. 우리는 어쩌면 서로를 바라보는 눈동자 속에 존재하는 별빛 같은 존재들이지. 하지만 우리의 빛은 약하지 않소. 서로를 바라볼 때 우리는 우리의 모든 빛을 뿜어내지.""나 같은 싸구려 도둑도요?"
              네리아의 목소리는 슬프지 않았다. 그리고 칼의 대답도 평온했다.
              "이제는 아시겠지? 네리아 양. 당신들 주위에 우리가 있고, 우리는 당신을 바라본다오. 그리고 당신은 우리들에게 당신의 빛을 뿜어내고 있소. 우리는 서로에게 잊혀질 수 없는 존재들이오. 최소한 우리가 서로를 바라보는 이상은."
              어둠 속에서 네리아의 눈이 별처럼 아름답게 반짝였다. 나는 혹시 반짝인 것은 그녀의 눈물이 아닐까 따위의 생각은 관두기로 했다. 그래서 고개를 돌려 밤하늘을 바라보았다.
              내가 바라보자, 별들은 나에게 빛을 주었다.
              - 본문 중-</p>
       </div>
      
  </body>
  ```



- position

  - 1. 정적 위치(static position) 지정 방식

    2. 상대 위치(relative position) 지정 방식

    3. 고정 위치(fixed position) 지정 방식

    4. 절대 위치(absolute position) 지정 방식

  - 정적위치 : 

    position 속성값이 static으로 설정된 요소는 top, right, bottom, left 속성값에 영향을 받지 않습니다.

    정적 위치(static position) 지정 방식은 단순히 웹 페이지의 흐름에 따라 차례대로 요소들을 위치시키는 방식입니다.

  - 상대 위치(relative position) 지정 방식 :

    상대 위치(relative position) 지정 방식은 해당 HTML 요소의 기본 위치를 기준으로 위치를 설정하는 방식입니다.

    HTML 요소의 기본 위치란 해당 요소가 정적 위치(static position) 지정 방식일 때 결정되는 위치를 의미합니다.

  - 고정위치:

    고정 위치(fixed position) 지정 방식은 뷰포트(viewport)를 기준으로 위치를 설정하는 방식입니다. 

    즉, 웹 페이지가 스크롤 되어도 고정 위치로 지정된 요소는 항상 같은 곳에 위치하게 됩니다.

  - 절대 위치(absolute position) 지정 방식

    절대 위치(absolute position) 지정 방식은 고정 위치가 뷰포트를 기준으로 위치를 결정하는 것과 비슷하게 동작합니다.

    단지 뷰포트(viewport)를 기준으로 하는 것이 아닌 위치가 설정된 조상(ancestor) 요소를 기준으로 위치를 설정하게 됩니다.

    하지만 위치가 설정된 조상(ancestor) 요소를 가지지 않는다면, HTML 문서의 body 요소를 기준으로 위치를 설정하게 됩니다.

  - ```html
    <style>
            *{
                margin:0px;
                padding:0px;
            }
            /*
            relative: 원래 자신의 위치에서 얼마나 움직이는지
            absolute : 부모의 위치 기준으로, 상대적으로 얼마나 움직이는지
            fixed : 브라우저 기준으로, 얼마나 움직이는지
            */
            /* 부모 #box에 relative를 걸어주지 않으면 자식들은 body 기준으로 움직임 */
            #box{
                position:relative;
                width: 500px;
                margin: 10px;
                padding: 10px;
                border: 1px dotted red;
            }
            p{
                width:150px;
                height: 150px;
                color:#fff;
                font-weight: bold;
            }
            .myred{
                background: red;
                position: relative;
            }
            /* 부모 : # box를 기준으로 왼쪽으로 100만큼 아래쪽으로 30만큼 이동 */
            .myblue{
                background: blue;
                position:absolute;
                left: 100px;
                top: 30px;
                z-index: 2;
            }
            /* 자기 자신을 기준으로 움직임 , 원래 위치 : 빨강 밑  */
            .mygreen{
                background: green;
                position: relative;
                left: 30px;
                top: -30px;
            }
    
            /* z값이 커지니까 가장 앞으로 나온다 */
            .myred:hover{
                z-index: 100;
            }
    
            .myblue:hover{
                z-index: 100;
            }
    
            .mygreen:hover{
                z-index: 100;
            }
            #fixed{
                width: 100px;
                height: 300px;
                background: silver;
                position: fixed;
                right: 50px;
                top: 100px;
            }
    
        </style>
    </head>
    <body>
    
        <div id="box">
            <p class="myred">빨간 박스</p>
            <p class="mygreen">초록 박스</p>
            <p class="myblue">파란 박스</p>
        </div>
        <div id="fixed">
            Fixed!!!!
        </div>
        <br><br><br><br><br><br><br><br><br><br>
        <br><br><br><br><br><br><br><br><br><br>
        <br><br><br><br><br><br><br><br><br><br>
        <br><br><br><br><br><br><br><br><br><br>
        <br><br><br><br><br><br><br><br><br><br>
        
    </body>
    ```



- Transform

  - translate , roatate, scale , skew 

  - ```html
    <style>
            div{
                width : 200px;
                height: 200px;
                background: red;
                color: white;
                font-size: 30pt;
                word-wrap: break-word;
            }
            /* 이동*/
            #tlate{ 
                transform: translate(50px, 50px); 
            }
            /* 회전 */
            #trotate{
                transform: rotate(30deg);
            }
            /* 크기 조절 */
            #tscale{
                transform:scale(0.5 , 0.5);
            }
            /* 왜곡 , 변형 */
            #skew{
                transform: skew(20deg , 10deg);
            }
            /* 이동하는 효과 */
            #tran{
                transition: width 0.5s , background 1.5s linear , transform 1.5s;
            }
            #tran:hover{
                transform:translate(100px, 0px)
            }
            li{
                width: 300px;
                background: gray;
                margin-bottom: 3px;
                font-size: 30pt;
                font-weight: bold;
                list-style-type: none;
                cursor: pointer;
    
                transition: width 1s linear, color 1s linear, letter-spacing 1s;
            }
            li:hover{
                /* letter spacing 효과 */
                width: 400px;
                color: red;
                letter-spacing: 5px;
            }
        </style>
    </head>
    <body>
        <h1>Transform</h1>
        <h2>Transform - translate</h2>
        <div id="tlate">translate(x,y): 위치 이동</div>
    
        <h2>Transform - rotate</h2>
        <div id="trotate">rotate(deg): 회전</div>
    
        <h2>Transform-scale</h2>
        <div id="tscale">scale(x,y) : 크기 </div>
        
        <h2>Transform-skew</h2>
        <div id="skew">skew(deg , deg) : 변형</div>
    
        <h2>Transition 속성 전환 - </h2>
        <div id="tran"> transition </div>
    
        <h2>MENU</h2>
        <ul>
            <li>학원소개</li>
            <li>과정소개</li>
            <li>채용정보</li>
            <li>커뮤니티</li>
        </ul>
    </body>
    </html>
    ```

    
