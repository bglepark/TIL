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



## js-array

```html
<script>
        //객체 생성 1, 2
        // 배열 : 여러 개의 값을 효과적으로 관리하기 위한 객체
        var arrayObj = new Array();
        var arrayLiteral = ['v1','v2',3,4];

        var arrayObj02 = new Array(5); //바로 숫자 5를 넣어서 만들면? -> ,,,, 로 출력됨 -> 배열의 5칸 빈 공간을 만듬 -> 4개의 콤마로 나옴
        
        var arrayObj03 = new Array(1,2,3,4,5) //1,2,3,4,5로 표기됨

        onload = function(){
            // alert(arrayObj);
            // alert(typeof(arrayObj)) //object type으로 출력됨
            // alert(arrayObj02)
            // alert(arrayObj03)
            // alert(arrayObj03[1]); //숫자 1개만 출력, 1번지 숫자를 출력
            // alert(arrayObj02[3]); // 빈칸 중 해당 위치의 빈칸 가져오기 -> undefined -> 값이 정의되지 않았다.(null과 undefined는 다르다)

        }

        function multiArr(){
            var len = 3;
            var arr = new Array(len);

            for (var i = 0; i<arr.length; i++){
                arr[i] = new Array(len) //3칸짜리 빈 배열에다가 배열 안에 각각의 칸에 3칸짜리 배열을 만듬
            }

            arr[0][0] = "수박";
            arr[0][1] = "딸기";
            arr[0][2] = "키위";

            arr[1][0] = 1;
            arr[1][1] = 2;
            arr[1][2] = 3;

            arr[2][0]=['lol' , 'wow'];
            arr[2][1]=['python','numpy','pandas'];
            arr[2][2]=['javascript', ['function']];

            arr[1][2] = 9 //숫자 9로 바꾸기

            // alert(arr)

            // function -> jquery로 바꾸는 방법
            arr[2][2][1][0] = 'jquery';
            alert(arr.toString()); //굳이 이거 안써도 호출을 해주는구나!!

        }

        function joinTest(){
            var nums = ['1' , '2' , 3 , 4 , '5'];
            var res = nums.join('+');
            // alert(res)
            alert(eval(res)); //연산을 수행한 결과가 출력됨
        }

        function sortTest01(){
            var arr = ['a' , 'd' , 'b', 'c'];
            alert(arr);
            arr.sort();
            alert(arr); //문자가 정렬됨
            
        }

        function sortTest02(){
            var arr = [1 , 2 , 6 , 11 , 3 , 65 , 21];
            alert(arr)
            arr.sort(); //숫자로 정렬은 ascii code순으로 정렬됨
            alert(arr)
        }

        function compareNum(a , b){
            return a-b;
            /* 뺀 값이 다음과 같으면 어떻게 되냐(숙제!!)
            b-a면 내림차순이 된다.
            1: 양수면 누가 더 크냐
            0: a==b
            -1: 음수면 누가 더 크냐

            */
        }

        function reverseTest(){
            var arr = [10,2,3,6,22,100];
            arr.sort(function(a,b){return a-b})
            arr.reverse()
            alert(arr) // 그냥 reverse 하면 쓴 순서대로 역순
        }

        function pushAndShift(){
            var queue = new Array();
            queue.push("first");
            queue.push("second");
            queue.push("third")

            alert(queue);

            var a = queue.shift(); //shift 찾아보자
            alert(a);
            alert(queue) //shift는 앞에서부터 잘라옴

            queue.push('4th');
            alert(queue);

            var b = queue.pop();
            alert(b)
            alert(queue)
        }

        function sliceTest(){
            var arr01 = new Array(1,2,3,4,5,6,7)
            var slice01 = arr01.slice(1,3); //1부터 3 전까지
            // alert(slice01)

            var arr02 = new Array(4);
            arr02[0] = new Array(1,2);
            arr02[1] = new Array(3,4);
            arr02[2] = new Array(5,6);
            arr02[3] = new Array(7,8);

            var slice02 = arr02.slice(1,3); //3,4,5,6 이 나옴
            // alert(slice02)

            slice02[0][0] =33; //3을 33으로 바꿈 
            // 얕은 복사 해서 값이 같음

            alert(arr02)
        }

    </script>
</head>
<body>

    <h1>배열 (객체) </h1>
    <ul>
        <li onclick="multiArr()">다중 배열</li>

        <li onclick='joinTest()'>join 함수</li>

        <li>배열 정렬
            <ul>
                <li onclick="sortTest01()">sort() : 문자 정렬</li>
                <li onclick="sortTest02()">sort() : 숫자 정렬</li>
                <li onclick="reverseTest()">reverse() : 거꾸로 정렬</li>
            </ul>
        </li>

        <li onclick="pushAndShift()">배열 Queue
            <ul>
                <li>push()</li>
                <li>shift()</li>
                <li>pop()</li>
            </ul>
        </li>

        <li onclick="sliceTest()">slice() : 배열의 부분을 가지고 새로운 배열 생성</li>
    </ul>
    
</body>
</html>
```



