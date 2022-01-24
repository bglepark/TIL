# Javascript

자바스크립트(JavaScript)는 객체(object) 기반의 스크립트 언어입니다.

HTML로는 웹의 내용을 작성하고, CSS로는 웹을 디자인하며, 자바스크립트로는 웹의 동작을 구현할 수 있습니다.

1. 자바스크립트는 객체 기반의 스크립트 언어입니다.

2. 자바스크립트는 동적이며, 타입을 명시할 필요가 없는 인터프리터 언어입니다.
3. 자바스크립트는 객체 지향형 프로그래밍과 함수형 프로그래밍을 모두 표현할 수 있습니다.



## js-basic

```html
<!-- text로 쓸꺼지만 작동 방식은 javascript로 할거다 -->
    <!-- 변수 사용은 var로 사용 , 함수는 {}로 시작 , function이 def와 같다 -->
    <script type="text/javascript">

        function embeddedFunction(){
            var doc = document.getElementsByTagName("li")[1]; /*li로 시작하는 tag의 elements를 가져옴*/
            doc.style.color = "red";
            doc.innerHTML = "<strong>javascript가 html 문서(document)를 변화시켰다!!</strong>";
        }
    </script>
    <script type="text/javascript" src="resources/js/js01.js"></script>
</head>
<body>

    <h1>js 기본문법</h1>

    <ol>
        <li onclick="alert('inline 방식!!!');">inline 방식</li>
        <li onclick="embeddedFunction();">내부 작성 방식</li>
        <li onclick="fileFunction();">외부 *.js 방식 (file)</li>
    </ol>
```

js01.js

```js
function fileFunction(){
    window.alert("외부 js file에서 실행됨!!");
    
}

// onload 는 모든걸 다 한다음에 수행해라 라는 뜸 -> alert로 표시
window.onload = function(){
    alert("윈도우 로딩 됨! (로딩 후)");
}
```



## js-var

```html
<script type="text/javascript">
        // 주석
        // 전역변수
        var variable = 10;
        function val01(){
            variable = variable+5;
            document.getElementById("value01").innerHTML= "<b style='color:red; background:yellow;'>"+variable+"</b>"
        }
    	//value01의 Element를 가지고 와서 innerHTML의 색 변경 및 variable 호출
    	// variable이 5씩 증가
        //ByID만 Element 이다 s가 안붙음 , 전역변수는 스크립트 영역 어디에서나 사용 가능하다
        /*
        여러 줄 
        주석
        입니다.
        */

        function val02(){
            //지역 변수를 가져오기 때문에 함수를 호출할 때마다 초기화돼서 5씩 증가하지 않음
            var innerVal = variable + 10;
            document.getElementById("value02").innerHTML= "<b style='color:red; background:yellow;'>"+innerVal+"</b>"
        }

        function jsType(){
            var inferVal = "문자";
            alert(inferVal + "의 타입은 : " +  typeof(inferVal));

            inferVal=33;
            alert(inferVal + "의 타입은 : " + typeof(inferVal));

            inferVal=true;
            alert(inferVal + "의 타입은 : " + typeof(inferVal));

            inferVal=null;
            alert(inferVal + "의 타입은 : " + typeof(inferVal));

            inferVal= new val01();
            alert(inferVal + "의 타입은 : " + typeof(inferVal));

            inferVal=function(){
                alert("타입 추론")
            }
            alert(inferVal+"의 타입은 : " + typeof(inferVal));
            
        }
    </script>
</head>
<body>

    <h1>var 변수 = 값;</h1>

    <dl>
        <dt>변수 선언 규칙</dt>
        <dd>대소문자 구분</dd>
        <dd>영문, $ , _로 시작</dd>
        <dd>영문 , $ , _ , 숫자 사용 가능</dd>
        <dd>키워드(예약어) 사용 불가</dd>
        <br>

        <dt>변수의 범위</dt>
        <dd>전역 변수 : window 객체에 포함됨
            <button onclick="val01();">확인</button>
            <p id="value01"></p>
        </dd>
        <dd>지역변수 : 함수나 객체 내부에 선언
            <button onclick="val02();">확인</button>
            <p id="value02"></p>
        </dd>

        <dt>타입의 종류
            <button onclick="jsType();">확인</button>
        </dt>
        <dd>string</dd>
        <dd>number</dd>
        <dd>boolean</dd>
        <dd>Null</dd>
        <dd>object</dd>
        <dd>function</dd>

    </dl>
    
</body>
</html>
```



