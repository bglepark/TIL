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



- JQuery 기본 문법

  - $(선택자).동작함수();

  - 달러($) 기호는 제이쿼리를 의미하고, 제이쿼리에 접근할 수 있게 해주는 식별자입니다.

    선택자를 이용하여 원하는 HTML 요소를 선택하고, 동작 함수를 정의하여 선택된 요소에 원하는 동작을 설정합니다.

- $() 함수

  - $() 함수는 선택된 HTML 요소를 제이쿼리에서 이용할 수 있는 형태로 생성해 주는 역할을 합니다.

  - $() 함수의 인수로는 HTML 태그 이름뿐만 아니라, CSS 선택자를 전달하여 특정 HTML 요소를 선택할 수 있습니다.

    이러한 $() 함수를 통해 생성된 요소를 제이쿼리 객체(jQuery object)라고 합니다.

    제이쿼리는 이렇게 생성된 제이쿼리 객체의 메소드를 사용하여 여러 동작을 설정할 수 있습니다.

- Document 객체의 ready() 메소드

  - 자바스크립트 코드는 웹 브라우저가 문서의 모든 요소를 로드한 뒤에 실행되어야 합니다.

    보통은 별다른 문제가 발생하지 않지만, 다음과 같은 경우에는 오류가 발생합니다.

     

     \- 아직 생성되지 않은 HTML 요소에 속성을 추가하려고 할 경우

     \- 아직 로드되지 않은 이미지의 크기를 얻으려고 할 경우



## jq01-basic

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

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
                //도큐먼트 먼저 다 읽은 후에 함수 불러오기
            });
            $(function(){}); 이라고도 많이 사용하는데

$(document).ready(function(){});와 동일한 의미입니다.

$(document).ready(function(){}); 이것이 jQuery를 사용하기 위한 기본 문법입니다.

정확히는 DOM(Document Object Model) 객체가 생성되어 준비되는 시점에서 호출된다는 의미입니다.

JS와 비교하자면 document.onload()... 와 거의 비슷하다

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

## jq02-selector

CSS 선택자

- 태그 이름으로 선택 : $("span")
- id로 선택 : $("#t1")
- class로 선택 : $(".t2")
- parent child로 선택 : $("li span")  => li : parent / span : child
- parent>child로 선택 : $("li > span") => li의 직계 span 태그만 선택함
- nth-child로 선택 : $("li:nth-child()") => 빈 칸에 n/odd/even 가능
- first-child로 선택 : $("li:first-child")
- last-child로 선택 : $("li:last-child")
- 전체 선택 : $("*")

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <!-- 링크로 jquery 불러오기 -->
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>

    <script>
        $(document).ready(function(){
            //$(document).ready()는 문서가 준비되면 매개변수로 넣은 콜백 함수를 실행하라는 의미입니다.
            //div 부분의 0번째 인덱스를 반환
            $("div:eq(0)").css({"border":"1px solid red" , "width":"400px", "height":"200px"})
            $("#view").css({"border":"1px solid red" , "width":"400px", "height":"100px"})
        })

        //태그 이름으로 선택
        function selector01(){
            $("span").css("color", "red");
            $("#view").text('$("span").css("color","red");')
        }

        //id로 선택
        function selector02(){
            $("#t1").css("color" , "green");
            $("#view").text('$("#t1").css("color" , "green")')
        }

        //class 선택
        function selector03(){
            $(".t2").css("color" , "violet");
            $("#view").text('$(".t2").css("color" , "violet");')
        }

        // p c 선택 (parent child) 
        function selector04(){
            $("li span").css("background-color" , "blue");
            $("#view").text('$("li span").css("background-color" , "blue")')    
        }

        // p>c 선택 -> b태그가 있는 부분은 선택이 안됨
        function selector05(){
            $("li > span").css("color" , "yellow")
            $("#view").text('$("li > span").css("color" , "yellow")')
        }

        // nth-child 선택 -> 6대신 odd 쓰면 홀수만 , even 쓰면 짝수만
        function selector06(){
            $("li:nth-child(6)").css("background-color" , "yellow");
            $("#view").text('$("li:nth-child(6)").css("background-color" , "yellow");')
        }
        //first - child 선택
        function selector07(){
            $("li:first-child").css("background-color" , "yellowgreen");
            $("#view").text('$("li:first-child").css("background-color" , "yellowgreen")')
        }

        // last-child 선택
        function selector08(){
            $("li:last-child").css("color" , "orange");
            $("#view").text('$("li:last-child").css("color" , "orange")')
        }

        function cls(){
            //black이 default라서 아무것도 입력 안해도 된다
            // css 를 연결해서 사용 가능 -> method chaining
            $("*").css("color" , "black").css("background-color" , "")
            $('#view').text("")
        }

    </script>
</head>
<body>

    <h1>css 선택자</h1>

    <div>
        <ul>
            <li><span>tag로 선택</span></li>
            <li id="t1">id로 선택</li>
            <li class="t2">class로 선택</li>
            <li><span>parent child로 선택</span></li>
            <li><b><span>parent &gt; child</span></b>로 선택</li>
            <li>:nth-child(n/odd/even)로 선택</li>
            <li>:first-child로 선택</li>
            <li>:last-child로 선택</li>
        </ul>
    </div>
    <br>
    <div>
        <button onclick="selector01()">태그선택(span)</button>
        <button onclick="selector02()">id선택(t1)</button>
        <button onclick="selector03()">class선택(t2)</button>
        <button onclick="selector04()">p c 선택</button>
        <button onclick="selector05()">p &gt; c선택</button>
        <button onclick="selector06()">nth-child 선택</button>
        <button onclick="selector07()">first-child 선택</button>
        <button onclick="selector08()">last-child 선택</button>
        <br>
        <button onclick="cls()">reset</button>
    </div>

    <h2>코드 내용</h2>
    <div id="view"></div>
    