## js-popup

```html
 <script type = "text/javascript">

        function popUpTest(){
            //open(경로, 이름, 옵션)
            window.open("js12-popup-res.html" , "", "width=300px , height=300px" );
        }
    </script>
</head>
<body>

    <button onclick="popUpTest()">팝업창</button>
    
</body>
</html>



//js12-popup-res.html
</head>
<body>
    
    화이팅!
    
</body>
</html>
```



## js-window

- js-window.html

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Document</title>
  
      <style type="text/css">
          #regist {
  			/* (absolute는 부모의 위치 기준으로, 얼마나 움직이는지) */
              border: 1px solid black;
              background: pink;
              position: absolute;
              top: 200px;
              left: 500px;
              display: none;
          }
      </style>
      
      <!-- 
          display : none;			//공간을 차지하지 않는다 (만들어지지 않은 상태)
          visibility: hidden;		//공간을 차지하고, 보이지 않는다 (만들어져 있는 상태)
       -->
      
      <script type="text/javascript">
          function openWin() {
              var url = "js13-window-popup.html";
              var title = "myframe";
              var prop = "top=200px,left=600px,width=500px,height=500px";
  			//open(경로, 이름, 옵션)
              window.open(url, title, prop);
  			// 경로만 줘도 새로운 탭에서 열린다
  			// window(url , prop) -> 새로운 창에서 열린다
  			// 여기서 말하는 이름(title)은 url에 있는 문서가 열릴 곳
  			// 여기서 iframe이 지정되어 있으니까 현재 페이지에서 문서가 열림 -> 최근엔 아예 사용을 안함
          }
      
          function registForm() {
  			//기존에 display none으로 되어 있던걸 block으로 바꿔 화면에 보이게함
              document.getElementById("regist").style.display = "block";
  			// 바디 색을 회색으로
              document.body.style.background = "gray";
  			// 창열기 , 회원가입 버튼의 name : btn
              var btns = document.getElementsByName("btn");
              for ( var i in btns) {
  				// 여기에 있는 for 반복문은 향상된 for each 문이라고 한다.
  				// in 기준으로 오른쪽은 덩어리 -> 이름이 btn인 노드들이 모여있는 리스트(btns) -> 노드를 가져옴
  				// 기존 for (var i = 0 ; i<btns.length; i++)은 index만 가져옴
  				// 창열기, 회원 가입 버튼을 disabled 해서 작동하지 않게 함
  				console.log(i);
                  // btns[i].disabled = "disabled";
              }
          }
      
          function closeWin() {
  			//display창을 다시 none으로 해서 화면에서 안보이게 함
              document.getElementById("regist").style.display = "none";
  			// 바디 색을 흰색으로
              document.body.style.background = "white";
  			// 창열기 , 회원가입 버튼을 받아서 disabled를 무효화 시켜줌
              var btns = document.getElementsByName("btn");
              for ( var i in btns) {
                  btns[i].disabled = "";
              }
          }
      
          function idchk() {
              alert("중복체크를 확인하세요");
          }
      
          function idCheck() {
              open("js13-window-id-check.html", "", "width=300px,height=300px");
          }
      </script>
      
      
  </head>
  <body>
      
      <h1>window객체</h1>
  	<!-- pre => 입력한 그대로 보여주는 속성 -->
  	<pre>
  	프로퍼티
  	 -document
  	 -history
  	 -location
  	 -navigator
  	 -screen
  	 -frames
  	 -parent
  	 -top
  	 -self
  	메서드
  	 -alert()
  	 -confirm()
  	 -prompt()
  	 -back()
  	 -forward()
  	 -setInterval()
  	 -clearInterval()
  	 -setTimeout()
  	 -open()
  	 -close()
  	 -scroll(),scrollBy(), scrollTo() 
  	</pre>
  
      <!-- 두번째 h1 -> 팝업에서 내용을 바꿈 -->
  	<div id="f1">
  		<h1>팝업창 만들기</h1>
  		<button onclick="openWin()" name="btn">창열기</button>
  		<hr>
  		<h1>회원가입하기(div팝업창)</h1>
  		<button onclick="registForm()" name="btn">회원가입</button>
  	</div>
  
      <!-- 회원가입폼 시작 -->
  	<div id="regist">
  		<form>
  			<table>
  				<caption>회원가입</caption>
  				<tr>
  					<td>아이디</td>
  					<!-- readonly : 읽기 전용 , id를 누르면 중복체크 하라고 alert -->
  					<td><input type="text" name="id" onclick="idchk()" readonly="readonly" /> 
  
  					<input type="button" value="중복체크" onclick="idCheck()" /></td>
  				</tr>
  				<tr>
  					<td>패스워드</td>
  					<!-- checked : 명시해야 True로 표기됨 -->
  					<td><input type="password" name="pwd" alt="" style="color: red;" checked="checked" /></td>
  					<!-- alt와 checked="checked"는 함정이다 라디오와 체크박스에서만 사용됨  -->
  				</tr>
  				<tr>
  					<td colspan="2" align="center"><input type="button" value="확인" onclick="closeWin()" /></td>
  				</tr>
  			</table>
  		</form>
  	</div>
  	<!-- 회원가입폼 종료 -->
  
  	<br/><br/><br/>
  	<!-- iframe 요소를 이용하면 해당 웹 페이지 안에 어떠한 제한 없이 또 다른 하나의 웹 페이지를 삽입할 수 있습니다.
  	이걸 사용했기 때문에 팝업창 화면이 해당 페이지 내에서 표기되는 것이고, 따라서 닫기 기능이 안된다.-->
  	<iframe name="myframe"></iframe>
  
  
  </body>
  </html>
  ```

  

- js-window-id-check

  ```html
  <script type="text/javascript">
          //중복확인을 위해 미리 변수를 설정
          var ids=["multi","java","script"];
          
          function confirmChk(){
              var id=document.getElementsByName("id")[0].value;
              var div=document.getElementsByTagName("div")[0];
              // 인덱스가 -1이면 존재하지 않다는 뜻 -> 즉 != -1이므로 아이디가 존재
              if(ids.indexOf(id)!=-1){
                  // 배열 객체에서도 인덱스를 사용할 수 있고, 값이 없으면 -1을 리턴한다
                  div.innerHTML="<b>아이디가 존재합니다.</b>";
              }else{
                  // 사용 가능한 아이디면 확인 버튼 생성하고 클릭 시 , insertID 함수 실행
                  var userId="사용할 수 있는 아이디입니다."
                          +"<input type='button' value='확인'"
                          +"onclick='insertId(\""+id+"\")'>";
                          // div[0]인 아이디 칸에 입력한 id를 삽입
                          // 부호 무효화 -> escape character(escape sequence)
                          // 문자열은 sequence 하다 (문자 하나하나가 모여서 만들어진것이기 때문에)
                          // 저거 없이 확인을 누르면 error 발생 -> 변수명으로 취급한다
                  div.innerHTML=userId;          
              }
          }
          
          function insertId(id){
              //팝업을 오픈한 윈도우 객체 화면에서 'id'라는 name 중 0번째 값을 input한 id로 바꿈
              opener.document.getElementsByName("id")[0].value=id;
              // input태그를 마우스로 클릭하여 입력상태로 만든것을 포커스를 얻었다고 한다.
              opener.document.getElementsByName("pwd")[0].focus();
              close();
          }
      </script>
  
  </head>
  <body>
      
  	<table>
  		<tr>
  			<td>아이디</td>
  			<td><input type="text" name="id"/></td>
  		</tr>
  		<tr>
              <!-- 행 합치기 -->
  			<td colspan="2"> 
  				<input type="button" value="중복확인" onclick="confirmChk()"/>
  				<input type="button" value="취소" onclick="self.close()"/>
  			</td>
  		</tr>
  	</table>
  	<div></div>
  
  </body>
  </html>
  ```



- js-window-popup

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Document</title>
  
      <script type="text/javascript">
          function test(){
              // name이 test인 text값의 0번지 주소값을 받아서 val에 저장
              var val=document.getElementsByName("test")[0].value;
              // opener : 자기자신을 연 기존 창의 window 객체를 참조
              // 즉, 이 popup창을 만든 window페이지에서 2번째 h1 태그를 찾아 문서 내용을 바꿈
              // 2번째 h1 태그는 팝업창 만들기 -> val 로 내용을 바꿈
              opener.document.getElementsByTagName("h1")[1].innerHTML=val;
              close();
          }
      </script>
      
  </head>
  <body>
      
  	<input type="text" name="test"/>
  	<input type="button" onclick="test()" value="전달"/>
  	<input type="button" onclick="self.close()" value="창닫기">
      <!-- self가 들어갔기 때문에 window 객체를 반환해서 close한다 -->
      <!--  팝업이 아니라 프레임에서 열린거라서 닫히지 않는다 -->
  
  
  </body>
  </html>
  ```