## js-alert

```html
<script>
        function alertFunc(){
            alert("내용출력 (단순 대화창)")
        }
        function confirmFunc(){
            if(confirm("배경을 파란색으로 변환?")){
                alert("파란색으로 변환합니다.")
                document.body.style.backgroundColor='blue';

            }else{
                alert("배경색을 없앱니다.");
                document.body.style.backgroundColor='';
            }
        }

        function promptFunc(){
            var txt = prompt("좋아하는 과목을 선택해주세요 \n[1:python 2:html/css 3:javascript]" , "3") //3을 default로 지정
            if (txt==1){
                alert("python 재밌죠!!!")
            } else if (txt==2){
                alert("문서 구조화 하고 스타일 지정 재밌죠!!!")
            }else if (txt==3){
                alert("아직 몇개 안해봤는데 벌써 재밌죠!!!")
            }else if (txt==null){
                alert("하나라도 좋아해 주세요")
            }else {
                alert("1이나 2나 3만 입력해 주세요")
            }
        }
    </script>
</head>
<body>

    <h1>window 객체의 대화형 메서드</h1>

    <p>
        alert() : 경고 , 코드 디버깅용
        <button onclick="alertFunc();">확인</button>
    </p>
    <p>
        confirm() : 확인 / 취소 버튼 (true / false 리턴)
        <button onclick="confirmFunc();">확인</button>
    </p>
    <p>
        prompt() : 텍스트박스, 확인 / 취소 버튼 (텍스트 / null 리턴)
        <button onclick="promptFunc();">확인</button>
    </p>
    
</body>
</html>
```



## js-function

```html
 <script>
     	// 일반적인 함수 형태
        function func01(){
            alert("함수의 이름이 있습니다.");
        }
     	// 변수에 함수type을 저장
     	// 익명함수는 변수만 사용하면 해당하는 값의 형태만 가져온다.
     	// ()를 사용하여 실행해야 한다
     	// func02() ==> function(){alert("함수 이름이 없어요...")}와 동일
        var func02 = function(){
            alert("함수의 이름이 없어요...")
        }
        
		
        function func03(){
            /*
            function test(){
                alert("내부 함수")
            }
            test();
            */
           (function(){
               alert("즉시 실행 함수")
           })()
        }
		
     	//fun04을 호출하면 literalPrn을 호출한다.
     	// literalPrn을 호출하기 위해서는 내부의 lieral이라는 값(Parameter)이 필요하다.
     	// 변수 literal에 (function(msg){alert(msg);}) 라는 값을 전달한 것이고 익명함수와 동일하게 작동한다.
        function literalPrn(literal){
            literal("안녕하세요. 함수 형태의 값 입니다.")
        }
        function func04(){
            literalPrn(function(msg){alert(msg);});
        }
     
		// 내부함수에서 외부함수의 값, 기능을 가져와서 쓸 수 있는 것을 클로저라고 한다.
     	// 함수 형태의 값을 return하여 closureTest01에 넣어준다. 이후 closureTest()를 실행
        function closureFunc(val){
            var suffix = "님, 안녕하세요~"
            function innerFunc(){
                alert(val + suffix + "잘 부탁 드립니다.");
            }
            return innerFunc;
        }
        var closureTest01 = closureFunc("멀캠");

        function closureTest02(val){
            closureFunc(val)();

        }
    </script>
</head>
<body>

    <h1>function = 기능 </h1>
    <h2>함수의 종류</h2>
    <p onclick="func01();">명시적 함수</p>
    <p onclick="func02();">익명 함수</p>
    <p onclick="func03();">즉시 실행 함수</p>
    <p onclick="func04();">함수 리터럴</p>
    <p onclick="closureTest01();"> 클로저: 외부함수에 접근 가능 (변수 등)</p>
    <p onclick="closureTest02('멀티캠퍼스');">연습</p>

</body>
</html>
```



## js-control