</body>
</html>
```



- JQuery 선택자

- 선택한 요소의 필터링

- | :eq(n)            | 선택한 요소 중에서 인덱스가 n인 요소를 선택함.               |
  | ----------------- | ------------------------------------------------------------ |
  | :gt(n)            | 선택한 요소 중에서 인덱스가 n보다 큰 요소를 모두 선택함.     |
  | :lt(n)            | 선택한 요소 중에서 인덱스가 n보다 작은 요소를 모두 선택함.   |
  | :even             | 선택한 요소 중에서 인덱스가 짝수인 요소를 모두 선택함.       |
  | :odd              | 선택한 요소 중에서 인덱스가 홀수인 요소를 모두 선택함.       |
  | :first            | 선택한 요소 중에서 첫 번째 요소를 선택함.                    |
  | :last             | 선택한 요소 중에서 마지막 요소를 선택함.                     |
  | :animated         | 선택한 요소 중에서 애니메이션 효과가 실행 중인 요소를 모두 선택함. |
  | :header           | 선택한 요소 중에서 h1부터 h6까지의 요소를 모두 선택함.       |
  | :lang(언어)       | 선택한 요소 중에서 지정한 언어의 요소를 모두 선택함.         |
  | :not(선택자)      | 선택한 요소 중에서 지정한 선택자와 일치하지 않는 요소를 모두 선택함. |
  | :root             | 선택한 요소 중에서 최상위 루트 요소를 선택함.                |
  | :target           | 선택한 요소 중에서 웹 페이지 URI의 fragment 식별자와 일치하는 요소를 모두 선택함. |
  | :contains(텍스트) | 선택한 요소 중에서 지정한 텍스트를 포함하는 요소를 모두 선택함. |
  | :has(선택자)      | 선택한 요소 중에서 지정한 선택자와 일치하는 자손 요소를 갖는 요소를 모두 선택함. |
  | :empty            | 선택한 요소 중에서 자식 요소를 가지고 있지 않은 요소를 모두 선택함. |
  | :parent           | 선택한 요소 중에서 자식 요소를 가지고 있는 요소를 모두 선택함. |



## jq03-input

- input 요소에서 사용하는 선택자

- 

- |  선택자   |                             설명                             |
  | :-------: | :----------------------------------------------------------: |
  |  :button  |         type 속성값이 "button"인 요소를 모두 선택함.         |
  | :checkbox |        type 속성값이 "checkbox"인 요소를 모두 선택함.        |
  |   :file   |          type 속성값이 "file"인 요소를 모두 선택함.          |
  |  :image   |         type 속성값이 "image"인 요소를 모두 선택함.          |
  | :password |        type 속성값이 "password"인 요소를 모두 선택함.        |
  |  :radio   |         type 속성값이 "radio"인 요소를 모두 선택함.          |
  |  :reset   |         type 속성값이 "reset"인 요소를 모두 선택함.          |
  |  :submit  |         type 속성값이 "submit"인 요소를 모두 선택함.         |
  |   :text   |          type 속성값이 "text"인 요소를 모두 선택함.          |
  |  :input   |  <input>, <textarea>, <select>, <button>요소를 모두 선택함.  |
  | :checked  | type 속성값이 "checkbox" 또는 "radio"인 요소 중에서 체크되어 있는 요소를 모두 선택함. |
  | :selected |        <option>요소 중에서 선택된 요소를 모두 선택함.        |
  |  :focus   |           현재 포커스가 가지고 있는 요소를 선택함.           |
  | :disabled |             비활성화되어있는 요소를 모두 선택함.             |
  | :enabled  |              활성화되어있는 요소를 모두 선택함.              |



```html
 <script src="resources/js/jquery-3.6.0.min.js"></script>
    <script>
        function inputText(){
            // input 태그 중에서 type이 text인 변수를 가져와라
            var txt = $("input:text").val()
            //JS : value();
            //JQ : val()
            alert(txt)
        }

        function inputRadio(){
            var radioVal = $("input:radio").val()
            $("#a").html(radioVal)
            //JS : innerhtml
            //JQ : html
        }

        function inputCheck(){
            var checkVal = $("input:checkbox").val()
            $("#a").html(checkVal)

        }

        //select 해서 바뀌는 이벤트
        // select 태그 밑 option에서 selected 된거 선택
        // 이 상태면 로딩이 안되어 있어서 실행이 안됨
        // $(function(){} 이 있어야 함)
        // function 없이 맨 밑에 scipt 태그 넣어서 실행하면 동작한다 -> body가 만들어진 이후에 되기 때문에

        $(function(){
            $("select").change(function(){
            var option = $("select>option:selected");
            alert(option.val())
            alert($("select>option").index(option))
        });})
        

    </script>
</head>
<body>
    <form>
        <input type="text">
        <br>
        <input type="button" value="선택" onclick="inputText()">
        <br>
        <input type="radio" value="radio val" onclick="inputRadio()">radio
        <br>
        <input type="checkbox" value="check val" onclick="inputCheck()">check
        <br>
        <div id="a"></div>
        <select>
            <option value="one">1</option>
            <option value="two">2</option>
            <option value="three">3</option>
        </select>
    </form>