## js-location

```html
<script>
        function locTest(){
            // location.href="http://www.naver.com"
            // location.assign("http://127.0.0.1:5500/web03-js/index.html")
            // location.assign("http://www.google.com")
            // location.replace("http://lc.multicampus.com/k-digital") //사이트 갔다가 뒤로 가기 하면 index로 감
            // href나 assign은 해당 경로로 가라! 라는 뜻
            // replace는 해당 경로로 가라 라는 뜻이 아니라 현재 페이지를 해당 경로로 바꿔라! 라는 뜻이다
            location.reload(); //페이지 새로고침

        }
    </script>
</head>
<body>

    <button onclick="locTest()">경로 연습</button>
    
</body>
</html>
```



## js-check (체크박스)

```html
<style>
        #colorbox{
            width:320px;
            height:320px;
            position:relative;
        }
        #red, #green, #blue, #magenta{
            width:150px;
            height:150px;
            border: 1px solid black;
            position: absolute;
        }
        #green{
            left:160px;
        }
        #blue{
            top:160px
        }
        #magenta{
            left:160px;
            top:160px;
        }
    </style>

    <script>
        function selectColor(){
            var chks = document.getElementsByName("chk"); //nodelist가 들어가 있음. chk의 checkbox 4개 들어있음

            for (var i = 0; i<chks.length; i++){
                // console.log(chks[i].checked)
                if (chks[i].checked){ //()괄호가 붙어 있으면 메소드 , 이건 그냥 변수이다
                    document.getElementById(chks[i].value).style.backgroundColor=chks[i].value
                }
                else{
                    document.getElementById(chks[i].value).style.backgroundColor=""
                }
                }
            }

            function allCehck(bool){
                var chks = document.getElementsByName("chk");

                for (var i=0; i<chks.length; i++){
                    chks[i].checked = bool; //checked된 속성 true/false를 bool에 각각 넣어 줄 것이다.
                }
            }
            //하나를 체크 풀면 전체 선택도 풀리는 상태 만들기

            //취소 누르면 싹 다 지우기
            function clearDiv(){
                allCehck(false);

                var colorbox = document.querySelectorAll("#colorbox > div") //colorbox가 가지고 있는 자식요소 div를 찾아라
                for (var i=0; i<colorbox.length; i++){
                    colorbox[i].style.backgroundColor=""
                }
            }

        
    </script>
</head>
<body>

    <div id="colorbox">
        <div id="red">red</div>
        <div id="green">green</div>
        <div id="blue">blue</div>
        <div id="magenta">magenta</div>

    </div>
    
    <div id="base">
        <form>
        
            <input type="checkbox" name="all" onclick="allCehck(this.checked)"> 전체 선택 <br> 
            

            <input type="checkbox" name="chk" value="red"> 빨강 <br>
            <input type="checkbox" name="chk" value="green"> 초록 <br>
            <input type="checkbox" name="chk" value="blue"> 파랑 <br>
            <input type="checkbox" name="chk" value="magenta"> 진홍 <br>

            <input type="button" value="선택" onclick="selectColor()">
            <input type="button" value="취소" onclick="clearDiv()">

        </form>
    </div>
    
</body>
</html>
```