```html
<script>
        function ifTest(){
            var i = prompt("숫자 1이나 2를 입력해 주세요")
            if (i==1){
                alert("1입니다.")
            } else if (i==2){
                alert("2입니다.")
            }else{
                alert("다른 숫자 입니다.")
            }
        }
		
    	//switch는 각각의 case로 구분
        function switchTest(){
            var season = prompt("봄 여름 가을 겨울 중 좋아하는 계절을 입력해 주세요");
            switch(season){
                case "봄" :
                    alert("봄에는 벚꽃엔딩");
                    break;
                case "여름":
                    alert("여름엔 바다");
                    break;
                case "가을":
                    alert("가을엔 단풍구경");
                    break;
                case "겨울":
                    alert("겨울엔 스키장");
                    break;
                dafault:
                    alert("봄 여름 가을 겨울 중 하나만 입력해 주세요");
            
            }
        }
		
    	//console창에서 실행되는 조건(개발자환경->console)
        function forTest(){
            // 초기값 ; 조건식 ; 증감식
            for (var i=0; i<10; i++){
                console.log(i);

            }
            //구구단 만들어보자! -> 검사하지 않는 숙제
            for (var i=2; i<10; i++){
                console.log(i+"단");

            for (var j=1 ; j<10 ; j++){
                console.log(i+"*"+j+"="+(i*j));
            }
            }
        }

        function whileTest(){
            var i=0;
            while (i<10){
                console.log(i);
                // i +=1;
                // i++;
                // console.log(i++);  <- 이렇게도 가능
                // console.log(++i); <- 1부터 10까지
                // 증감 연산자 (++ / --)
                // 변수++ : 변수의 값을 리턴한 뒤 , 연산
                // ++변수 : 연산을 먼저 하고, 변수의 값 리턴
            
                //구구단 만들기!! while문으로 거꾸로 출력 만들어보기

        }

        var j = 10;
        do {
            console.log(j);
            j--;
        } while(j>0);
    }

    </script>
</head>
<body>

    <button onclick = "ifTest();">IF</button>
    <br>
    <button onclick="switchTest();">SWITCH</button>
    <br>
    <button onclick="forTest();">FOR</button>
    <br>
    <button onclick="whileTest();">WHILE</button>
    
</body>
</html>
```



## js-dom

```html
<script type="text/javascript">
        function searchQS(){
            // var doc = document.querySelector("#test"); //여기서 css 선택자를 넣어줄것이다.
            // //querySelector("css 선택자")-> node 하나 리턴죔
            // console.log(doc);
            // var doc = document.querySelectorAll("#test"); 
            //querySelectorAll : 해당 test에 속하는 모든 nodelist를 가져옴 -> nodelist 리턴됨
            // console.log(doc)
            // test의 이름의 모든 query를 선택한후 0번째 선택
            var doc = document.querySelectorAll("#test")[0]
            // console.log(doc)
            doc.innerHTML = 'querySelectorAll(css선택자)' //p 태그 안에 있는 'DOM 탐색 메서드' 를 바꿀꺼다

        }

        function searchID(){
            var doc = document.getElementById("test");
            // console.log(doc)
            doc.innerHTML = 'id 속성으로 탐색';
            doc.style.color = 'red'
        }

        function searchName(){
            // nodelist로 리턴됨
            var doc = document.getElementsByName("test02")
            // console.log(doc)
            doc[1].value = "name으로 탐색!!"
        }

    	//p라는 이름의 Tag가 가진 모든 elements를 반환
    	// 3번째 innerHTML을 다음과 같이 변경
        function searchTag(){
            var doc = document.getElementsByTagName('p');
            doc[3].innerHTML = "tag 이름으로 탐색했음!!"
        }
    </script>
</head>
<body>

    <p onclick="searchQS();">DOM 탐색 메서드</p>

    <P id="test" onclick="searchID()">1. 엘리먼트의 id로 탐색 : 엘리먼트 하나를 선택(중복 불가) - 반환 : 값 하나 (Node)</P>

    <p onclick="searchName();">2. 엘리먼트의 name으로 탐색 : 엘리먼트를 여러 개 선택 - 반환 : 배열 (Nodelist) 
        <br>
        <input type="text" name="test02" value=""><br>
        <input type="text" name="test02" value=""><br>
        <input type="text" name="test02" value=""><br>
    </p>
    <p onclick="searchTag()">3. 엘리먼트의 태그 이름으로 탐색 : 엘리먼트를 여러 개 선택 - 반환 : 배열 (Nodelist)</p>

   
    
</body>
</html>
```



## js-object