</body>
</html>
```



## jq04-checkbox

```html
 <script src="resources/js/jquery-3.6.0.min.js"></script>

    <script>
        //JS : onsubmit()
        //JQ : submit()
        // 이벤트가 발생할 때마다 실행할 함수
        // submit 버튼을 클릭했을 때 , form 태그 안의 action 경로로 method의 방식으로 안에 있는 value값을 쿼리 스트링으로 전달
        // submit이 발생했을때 빈 공간이면 error 메세지를 보여라!
        $(function(){
            $("#signal").submit(function(){
                if($(".infobox").val()== null || $(".infobox").val()==""){
                    $(".error").show()
                    // 원래는 submit을 하고 form 태그로 넘어가야하는데, 위의 if문으로 거짓일 경우 false로 return하고 멈춰라!!
                    return false;
                }

            });

            $("#confirm").click(function(){
                $("#result").empty();
                
                var total = 0;
                // checkbox 중 checked 되어 있는 요소들을 가지고 와서
                // .each() 를 사용하여 해당 요소들의 가격을 가져오고
                // jquery의 결과가 반복 가능한 객체이다 -> 하나하나 each에 각각의 function을 적용할 것이다
                // python의 map과 동일
                $("input[name=chk]:checked").each(function(i){
                    // i는 index를 가지고 온다!!
                    // console.log(i)
                    // var chk = $(this);
                    var chk = $("input[name=chk]:checked").eq(i); //i번지에 있는 변수 가져옴
                    // console.log(chk);
                    var book = chk.next().text(); //선택된 check박스의 옆에 있는 형제 가지고 와서 text 가져옴
                    var price = chk.val();
                    $("#result").append(book + " : " + price + "<br/>")
                    
                    total += parseInt(price )
                    
                });
                // 더해서
                // id가 result인 요소의 안에 값을 출력하자
                $("#result").append("총가격 : " +  total)
                
                

            })

            //숙제 : 모두 선택되어 있으면 name이 all인 체크박스도 체크
            // 하나라도 체크 해제되면 name이 all인 체크박스 체크 해제
            // : 은 가상 클래스 선택자를 의미함
            $("input[name=chk]").click(function(){
                if($("input[name=chk]").length == $("input[name=chk]:checked").length){
                    $("input[name=all]").prop("checked" , true)
                }
                else{
                    $("input[name=all]").prop("checked" , false)
                }

            })


        })

        // 숙제 
        function allChk(bool){
            //구현하기
            //input 태그를 가지고 와서 name이라는 속성이 있는 chk를 가져옴
            // each 각각에 function 적용
            // property -> checked 속성을 bool (True or False)로 바꿔주자
            $("input[name=chk]").each(function(){
                $(this).prop('checked' , bool)
            })
        }


    </script>
</head>
<body>

    <form id="signal">
        <div>
            <span class="label">User ID</span>
            <input type="text" class="infobox" name="userid">
            <span class="error" hidden="" style="color:red">반드시 입력하세요!!</span>
        </div>
        <input type="submit" class="submit" value="입력">
    </form>

    <hr>
    <fieldset style="width:300px">
        <legend>체크 여부 확인</legend>
        <input type="checkbox" name="all" onclick="allChk(this.checked)">전체선택
        <br>
        <input type="checkbox" name="chk" value="20000"><b>python</b>
        <br>
        <input type="checkbox" name="chk" value="25000"><b>pandas</b>
        <br>
        <input type="checkbox" name="chk" value="30000"><b>django</b>
        <br>
        <input type="button" value="확인" id="confirm"/><br>

        <span>선택한 책 가격</span>
        <div id="result"></div>
    </fieldset>
    
</body>
</html>
```



## jq05-dom01

```html
<script src="resources/js/jquery-3.6.0.min.js"></script>

    <script>
        $(function(){
            $("div>p").eq(0).click(function(){
                $("pre b").eq(0).toggle()
            })
            $("div>p").eq(1).click(function(){
                $("pre b").slice(1,2).toggle()
            })
            $("div>p").eq(2).click(function(){
                // $("pre b").first().css("color" , "red");
                // $("pre b").eq(2).toggle()
                // 하나로 합치기 -> end()를 넣으면 그 다음요소로 가서 찾아주세요 라는 뜻
                $("pre b").first().css("color" , "red").end().eq(2).toggle().end().last().text("진짜되네") // 다 앞에 있는 덩어리에 적용됨
            })
            $("div>p").eq(3).click(function(){
                $("pre b").last().css("background-color" , "skyblue")
            })
        })
    </script>
</head>
<body>

    <pre>
        <b>eq() : 선택한 엘리먼트들 중에 인덱스로 탐색</b>
        <b>slice() : 선택한 엘리먼트들 중에 인덱스 길이로 탐색</b>
        <b>first() : 선택한 엘리먼트들 중에 첫번째 요소</b>
        <b>last() : 선택한 엘리먼트들 중에 마지막 요소</b>
    </pre>

    <div>
        <p>eq()</p>
        <p>slice()</p>
        <p>first()</p>
        <p>last()</p>
    </div>
    
</body>
</html>
```



## jq06-dom02

```html
<script src = "resources/js/jquery-3.6.0.min.js"></script>
    <script>
        //$ function이랑 같은 기능
        $(document).ready(function(){
            $("div").find("b").css({"font-size":"30px", "color":"red"})
            $("div").children("#chd").text("2.children()")
            $("p>b").parent().css("background-color" , "hotpink") //div랑 p 둘다 찾아버림 -> p>b 사용
            $("p>b").parents("div").css("background-color","yellow");
            $("p").eq(0).next().css("color" , "blue") //p의 0번지 다음꺼 (1번지)
        })
    </script>