## js-dom01 (롤링갤러리)

```html
 <style>
        a>img{width:50px ; height: 50px;}
        #gallery{width: 200px; height: 200px;}
        p{width: 350px; height: 250px;}
        img{vertical-align: middle;}
        a{text-decoration: none;}
    </style>

    <script>
        var num=1

        function prevGallery(){
            num--; //num=num-1
            //전역 변수를 받아서 숫자를 감소시키면서 이미지가 변하게 만들고 있다.
            if(num<1){
                num=6;
                
            }
            document.getElementById("gallery").src = "resources/imgs/img0"+num+".png";

            //return을 사용한 이벤트 전파 막기 (jquery때 공부!)
            // a tag의 기본속성은 naver로 이동해라 -> 클릭 이벤트가 발생한 이후에 기본동작(네이버)가 작동하지 않는다.
            return false;
        }

        function nextGallery(){
            num++;
            if(num>6){
                num = 1;
            }

            document.getElementById("gallery").src = "resources/imgs/img0"+num+".png"

            return false;
        }
    </script>

</head>
<body>

    <div id="gallerywrap">
        <p>
            <a href="#pre" onclick="prevGallery()">
                <img src="resources/imgs/arrowleft.png" alt="왼쪽화살표">
            </a>

            <img id="gallery" src="resources/imgs/img01.png" alt="gallery">

            <a href="#next" onclick="nextGallery()">
                <img src="resources/imgs/arrowright.png" alt="오른쪽화살표">
            </a>
        </p>
    </div>


    
</body>
</html>
```