```html
<script>
        function object01(){
            //this 는 객체를 만들었을때 해당 객체의 값을 외부에서 접근 가능하게 하는 변수 , self.변수 라고 생각하면 됨
            this.name01 = '홍길동';
            var name02 = 'hong-gd';
            this.getName02 = function(){
                return name02;
            }
        }

        // 객체 리터럴 : key를 통해서 가져옴 -> 자체로 객체를 생성
        // 객체를 만들때 가장 많이 사용하는 방법
        var object02 = {
            name : "kim-sd",
            prn : function(){
                alert(object02.name + "의 전화번호 : 010-1111-1111")
            }
        }

        function objTest(){
            // 객체 생성
            var obj01 = new object01(); //this로만 지정된 값을 가져옴 , 함수를 onject01 객체를 만듬
            // alert(obj01.name01);
            // alert(obj01.name02); //undefined로 표기됨 , var로 지정했기 때문
            // alert(obj01.getName02());
            // alert(object02.name);
            // object02.prn()
            obj01.prn();
        }
        // prototype은 객체에다가 기능을 추가하고 싶을 때 사용
        object01.prototype.prn = function(){
            alert(this.name01 + "의 전화번호는 010-2222-2222"); //뒤에 name02 붙여보셈
            
        }

    </script>
</head>
<body>
    <h1>object (객체) </h1>

    <pre>
        객체의 구성
        - property : 속성
        - function (method) : 기능
        - this : 객체 내부의 메서드나 속성을 정의
        - prototype : 객체의 확장
    </pre>

    <button onclick="objTest()">확인</button>
    
</body>
</html>
```



## js-string

```html
 <script>
        function strTest01(){
            var str01 = "String";
            var str02 = "Test"

            var str03 = str01 + str02;
            // alert(str03)

            var newString = str01.concat("Test" , "Java" , "Script")
            // alert(newString)

            //배열.join('문자') : 배열 사이사이에 문자가 삽입됨 (문자열로 반환)
            var JoinTest = ["5","10", "15", "20"].join("+")
            alert(JoinTest);
        }

        function strTest02(){
            var numVal = 12.5;
            var bool = true;
            //문자열과 다른 타입이 만나면 문자열로 합쳐짐
            var result = "String" + numVal + bool;
            // alert(result);
            // alert(typeof(result));

            var result2 = "a"+10+20
            alert(result2)
        }

        function strTest03(){
            var str = prompt("이름을 입력하세요")
            var span = document.getElementById("res") //id:res

            if (str=="멀캠"){
                span.textContent = str + "님 환영합니다"
            }else if (str.toLowerCase()=="multicampus"){ //전부 소문자로 변환해서 비교
                span.textContent = str+", Hello!"
            }else{
                span.textContent = '이름을 다시 한번 확인해 주세요'
            }

            //자동 형변환 => 숫자 10입니다 라고 표기됨
            var numVal = 10;
            if (numVal == "10"){
                alert("==연산자 사용 : 숫자 10 입니다.")
            } else{
                alert("==연산자 사용 : 숫자 10이 아닙니다.")
            }

            //자동으로 형 변환 되는게 싫어 !!
            // === 3개 사용 : 엄격하게 비교(형태까지 비교)
            if (numVal ==="10"){
                alert("===연산자 사용 : 숫자 10 입니다.")
            } else{
                alert("===연산자 사용 : 숫자 10이 아닙니다.")
            }

            // 문자열 객체를 생성
            var strObj = new String("멀캠");
            var strLiteral = "멀캠";

            // 처음꺼는 문자가 같다고 나옴
            if (strObj == strLiteral){
                alert("문자가 같습니다")
            }else{
                alert("문자가 다릅니다")
            }
            // 다르다고 표시됨 . 문자열과 문자열 객체이기 때문에 형태가 다르다
            if (strObj===strLiteral){
                alert("문자가 같습니다.===")
            }else{
                alert("문자다 다릅니다. ===")
            }
        }

        function strTest04(){
            var strVal = "홍길동 이순신 유재석 강호동 홍길동"
            var prop = prompt("검색할 이름을 입력해 주세요");
            //문자열을 가지고 잘라놨다고 생각하자
            // IndexOf는 왼쪽에서부터 찾을거다
            // lastIndexOf는 오른쪽에서부터 찾을거다
            // 둘이 같은 인덱스를 쓴다 -> 홍길동은 indexof는 첫번째 0 , lastindexof는 마지막 홍길동 16을 출력
            // 해당하지 않는 값을 입력하면 둘다 -1이 나옴
            alert("indexOf : " + strVal.indexOf(prop))
            alert("lastIndexOf : " +strVal.lastIndexOf(prop))
        }

        function strTest05(){
            var strVal = "문자열 추출하기. 관련 메소드:indexOf,substring";
            var startIndex = strVal.indexOf(":")
            var endIndex = strVal.lastIndexOf(",");
            //파이썬 슬라이싱하고 동일, :부터 ,전까지
            var res = strVal.substring(startIndex, endIndex);
            // alert(res);

            //공백 기준으로 자름
            var splitVal = strVal.split(" ")
            alert(splitVal[1]);
        }

        function strTest06(){
            var prop = prompt("쉼표로 구분하여 키워드를 입력해주세요", "사과, 바나나, 키위, 수박")
            var propArr = prop.split(",");
            
            var propResult="";
            for (var i = 0; i<propArr.length; i++){
                propResult += propArr[i] + "<br/>"
            }
            document.getElementById("key").innerHTML = propResult;

        }
    </script>
</head>
<body>

    <p>문자열합치기
        <button onclick="strTest01();">클릭</button>
    </p>

    <p>
        다른 자료형 합치기
        <button onclick="strTest02();">클릭</button>
    </p>

    <p>
        문자열 비교하기
        <button onclick="strTest03();">클릭</button>
        <span id="res"></span>
    </p>

    <p>
        문자열 검색하기
        <button onclick="strTest04();">클릭</button>
    </p>

    <p>
        문자열 추출하기
        <button onclick="strTest05();">클릭</button>
    </p>

    <p>
        키워드 나누기
        <button onclick="strTest06();">클릭</button>
    </p>
    <div id="key"></div>
</body>
</html>
```