</head>
<body>

    <pre>
        <b>find("selector") : 선택한 엘리먼트의 자손들 중에 탐색</b>
        <b>children("selector") : 선택한 엘리먼트의 자식들 중에 탐색</b>
        <b>parent() / parents("selector") : 선택한 엘리먼트의 부모 / 조상 탐색</b>
        <b>next("selector") : 선택한 엘리먼트 다음에 따라오는 요소 탐색</b>
    </pre>

    <div>
        <p><b>1</b></p>
        <p id="chd">2</p>
        <p>3</p>
        <p>4</p>
        <p>5</p>
    </div>
    
</body>
</html>
```



## jq07-dom03

```html
<script src="resources/js/jquery-3.6.0.min.js"></script>
    <script>
        $(function(){
            $("p:eq(0)").add("span").css("color" , "red")
            
            ///확인 필요ㅕ!!!!!!!!!
            $("div").children().click(function(){
                if($(this).prop("tagName") =="SPAN"){ //nodename 가져오면 대문자로 가져옴
                    alert("span tag click")
                    $(this).css("color" , "blue");
                    
                }
                if($(this).is("p")){
                    $(this).css("background-color" , "violet")
                }
            });

            $('b').click(function(){
                $("div").children().css("background-color" , "");
                $("p:eq(0)").add("span").css("color","red")
            })
        })
        // attr() : HTML의 속성(attribute)
        // prop() : JS의 속성(property)
        


    </script>
</head>
<body>
    
    <div>
        <p>add()</p>
        <span>add():선택한 엘리먼트에 추가적으로 selector 표현식을 작성할 때 사용</span>
        <p>is()</p>
        <b> 선택한 엘리먼트들 중에 구하는 엘리먼트가 있는지 확인할 때 사용</b>
    </div>
    
</body>
</html>
```



## jq08-dom04

```html
<script src="resources/js/jquery-3.6.0.min.js"></script>
    <script>
        $(function(){
            $("p:eq(0)").add("span").css("color" , "red")
            
           
            $("div").children().click(function(){
                if($(this).prop("tagName") =="SPAN"){ //nodename 가져오면 대문자로 가져옴
                    alert("span tag click")
                    $(this).css("color" , "blue");
                    /* text-decoration : none => 기본값으로 밑줄이 없는 보통 문자 */
                    
                }
                if($(this).is("p")){
                    $(this).css("background-color" , "violet")
                }
            });

            $('b').click(function(){
                $("div").children().css("background-color" , "");
                $("p:eq(0)").add("span").css("color","red")
            })
        })
        // attr() : HTML의 속성(attribute)
        // prop() : JS의 속성(property)
        


    </script>
</head>
<body>
    
    <div>
        <p>add()</p>
        <span>add():선택한 엘리먼트에 추가적으로 selector 표현식을 작성할 때 사용</span>
        <p>is()</p>
        <b> 선택한 엘리먼트들 중에 구하는 엘리먼트가 있는지 확인할 때 사용</b>
    </div>
    
</body>
</html>
```



## jq09-event

```html
 <style>
        div{
            width: 400px;
            height: 200px;
            border: 2px solid red;
            padding: 20px;
            overflow: auto;
        }
        div p:first-child{
            float:left;
            border: 1px solid blue;
            width: 150px;
            height: 150px;
            text-align: center;
            line-height: 150px;
        }

        div p:last-child{
            float: right;
            border: 1px solid blue;
            width: 150px;
            height: 150px;
            text-align: center;
            line-height: 150px;
        }
    </style>

    <script src="resources/js/jquery-3.6.0.min.js"></script>

    <script>
        /*
            이벤트 전파 : 각 요소가 서로 포함관계(중첩)인 경우
                            요소 중 하나에 이벤트가 발생하면
                            중첩된 요소들도 이벤트가 전파된다

            이벤트 전파 막기
                    - stopPropagation() : 이벤트 요소의 전파 막기
                    - preventDefault() : 이벤트에 의한 기본 동작 막기
                    - return false : 위의 기능 두개 모두 적용
                    
        */

        $(function(){
            $("a:eq(0)").click(function(e){
                //a가 전달 이후 감싸고 있는 p클릭 이후 감싸고 있는 div 클릭
                // 이벤트가 다 발생한 이후 기본동작(naver로 가기) 작동
                alert("a클릭")
                // e.stopPropagation(); //a클릭만 발생하고 네이버로 이동 -> 이벤트를 전파하지 마셈
                // e.preventDefault(); //a클릭->p클릭->div클릭->네이버로 이동하지 않는다(기본동작을 막아라)
                return false; // return을 false로 했기 때문에 이벤트 전파를 막음, 위의 기능 두개를 모두 적용
            })
            $("p").click(function(e){
                alert("p 클릭")
                e.preventDefault() //여기서 말하는 e는 a꺼다. -> 기본동작(네이버) 작동 안하게함 -> a에 e없어도 됨
            })
            $("div").click(function(){
                alert("div 클릭!")
            })

            //bind : 특정 요소에 이벤트를 묶어준다
            // $("a:eq(1)").bind("mouseover mouseout", function(e){
            //     if(e.type == "mouseover"){
            //         $(this).css("background-color" , "hotpink")
            //     }
            //     if(e.type == "mouseout"){
            //         $(this).css("background-color" , "")
            //     }
            // });

            //다음과 같이도 가능
            $("a:eq(1)").bind({
                "mouseover":function(){
                    $(this).css("color" , "gold")
                },
                "mouseout":function(){
                    $(this).css("color" , "")
                }
            })

            //클릭하면 이벤트 해제
            $("span").click(function(){
                $("a:eq(1)").unbind();

            })

            $("button").click(function(){ //위의 이벤트는 onload와 같이 function은 자바스크립트가 다 만들어진 이후에 자바스크립트를 읽어라
                // "p"는 이미 만들어진 애들만 찾는다 -> 걔네들한테만 클릭 이벤트가 걸린다.

                $("body").append("<p>새로 추가된 p</p>")
            })

            $("body").on("click" , "p" , function(){
                // body태그의 자식요소인 p를 클릭했을 때 적용해라
                // body 안에 있는 p태그에다가 click 이벤트를 on 처럼 연결한다 (이벤트를 on)
                alert("새로 추가된 요소도 이벤트 적용!") //얘도 alert 적용됨(이벤트 적용됨)
            })
            // JS : addEventListener 사용하기
            // JQ : on 사용

        })
    </script>