## js-dom02 (부모자식)

```html
 <script>
        function searchPar(){
            var child02 = document.getElementsByTagName("p")[1];
            var div = child02.parentNode;
            alert(div);
            alert(typeof(div));
            alert(div.nodeName);
            div.style.backgroundColor = "violet"
            
        }

        function searchChi(){
            // var div = document.getElementsByTagName("div") //div가 들어 있는 값이 1개인 노드리스트를 반환
            var div = document.getElementsByTagName("div")[0];

            //자식요소들 가져오기
            var divChildren = div.childNodes; //childNodes는 div 태그 안에 있는 모든 걸 가져온다
            //[공백, child01 , 공백 , child02, 공백 , child03, 공백] -> 공백은 tag가 아니라서 undefined라고 뜸
            // alert(divChildren.length) -> 7이 나온다
            // divChildren[3].style.backgroundColor= "blue"

            for (var i=0 ; i<divChildren.length; i++){
                // console.log(divChildren[i].tagName);
                console.log(divChildren[i].nodeName);
            }
        }
    </script>
</head>
<body>

    <h1>부모탐색 , 자식탐색</h1>

    <div>
        <p>child01</p>
        <p>child02</p>
        <p>child03</p>
    </div>

    <button onclick="searchPar()">부모탐색</button>
    <br>
    <button onclick="searchChi()">자식탐색</button>
    
</body>
</html>
```



## js-dom03 (엘리먼트 생성)