## js-number

```html
<script type="text/javascript">
        function numberObj(){
            // 값 자체로 되어 있는 것을 literal이라고 한다
            var num01 = 3;
            // alert(num01 + ":" + typeof(num01));

            //object
            var num02 = new Number(3);
            // alert(num02 + ":" + typeof(num02));

            //문자형을 숫자형으로 바꿈
            // alert(parseInt("1")+1);

            //Not a Number 뜸 -> NaN으로 표기
            // alert(parseInt("a")+1)

            var prop = prompt("숫자만 입력해 주세요");
            if (isNaN(prop)){
                alert("숫자가 아닙니다.");
            } else{
                alert("숫자가 맞습니다.")
            }


        }

        function randomNum(){
            //Math.random() : 0<=x<1
            //Math.floor() : 내림
            //Math.round() : 반올림
            //Math.ceil() : 올림

            // 0~100
            var hundred = Math.floor(Math.random()*101);

            // 10~100
            var min = 10;
            var max = 100;
            var ran = Math.floor(Math.random()*(max-min)+min);
            // alert(ran)
            //로또 숫자 1~45 만들기 (1<=x<46)
            var lotto = Math.floor(Math.random()*45+1)
          alert(lotto) //확인 필요
        }
        
        function randomBG(){
            //style 색상 표현색 : rgb(256,256,256)
            var rum = function(){
                return Math.floor(Math.random()*256);
                
            }
            document.body.style.backgroundColor = "rgb("+rum()+","+rum()+","+rum()+")";
        }
    </script>
</head>
<body>

    <h1>숫자</h1>

    <button onclick="numberObj();">숫자</button>
    <br>
    <button onclick="randomNum()">난수</button>
    <br>
    <button onclick="randomBG()">배경색 변환</button>
    <br>
    <button onclick="randomCircle()">랜덤 원 그리기</button>
    <button onclick="circleArea()">원의 넓이 / 둘레</button>
    <br>
    원의 넓이 : <span id="area"></span>
    <br>
    원의 둘레 : <span id="len"></span>
    <br>
    <br>
    <br>
    <br>
    <br>
    <style>
        #circle{
            border: 1px solid red;
            display : none;
        }
    </style>
    <div id="circle"></div>
    <script>
        function randomCircle(){
            var rnum = Math.floor(Math.random() * 200)
            var circle = document.getElementById("circle");

            circle.style.width = rnum + "px";
            circle.style.height = rnum + "px";

            circle.style.borderRadius = Math.floor(rnum/2) + "px";
            circle.style.display = "block";
        }

        function circleArea(){
            // Math.PI
            // 원의 넓이 : pi r r
            var circleWidth = document.getElementById("circle").style.width;
            // alert(circleWidth)
            var r2 = circleWidth.substring(0,circleWidth.length-2)
            // alert(r2)
            var r = Math.floor(r2/2);
            // alert(parseInt(circleWidth))  <- 이렇게 하면 한번에 숫자만 나옴
            // var doc1 = document.getElementById('area')
            // doc1.innerHTML = Math.PI*r*r

            // var doc2 = document.getElementById('len')
            // doc2.innerHTML = Math.PI*r2
            document.getElementById("area").innerHTML = Math.floor(Math.PI * Math.pow(r,2))
            document.getElementById("len").innerHTML = Math.floor(Math.PI * r2)
            

            // 원의 둘레 : 2 pi r
            Math.PI*r*r
            
        }
    </script>
    
</body>
</html>
```



