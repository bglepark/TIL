# JQuery

제이쿼리는 자바스크립트 언어를 간편하게 사용할 수 있도록 단순화시킨 오픈 소스 기반의 자바스크립트 라이브러리입니다.

제이쿼리를 이용하면 문서 객체 모델(DOM)과 이벤트에 관한 처리를 손쉽게 구현할 수 있습니다.

또한, Ajax 응용 프로그램 및 플러그인도 제이쿼리를 활용하여 빠르게 개발할 수 있습니다.



제이쿼리(jQuery)는 오픈 소스 기반의 자바스크립트 라이브러리입니다.

제이쿼리는 웹 사이트에 자바스크립트를 더욱 손쉽게 활용할 수 있게 해줍니다.

또한, 제이쿼리를 사용하면 짧고 단순한 코드로도 웹 페이지에 다양한 효과나 연출을 적용할 수 있습니다.



## JQuery 시작

https://jquery.com/download/

compressed / uncompressed 중 선택해서 다운로드

이후 경로를 불러와서 실행

```html
<script src = "경로/jquery-3.6.0.min.js"></script>		
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
```





## jq01-basic

```html
<style>
        img{
            width:200px;
            height: 200px;
        }
    </style>

    <!-- src로 가져온 다음에 사이에 코드 넣으면 안된다!! -->
    <script src = "resources/js/jquery-3.6.0.min.js"></script>
    <script>
        /*
            jquery 기본 작성법! (jquery 대신에 $표시를 쓴다)
            -> selector 표현식
            jQuery("selector").method();
            $("selector").method();
            -> $("p").css("color" , "red");
            ==> p 태그에 빨간색 적용

            기능 구현!!!
            원래 맨 위 script를 배치하여 함수 등을 구현하면 문서를 다 읽은 후에 실행 가능
            onload=function() {

            }
            -> 
            $(function(){

            });

            $(document).ready(function(){

            });

        */
       //아이디가 test-btn이라는 요소를 찾아와라
       $(function(){
           $("#test-btn").click(function(){
               alert("클릭했음!!")
           });  

           $("img").click(function(){
               $(this).hide();
           })
       });

       function showImg(){
        // 감춰진 그림을 보이게 하자
        $("img").show()
       }

       function resizeImg(){
        // 100 100으로 변경하자
        // css 2번 쓰기
        // $("img").css("width" , "100px").css("height" , "100px")
        // css 1번 쓰기
        $("img").css({"width":"100px" , "height":"100px"})
       }

       function addImg(){
        $("img").last().after("<img src='resources/imgs/img01.png'/>");
       }

       function toggleImg(){
        // 보였다 안보였다 하자
        $('img').toggle()
       }

    </script>
</head>
<body>
    <h1>Jquery : Javascript library</h1>

    <button id="test-btn">click me</button>
    <br>
    <button onclick="showImg();">이미지 보이기</button>
    <button onclick="resizeImg()">이미지 축소</button>
    <button onclick="addImg()">이미지 추가</button>
    <button onclick="toggleImg()">이미지 숨기기/보이기</button>
    <br>
    <br>
    <div>
        <img src="resources/imgs/img01.png" alt="img01">
    </div>
</body>
</html>
```