```html
  <script>
        function elementCreate(){
            var div = document.createElement("div"); //<div></div> 라는 태그를 만든다

            // 속성 지정해주기(attribute 생성)
            // 방법 1. 
            // var attr = document.createAttribute("Style");  //style 속성을 만들것이다. style=""
            // attr.nodeValue = "border:2px solid blue"       //style = " border : 2px solid blue"
            // div.setAttributeNode(attr);              //<div style="borderL2px solid blue"></div> 라는 뜻

            //방법 2
            div.setAttribute("style" , "border:2px solid red;") //한번에 가능

            //textnode 생성
            var txt = document.createTextNode("엘리먼트 생성!!")   //엘리먼트 생성
            div.appendChild(txt);  //<div style="borderL2px solid blue">엘리먼트 생성</div>

            document.body.appendChild(div); // 위치 : body 밑으로 들어간다. button 엘리먼트 생성하기 옆에 생성됨(body 파트)

            
        }
    </script>
</head>
<body>

    <button onclick="elementCreate();">엘리먼트 생성하기</button>
    <!-- 
        엘리먼트 객체 생성 : createElement("tagname");
        txt 객체 생성 : createTextNode("txt");
        객체의 속성 :
        - createAttribute("attributename");
          setAttributeNode(attribute 객체);

        - setAttribute("attributename" , "attributevalue");
     -->
    
</body>
</html>
```



## js-dom04 (엘리먼트 생성 연습)

```html
 <script>
        function createImg(){
            // 1. 이름이 rdobtn인 요소들을 가지고 온다.
            var radios = document.getElementsByName("rdobtn");

            // 2. 가지고 온 요소들의 length만큼 반복하여 라디오 버튼이 체크되어 있는지 확인하고,
            //      만일 체크되었다면 자신의 이미지를 가지고 온다.
            //      hint) radioVal = "resources/imgs/img0"+...

            var radioVal ="";
            for (var i=0; i<radios.length; i++){
                if (radios[i].checked){
                    radioVal = "resources/imgs/" + radios[i].value

                }
            }

            // 3. img태그를 생성하고 , src 속성에 위의 값(radioVal)을 저장하여 
            //      화면에 그림이 나오도록 하자
            
            var img = document.createElement("img");
            img.setAttribute("src" , radioVal)
            


            var div = document.getElementById("imgview");
            var chd = document.querySelector("#imgview > img");
            div.replaceChild(img, chd);

        }

        function deleteImg(){
            document.getElementById("imgview").innerHTML = "<img src=''/>";
            // document.querySelector("#imgview>img").src="";

        }

    </script>
</head>
<body>

    <input type="radio" name="rdobtn" value="img01.png">img01 <br>
    <input type="radio" name="rdobtn" value="img02.png">img02 <br>
    <input type="radio" name="rdobtn" value="img03.png">img03 <br>

    <button onclick="createImg();">이미지 생성</button>
    <button onclick="deleteImg()">이미지 삭제</button>

    <div id="imgview"><img src="" ></div>
    
</body>
</html>
```



## js-dom05 (롤링갤러리2)

```html
 <style>
        img{
            vertical-align: middle;
            width: 300px;
            height: 300px;
        }
        a{
            font-size: 30px;
            text-decoration: none;
        }
    </style>

    <script>
        window.onload=function(){
            var anchs = document.querySelectorAll("a");
            var img = document.querySelector("img");

            var count=1;

            //왼쪽 화살표
            anchs[0].onclick = function(){
                var imgAlt = img.getAttribute("alt");
                if (imgAlt=="img01"){
                    count = 6;
                    img.setAttribute("alt" , "img06");
                    img.setAttribute("src" , "resources/imgs/img06.png");
                }
                else{
                    img.setAttribute("alt" , 'img0'+(--count)); //전위 연산자는 먼저 연산하고 값 return
                    img.setAttribute("src" , "resources/imgs/img0" + count + ".png");
                }

            }

            //오른쪽 화살표
            anchs[1].onclick = function(){
                var imgAlt = img.getAttribute("alt"); //해당 속성을 가지고 와라
                if (imgAlt == "img06"){
                    count = 0;
                    img.setAttribute("alt" , "img01") //alt속성을 img01로 넣는다
                    img.setAttribute("src" , "resources/imgs/img01.png");
                }
                else{
                    img.setAttribute("alt" , 'img0'+(++count)); //전위 연산자는 먼저 연산하고 값 return
                    img.setAttribute("src" , "resources/imgs/img0" + count + ".png");
                }

            }
        }
    </script>
</head>
<body>

    <div>
        <a href="#" id="lt">◀</a>
        <img src="resources/imgs/img01.png" alt="img01">
        <a href="#" id="gt">▶</a>
        <!-- href에 #이 없으면 안된다. 여기에 아무 값도 없으면 현재 페이지를 새로고침해서 다시 받는다 -->
    </div>
    
</body>
</html>
```