## js-datetime

```html
 <script type="text/javascript">
        //onload : 화면이 다 완성됐다고 표시된 이후
        onload = function(){
            //원하는 시점에 call 하면 back 해주면 좋겠어 : call-back 함수
            document.getElementsByTagName("button")[0].onclick = testDate01;
            document.getElementsByTagName("button")[1].onclick = testDate02;
            document.getElementsByTagName("button")[2].onclick = testDate03;
            document.getElementsByTagName("button")[3].onclick = testDate04;
            document.getElementsByTagName('button')[4].onclick = testDate05;
            // onload 함수 안에 없으면 cannot set properties
            // 버튼이 만들어지기 전이기 때문에 그렇게 오류가 나온다
            // 따라서 button 만든거 이후에 그냥 document~~~이것만 써도 실행 가능하다.
            // onload 라는 뜻은 결국 문서가 다 만들어진 이후!! 라는 뜻으로 함수 안에서 사용해야 한다.
            
        }
        function testDate01(){
            var inputDate = document.getElementById("today");
            // Date 객체 생성
            var date = new Date();

            inputDate.innerHTML = date.toDateString()+"<br/>"
            inputDate.innerHTML += date.toLocaleDateString() + "<br/>";
            inputDate.innerHTML += date.toLocaleString() + "<br/>";
            inputDate.innerHTML += date.toLocaleTimeString()+"<br/>"
        }
        function testDate02(){
            var date = new Date();
            var year = date.getUTCFullYear();
            var month = date.getMonth()+1;
            var day = date.getDate();
            var week = date.getDay();
            var dayOfWeek = ['일', '월', '화' , '수' , '목' , '금', '토'];

            document.getElementById("today").innerHTML = year + "/" + month + "/" + day + "/" + dayOfWeek[week];   
            // date.prn(); 
        }

        //date.prn()으로
        //prototype으로 기능 추가 가능
        // Date.prototype.prn = function(){
        //     alert("데이트 객체 공부하고 있습니다.")
        // }


        function testDate03(){
            var year = 2022;
            var month = 5;
            var day = 13;

            var date = new Date(year, month-1, day);
            document.getElementById("specific").innerHTML = "수료 일시 : " + date
        }

        function testDate04(){
            var dates = document.getElementById("dates").value;
            var inputDate = document.getElementById("inputdate").value;

            var date = new Date(dates);
            date.setDate(date.getDate() + parseInt(inputDate));
            document.getElementById("result").value = date.toLocaleDateString();
        }

        function testDate05(){
            var dates02 = document.getElementById("dates02").value;
            var inputDate02 = document.getElementById("inputdate02").value;

            var nowDate = new Date(dates02)
            var afterDate = new Date(inputDate02)

            // getTime() : milliseconds 형태로 바꿔서 나옴

            var resultVal = (afterDate.getTime() - nowDate.getTime())/(1000*60*60*24)

            document.getElementById("result02").value = resultVal
        }
    </script>
</head>
<body>

    <h2>오늘 날짜 출력하기</h2>
    <span id="today"></span>
    <br>
    <button>오늘날짜</button>
    <button>오늘날짜(표현)</button>

    <h2>특정 날짜 출력하기</h2>
    <span id="specific"></span>
    <br>
    <button>특정날짜</button>

    <h2>경과 날짜 출력하기</h2>
    <label>지정 날짜</label>
    <input type="date" id="dates" size ="50">
    <br>
    <label>경과일</label>
    <input type="number" id="inputdate">
    <br>
    <label>경과 후 날짜</label>
    <input type="text" id="result" readonly="readonly">
    <button>경과날짜</button>

    <h2>D-Day</h2>
    <label>시작 날짜</label>
    <input type="date" id="dates02" size="50">
    <br>
    <label>종료 날짜</label>
    <input type="date" id="inputdate02">
    <br>
    <label>남은 일수</label>
    <input type="text" id="result02" readonly="readonly">
    <button>남은 일 수 구하기</button>
    
</body>
</html>
```