</head>
<body>

    <span>unbind() : 이벤트 해제</span>
    <div>
        <p>
            <a href="https://www.naver.com">클릭!</a>
        </p>
        <p>클릭</p>
    </div>

    <div>
        <p>
            <a href="https://www.google.com">클릭!</a>
        </p>
        <p>클릭</p>
    </div>

    <button>요소 추가</button>
    
</body>
</html>
```



## jq10-accordian

```html
<style>
        .main_menu{width:300;}
        .sub_menu1{cursor:pointer}
        .sub_menu2{display: none; cursor: default;}
    </style>

    <script src="resources/js/jquery-3.6.0.min.js"></script>

    <script>
        $(function(){
            //b 태그를 클릭했을 때
            $("b").click(function(){
                // b 태그 기준으로 보여져야 되는 것들(슬라이드로 표기)
                // $(this).next().slideToggle()

                // b 태그 기준으로 숨겨져야 되는 것들 생각
                
                // $('.sub_menu2').prev().not($(this)).next().slideUp()
                // $(this).parent().siblings().find("ul").slideUp()

                //2번과 3번을 한줄로 -> end() : 다시 this로 가세요
                $(this).next().slideToggle().end().parent().siblings().find("ul").slideUp()
                
            })
            
        })

    </script>
</head>
<body>

    <p>메뉴 만들기</p>
    <ul type="square" class="main_menu">
        <li class="sub_menu1">
            <b>(1)css선택자</b>
            <ul type="circle" class="sub_menu2">
                <li>tag 선택</li>
                <li>id 선택</li>
                <li>class 선택</li>
                <li>parent child 선택</li>
                <li>parent &gt; child 선택</li>
                <li>:nth-child 선택</li>
                <li>:first-child 선택</li>
                <li>:last-child 선택</li>
            </ul>
        </li>

        <li class="sub_menu1">
            <b>(2)속성 선택자</b>
            <ul type="circle" class="sub_menu2">
                <li>[attr]</li>
                <li>[attr=value]</li>
                <li>[attr!=value]</li>
            </ul>

        </li>

        <li class="sub_menu1">
            <b>(3)폼 선택자</b>
            <ul type="circle" class="sub_menu2">
                <li>:input 타입</li>
            </ul>
        
        </li>


        <li class="sub_menu1">
            <b>(4)사용자 정의</b>
            <ul type="circle" class="sub_menu2">
                <li>:eq</li>
                <li>:first</li>
                <li>:last</li>
                <li>:even</li>
                <li>:odd</li>
                <li>:parent</li>
            </ul>
        </li>

        
    </ul>
    
</body>
</html>
```



## jq11-class

```html
 </style>

    <script src="resources/js/jquery-3.6.0.min.js"></script>
    <script>
        $(document).ready(function(){
            $("#btn").click(function(){
                $("img").toggleClass("onoff"); //클릭하면 클래스를 없애고 만들어라

                
            })
            $("img").click(function(){
                    if($(this).hasClass("addsize")){
                        $(this).removeClass("addsize").attr("title" , "이미지 축소됨")
                    } else{
                        $(this).addClass("addsize").attr("title" , "이미지 확대됨")
                    }
                })

                /*
                    .attr() : html
                    .prop() : js/jq(object)

                    
                */
        })
    </script>
</head>
<body>

    <button id = "btn">class on/off</button>
    <br>
    <img src="resources/imgs/img01.png" alt="img01" title="이미지 1번">
    <img src="resources/imgs/img02.png" alt="img02" title="이미지 2번">
    <img src="resources/imgs/img03.png" alt="img03" title="이미지 3번">
    
</body>
</html>
```



## jq12-insert

```html
<style>
        div{border: 1px solid red;}
        .prepend{border: 1px dotted green;}
        .append{border: 1px dotted blue;}
    </style>

    <script src="resources/js/jquery-3.6.0.min.js"></script>
    <script>
        $(function(){
            var cnt=0;
            $("button:eq(0)").click(function(){
                $("div").prepend($("<p>").addClass("prepend").text("prepend"+(++cnt)))
                    //div 의 자식요소들 중에 가장 앞에 추가됨
                    //document.createElement("p")와 동일 -> p태그를 만들어줌
                    // p태그 만들어서 class 추가하고 text 추가함
            })
            $("button:eq(1)").click(function(){
                $("div").append($("<p>").addClass("append").text("append"+(++cnt)))
                    // append 누르면 자식 요소들 중에 가장 마지막에 추가
            })
            $("button:eq(2)").click(function(){
                $("div").html("<b>html 요소를 바꾼다.</b>")
                //bold처리된 문자열로 html 요소가 바뀜
            })
            $("button:eq(3)").click(function(){
                $("div").text("<b>text 요소를 바꾼다.</b>")
                // text요소 그대로 출력된다
            })
        })
    </script>