## js-dom06(자식들)

```html
<style>
        p{
            border:1px solid red;
        }
    </style>

    <script>
        function addAppend(){
            var fieldset = document.getElementById("addele");
            var p = document.createElement("p")

            p.textContent = "자식 태그들 중 가장 마지막에 넣어진다."

            fieldset.appendChild(p);
            
        }

        var count = 1
        function addInsert(){ //확인 필요!!!!!!!!!!!!
            var newP = document.createElement("p");
            var fieldset = document.getElementById("addele");

            newP.textContent = "엘리먼트의 앞에 넣어진다 " + (count++);

            var oldDiv = document.querySelector("fieldset > div");
            fieldset.insertBefore(newP , oldDiv);
        }

        function moveElement(){
            var moveEle = document.querySelector("fieldset").children[1];

            var addEle = document.body;
            addEle.appendChild(moveEle);

            /*
                검사하지 않는 숙제!
                childNodes와 children의 차이점?
            */
        }
    </script>
</head>
<body>

    <h1>태그 추가하기</h1>

    <button onclick="addAppend();">appendChild()</button>
    <button onclick="addInsert();">insertBefore()</button>
    <button onclick="moveElement()">element 이동</button>

    <fieldset id="addele">
        <legend>부모태그</legend>
        <div>div</div>
    </fieldset>
    
</body>
</html>
```



## js-dom07 (연락처)

```html
 <script>
        function tableVal(){
            //form 요소를 모두 반환
            var doc = document.forms[0];
            //문자열이 저장된 배열로 가져옴
            var vals = [doc.id.value , doc.pw.value , doc.addr.value , doc.phone.value]

            //유효성 검사 -> 유효한 값을 넣지 않으면 창 뜨는것과 비슷
            for (var i=0; i<vals.length; i++){
                if(vals[i]==null || vals[i]==""||vals[i]==undefined){
                    alert("제대로 입력했는지 다시 한번 확인해주세요")
                    return;
                }
            }
            // 값을 넣기 위해 row를 만듬
            document.getElementById("addtr").appendChild(createRow(vals));
        }

        function createRow(vals){
            var tr = document.createElement("tr"); //

            for (var i=0; i<vals.length; i++){
                // <td>id</td>
                var td = document.createElement("td");
                td.textContent = vals[i];
                //해당 td에 값 넣음 -> 4번 반복
                tr.appendChild(td);
            }

            //input 안에 삭제 버튼을 만들고 delRow하는 함수 -> this는 input tag를 가리킨다
            var deleteTd = document.createElement("td");
            deleteTd.innerHTML = "<input type='button' value = '삭제' onclick = 'delRow(this)'>";
            tr.appendChild(deleteTd);

            /*
                <tr>
                    <td>id값</td>
                    <td>pw값</td>
                    <td>addr값</td>
                    <td>phone값</td>
                    <td><input type="button" value="삭제" onclick="delRow(this)></td>
            */

            return tr
        }

        function delRow(ele){
            /*
                <tr>
                    <td>id값</td>
                    <td>pw값</td>
                    <td>addr값</td>
                    <td>phone값</td>
                    <td><input type="button" value="삭제" onclick="delRow(this)></td>
            */

            var delTr = ele.parentNode.parentNode;
            var tbody = document.getElementById("addtr");
            tbody.removeChild(delTr);

        }

        function deleteAll(){
            var tbody = document.getElementById("addtr");

            //tbody에 childnode가 하나라도 있으면 true , 없을경우 false
            while(tbody.hasChildNodes()){
                //마지막애부터 쭉 삭제
                tbody.removeChild(tbody.lastChild);

            }
        }
    </script>
</head>
<body>

    <form>
        <table id="intable">
            <tr>
                <td>아이디</td>
                <td><input type="text" name="id"></td>
            </tr>
            <tr>
                <td>비밀번호</td>
                <td><input type="text" name="pw"></td>
            </tr>
            <tr>
                <td>주소</td>
                <td><input type="text" name="addr"></td>
            </tr>
            <tr>
                <td>전화번호</td>
                <td><input type="text" name="phone"></td>
            </tr>

        </table>
        <input type="button" value="추가" onclick="tableVal()">
        <!-- 전체 삭제 버튼 -->
        <input type="button" value="삭제" onclick="deleteAll()">
    </form>

    <div id="addtable">
        <table border="1" id="ctb">
            <col width="100px">
            <col width="100px">
            <col width="300px">
            <col width="200px">
            <col width="100px">
            <thead>
                <tr>
                    <th>아이디</th>
                    <th>비밀번호</th>
                    <th>주소</th>
                    <th>전화번호</th>
                    <th>삭제</th>
                </tr>
            </thead>
            <tbody id="addtr"></tbody>

        </table>
    </div>
    
</body>
</html>
```