</head>
<body>

    <button>prepend</button>
    <button>append</button>
    <button>html</button>
    <button>txt</button>

    <div>
        <p>내부 삽입1</p>
        <p>내부 삽입2</p>
    </div>
    
</body>
</html>
```



## jq13-insert

```html
<style>
        div{border:1px solid red}
    </style>
    <script src="resources/js/jquery-3.6.0.min.js"></script>
    <script>
        $(function(){
            $("button:eq(0)").click(function(){
                $("#base").after("<div>새로운 엘리먼트(after)</div>")
            })

            $("button:eq(1)").click(function(){
                $("<div>새로운 엘리먼트(insertAfter)</div>").insertAfter("#base")
            })

            $("button:eq(2)").click(function(){
                // target이 앞 , 기준을 잡고 function에서 return 되는 값도 넣어줄 수 있다.
                $("#base").before("<div>새로운 엘리먼트(before)</div>")
            })

            $("button:eq(3)").click(function(){
                // target이 뒤 , 함수를 넣을 순 없다.
                $("<div>새로운 엘리먼트(insertBefore)</div>").insertBefore("#base")
            })
        })
    </script>
</head>
<body>

    <button>after()</button>
    <button>insertAfter()</button>
    <button>before()</button>
    <button>insertBefore()</button>

    <div id="base">
        <p>외부 삽입</p>
    </div>
    
</body>
</html>
```



## jq14-replace

```html
<script src="resources/js/jquery-3.6.0.min.js"></script>

    <script>
        $(function(){
            $("button:first").click(function(){
                // target이 앞
                // 이미 만들어져 있는애 선택하고 나서 바꾸기 때문에 함수 삽입 가능
                $("p").replaceWith("<p><b>replaceWith()</b></p>")
            })
            $("button:last").click(function(){
                // target이 뒤
                // 앞은 언제 만들어질지 몰라서 함수 삽입이 불가능하다
                $("<p><b>replacaAll()</b></p>").replaceAll("p")
            })
        })
    </script>
</head>
<body>
    <div>
        <p>DOM 대체</p>
    </div>

    <button>바꾸기(replaceWith)</button>
    <button>바꾸기(replaceAll)</button>

</body>
</html>
```



## jq15-slotmachine

```html
<style>
        img{
            width:150px;
            height: 150px;
            float: left;
        }
        #menubox{position:relative} 
        /* 요소 자신을 기준으로 배치 : relative */
        #menu{overflow: auto;}
        /* 컨텐츠가 넘칠 경우 스크롤바가 자동을 생성됨. */
        .sel{
            /* sel : 테두리 선 */
            width:140px;
            height: 140px;
            border:5px dotted red;
            position: absolute;
            left: 300px;
        }
        button{
            width: 150px;
            height: 50px;
            margin-left: 300px;
        }
    </style>

    <script src="resources/js/jquery-3.6.0.min.js"></script>
    <script>
        $(function(){
            setInterval(function(){
                //setInterval() : 일정한 시간 간격으로 코드를 반복실행하는 함수 (function, 시간간격(ms))
                // appendTo() : 해당 타겟 뒤에 원하는 요소를 붙여준다
                var div=$('#menu');
                $(".active").first().appendTo(div);
                //active 클래스의 first요소에 div라는 요소를 붙여준다.
                // 여기 함수에서는 아직 active 클래스가 생성되지 않았음

                //#menu : id가 menu인 객체를 가지고 온다
            // 버튼을 누르면 다음과 같이 class="active 가 생성됨
            // 	<img src="resources/imgs/img01.png" alt="img01" class="active>
            //             <img src="resources/imgs/img02.png" alt="img02" class="active>
            //             <img src="resources/imgs/img03.png" alt="img03" class="active>
            //             <img src="resources/imgs/img04.png" alt="img04" class="active>
            //             <img src="resources/imgs/img05.png" alt="img05" class="active>
            //             <img src="resources/imgs/img06.png" alt="img06" class="active>

            // appendTo : 자식 요소들 중에 가장 뒤에다가 요소를 추가해준다
            // append : 자식 요소들 중에 가장 뒤에다가 추가

            // append와 appendTo는 target이 앞에 오냐 뒤에 오냐 차이가 있다
            // div의 자식요소들 중에 맨 뒤에다가 ".active".first()를 추가한다.

            // DOM의 트리 안에 없는 애들을 append를 하면 자식요소로 들어가지지만
            // 이미 있는 애들을 선택해서 추가하면 이동한다. ***중요!!***
            // -> 해당 ms마다 수행한다.
            // js21 복습하기!

            }, 100)

            $("button").click(function(){
                $("img").toggleClass("active"); //클릭하면 img에 active라는 가상 클래스를 생성
                if($("button").text() == "start"){
                    $("button").text("stop");
                }else{
                    $("button").text("start")
                }
            })
        })
    </script>
</head>
<body>
    
    <h1>SlotMachine</h1>

    <div id="menubox">
        <div class="sel"></div>


        <div id="menu">
            <img src="resources/imgs/img01.png" alt="img01">
            <img src="resources/imgs/img02.png" alt="img02">
            <img src="resources/imgs/img03.png" alt="img03">
            <img src="resources/imgs/img04.png" alt="img04">
            <img src="resources/imgs/img05.png" alt="img05">
            <img src="resources/imgs/img06.png" alt="img06">
        </div>

        <button>start</button>
    </div>


</body>
</html>
```



## jq16-menu

```html
<style>
        .box{border:2px solid red}
        #menu{background-color: skyblue; text-align: center;}
        a{text-decoration: none; font-size: 20px;}
        #menu div {display: inline-block; margin-right: 10px;}
    </style>

    <script src="resources/js/jquery-3.6.0.min.js"></script>

    <script>
        $(function(){
            // $("<div>") == documnet.createElement("div")
            var $box = $("<div>").addClass("box");
            $(".sub_menu:first").wrap($box);

            $(".sub_menu").click(function(){
                $(".sub_menu").each(function(){
                    if($(this).parent().is(".box")){
                        //this : submenu라는 클래스를 가지고 있는 전부 -> 각각 하나씩 가져옴
                        $(this).unwrap(".box")
                    }
                })
                $(this).wrap($box)
                // 클릭 이벤트가 발생한 애
                // 클릭한 애만 box class로 감싸줘라
            })

            $("a").wrapInner("<span></span>")
            //a 태그 찾아서 자식요소들을 뒤에 있는 값으로 포장해라

            $("pre").wrapAll("<b></b>")
            //pre 태그 찾아서 전체를 뒤의 값으로 감싸주세요

        })
    </script>
</head>
<body>
    <div id="menu">
        <div class="sub_menu">
            <a href="#"><span>국비지원</span></a>
        </div>
    
    <div class="sub_menu">
        <a href="#">훈련검색</a>
    </div>
    <div class="sub_menu">
        <a href="#">기관검색</a>
    </div>
    <div class="sub_menu">
        <a href="#">질문답변</a>
    </div>
    <div class="sub_menu">
        <a href="#">과정후기</a>
    </div>
</div>

<pre>1</pre>
<pre>2</pre>
<pre>3</pre>
    
</body>
</html>
```



## jq17-delete

```html
<style>
        div{
            border:2px solid red;
            width: 200px;
            padding: 10px 10px;
        }
        p{
            background-color: yellow;
        }
        h1{
            border: 1px solid blue;
        }
    </style>
    <script src="resources/js/jquery-3.6.0.min.js"></script>
    <script>
        $(document).ready(function(){
            $("p:eq(0)").click(function(){
                //삭제 -> 요소 자체를 지운다
                $(this).remove()
            })
            $("p:eq(1)").click(function(){
                // 잘라내기
                var ele = $(this).detach();
                // $("h1").append(ele)
                // detach는 데이터 킵해둠 -> 나중에 insert 하고 싶을때 사용
            })
       
            $("p:eq(2)").click(function(){
                $(this).parent().empty();
                // 요소의 내용을 지운다
            })
        })
    </script>
</head>
<body>
    <h1>엘리먼트 제거하기</h1>

    <div>
        <p>remove()</p>
        <p>datach()</p>
        <p>empty()</p>
    </div>
    
</body>
</html>
```



## jq18-ajax1

```html
 <style>
        *{margin : 0px; padding: 0px;}
        table{width:400px}
        table tr:nth-child(odd){background-color: orange;}
        fieldset{width: 400px;}
        body{width:1000px; margin:50px auto}
    </style>
    <script src="resources/js/jquery-3.6.0.min.js"></script>
    <script>
        $(function(){
            $("#emp_search").click(function(){
                var empid = $("input[name=empid]").val();
                if (!isNaN(empid) && (empid >=100) && (empid <= 206)){
                    // alert(empid)

                    $.ajax({
                        url:"emplist.xml",      //통신할 경로(주소)
                        method:"get",           // 전송 방식(get(default)/post)
                        async:true,             // 비동기(default) / 동기 -> 비동기 방식은 서버에 요청하고 데이터만 슬쩍 가져옴
                        dataType:"xml",         // 전송 받을 데이터의 타입 : xml , json, html , script , ...
                        //data:{"key:value"},   // 전송할 데이터
                        success:function(data){ // 성공 했을 때
                            // alert(data);
                            var empInfo = $(data).find("EMPLOYEE_ID:contains("+empid+")").parent();

                            if((empInfo).is("ROW")){
                                $("table input").each(function(i){
                                    $(this).val($(empInfo).children().eq(i).text())
                                })
                            } else{
                                alert("검색대상이 존재하지 않습니다...")
                            }


                        },
                        error:function(request,error){ //실패 했을 때
                            alert("code:"+request.status+"\n"+"message:"+request.responseText+"\n"+"error:"+error)
                        }

                })
             } else{
                    alert("사원 번호를 다시 입력해주세요!!")
                }
            })
        })
    </script>
</head>
<body>
    
    <h1>데이터 가져오기</h1>

    <fieldset>
        <legend>사원정보 조회</legend>
        <input type="text" name="empid">
        <input type="button" id="emp_search" value="조회">
    </fieldset>

    <table>
        <tr>
            <th>사원번호</th>
            <td><input type="text" name="empnum"></td>
        </tr>
        <tr>
            <th>이  름</th>
            <td><input type="text" name="lastname"></td>
        </tr>
        <tr>
            <th>이 메 일</th>
            <td><input type="text" name="email"></td>
        </tr>
        <tr>
            <th>전화번호</th>
            <td><input type="text" name="phone"></td>
        </tr>
        <tr>
            <th>입 사 일</th>
            <td><input type="text" name="hire"></td>
        </tr>
    </table>