## js-ajax

```html
<script>
        function ajaxTest(){

            var xhr = new XMLHttpRequest(); //객체 생성 (통신 관련된 객체)

            //on 시리즈는 이벤트다 , readystate가 발생할때마다 callback 발생
            xhr.onreadystatechange = function(){ //이 함수가 call back (onreadystatechange가 실행할때마다 해당 함수를 호출)
                // 4: 요청의 완료
                if(xhr.readyState==4){
                    // 200: 정상 응답
                    if(xhr.status ==200){
                        // alert(xhr.responseText);
                        var respXml = xhr.responseXML; //응답된 데이터는 xml이야 라고 말해줌(원래 받는 문서는 str형태이다->xml 객체로 바꿔줌)
                        // console.log(respXml);
                        // console.log(typeof(respXml))

                        var table = document.getElementById('tb');
                        var rows = respXml.getElementsByTagName('ROW'); //ROW의 타입은 노드리스트 -> ROW[0] : 노드이다
                        // console.log(rows);

                        //emplist.xml을 서버에서 가지고 와서 xml 파일 안에 있는 데이터들을 table 안에 
                        // tr 태그 만들고, td태그 만들고 텍스트 넣어서 화면에 출력시켜라

                        // 1. column 이름 만들자
                        var columnTr = document.createElement('tr');
                        for (var i= 0 ; i<rows[0].children.length; i++){ //ROW 의 CHILDREN 5개 데이터를 가져올거다
                            // console.log(rows[0].children[i].nodeName)
                            var th = document.createElement("th");
                            th.appendChild(document.createTextNode(rows[0].children[i].nodeName))

                            columnTr.appendChild(th)
                            
                           

                        }
                        table.appendChild(columnTr)

                        //2. data 만들자
                        for (var i=0; i<rows.length; i++){
                            var tr=document.createElement("tr");
                            for (var j=0; j<rows[i].children.length; j++){
                                var td = document.createElement("td");
                                td.appendChild(document.createTextNode(rows[i].children[j].textContent));
                                tr.appendChild(td);
                            }
                            table.appendChild(tr);
                        }
                        
                        
                            
                            
                    }      
            }
        }
            // get 방식으로 요청 , 해당 경로에 요청
            xhr.open('GET' , 'emplist.xml'); // GET방식으로 뒤의 경로로 연결
            xhr.send();
        }
    </script>
</head>
<body>

    <!-- 
        ajax : Asynchronous Javascript And Xml
        비 동기 통신\
        클라이언트와 서버가 동기화되지 않는다
        일반적으로 서버에 요청을 하면 기다린다. (아무것도 안하고 기다린다)
        그러나 비 동기 통신은 요청하고 지 할거 한다.
        callback : call 해야지 back 할거야
        
     -->

    <button onclick="ajaxTest();">ajax</button>
    <table id="tb" border="1"></table>


    
</body>
</html>
```