</body>
</html>
```



## jq19-ajax2

```html
<style type="text/css">
        *{margin:0px;padding:0px;}
        table{width: 900px;}
        table tr:nth-child(1){background: orange;}
        fieldset{width: 400px;}
        body {width: 1000px; margin: 50px auto;}
    </style>
    
    <script type="text/javascript" src="resources/js/jquery-3.6.0.min.js"></script>
    <script type="text/javascript" src="resources/js/create-table.js"></script>
    
    <script type="text/javascript">
    
        $(function(){
            $("#emp_search").click(function(){
                
                $.ajax({
                    url:"emplist.xml", //통신할 경로(주소)
                    dataType:"xml",     // xml 형태
                    success:function(data){ //성공했을 경우
                        var empRowList=$(data).find("ROW"); //ROW들만 찾아서
                        $("body").append(makeTable(empRowList));    //makeTable 함수에 전달 , return되는 값을 body에 append
                    },
                    error:function(){
                        alert("통신 실패");	
                    }
                });
                
            });
        });
    
    </script>
    
</head>
<body>
    
	<h1>데이터 가져오기</h1>

	<fieldset>
		<legend>사원 전체 조회</legend>
		<input type="button" value="조회" id="emp_search"/>
	</fieldset>

</body>
</html>
```



- create-table.js

  ```json
  //엘리먼트들에 대한 데이터를 테이블 형식으로 화면에 표현하기
  
  function makeTable(elem){
  	var $table = $("<table border=1>");
  	// <table border=1></table> 생성 -> table 태그를 하나 만듬
  	
  	//컬럼 정의하기
  	for(var i =0; i<1;i++){
  		//var empRowList=$(data).find("ROW")
  		// (elem.eq(0).children()) => EMPLOYEE_ID, LAST_NAME, EMAIL, PHONE_NUMBER, HIRE_DATE
  		var $tr=$("<tr>");
  		for(var j=0; j<elem.eq(0).children().length;j++){
  			// console.log(elem.eq(0).children().eq(j))
  			//tagName을 각각 가져온다
  			var $td=$("<td>").append(elem.eq(0).children().eq(j).prop("tagName"));
  			$tr.append($td);
  		}
  		$table.append($tr);
  	}
  	
  	//데이터 넣기
  	for(var i =0; i<elem.length;i++){
  		var $tr=$("<tr>");
  		for(var j=0; j<elem.eq(i).children().length;j++){
  			//각각의 text를 가지고 온다
  			var $td=$("<td>").append(elem.eq(i).children().eq(j).text());
  			$tr.append($td);
  		}
  		$table.append($tr);
  	}
  	
  	//만들어진 테이블 반환
  	return $table;
  }
  ```



## jq20-menu

```html
<style>
        img{
            width:200px;
            height: 200px;
            position: absolute;
            left:200px;
            top:100px
        }
        p{
            width:100px;
            border:1px solid red;
            position: absolute;
            left: 10px;
            display: none;
        }
    </style>

    <script src="resources/js/jquery-3.6.0.min.js"></script>

    <script>
        $(function(){
            $("b").click(function(){
                $("p").toggle();
                $("p").each(function(i){
                    $(this).animate({
                        "top":50*(i+1)+"px"
                    },1000)
                })
            })

            $("p").on("click" , function(){
                var ele = $(this);
                ele.css("background" , "hotpink");
                ele.siblings("p").css("background-color" , "")

                if(ele.is("p:contains(hide)")){
                    $("img").hide()
                }
                if(ele.is("p:contains(show)")){
                    $("img").show()
                }
                if(ele.is("p:contains(toggle)")){
                    $("img").toggle()
                }
                if(ele.is("p:contains(slideUp)")){
                    $("img").slideUp()
                }
                if(ele.is("p:contains(slideDown)")){
                    $("img").slideDown()
                }
                if(ele.is("p:contains(slideToggle)")){
                    $("img").slideToggle()
                }
                if(ele.is("p:contains(fadeOut)")){
                    $("img").fadeOut()
                }
                if(ele.is("p:contains(fadeIn)")){
                    $("img").fadeIn()
                }
                if(ele.is("p:contains(fadeTo)")){
                    $("img").fadeTo(400,0.2) //fadeTo(속도, 0~1 사이의 투명도, 콜백함수)
                }
                if(ele.is("p:contains(fadeToggle)")){
                    $("img").fadeToggle();
                }
                if(ele.is("p:contains(animate)")){
                    $("#image01").animate({
                        width:"500px",
                        height:"500px",
                        left:"600px",
                        top:"0px"
                    },1000)
                }
            })
        })
    </script>
</head>
<body>
    <b>메뉴</b>

    <div>
        <p>hide()</p>
        <p>show()</p>
        <p>toggle()</p>
        <p>slideUp()</p>
        <p>slideDown()</p>
        <p>slideToggle()</p>
        <p>fadeOut()</p>
        <p>fadeIn()</p>
        <p>fadeTo()</p>
        <p>fadeToggle()</p>
        <p>animate()</p>
    </div>
    <img src="resources/imgs/img01.png" alt="image01" id="image01">
</body>
</html>
```

