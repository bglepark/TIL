# HTML

HTML(Hypertext Markup Language)는 웹 페이지와 그 내용을 구조화하기 위해 사용하는 코드이다.

즉, 온라인 상의 문서를 만들기 위해 데이터를 구조화 시키는 언어이다.



## HTML의 구성

1. **여는 태그(opening tag)**: 이것은 요소의 이름으로 구성되고 (여기에서는 p), 여닫는 꺾쇠괄호로 감싸집니다. 이것은 요소가 시작되는 곳, 또는 효과를 시작하는 곳임을 나타냅니다 — 이 예제에서는 문단이 시작되는 위치를 나타냅니다.

2. **닫는 태그(closing tag)**: 이것은 여는 태그와 같지만, 요소의 이름 앞에 전방향 슬래시가 포함된다는 점이 다릅니다. 이것은 요소의 끝을 나타냅니다 — 이 예제에서는 문단이 끝나는 위치를 나타냅니다. 초보자가 가장 흔히 범하는 오류 중 하나가 닫는 태그를 쓰지 않는 것으로 이상한 결과가 표시됩니다.

3. **컨텐츠(content)**: 이것은 요소의 내용(content)으로 이 예제에서는 그냥 텍스트입니다.

4. **요소(element)**: 요소는 여는 태그와 닫는 태그, 그리고 컨텐츠로 이루어집니다.

   <meta> : 문서의 기본 정보 등
   <title> : 문서의 제목
   <script> : javascript 등
   <style> : css 등
   <link> : 외부 문서 연결
   <!--주석처리-->

## HTML 텍스트 요소

1. 제목

   - HTML은 제목을 표현할 수 있는 다양한 크기의 <h>태그를 제공합니다.

     가장 큰 <h1>태그부터 가장 작은 <h6>태그까지 다양한 크기로 제목을 표현할 수 있습니다.

     ```html
     <h1>제목1의 크기입니다!</h1>
     
     <h2>제목2의 크기입니다!</h2>
     
     <h3>제목3의 크기입니다!</h3>
     
     <h4>제목4의 크기입니다!</h4>
     
     <h5>제목5의 크기입니다!</h5>
     
     <h6>제목6의 크기입니다!</h6>
     ```

2. 단락

   - 단락이란 내용상 끊어서 구분할 수 있는 하나하나의 부분을 의미하며, 문단이라고도 부릅니다.

     HTML에서는 <p>태그를 이용하여 이러한 단락을 표현합니다.

     ```html
     <h1>제목1의 크기입니다!</h1>
     
     <h2>제목2의 크기입니다!</h2>
     
     <h3>제목3의 크기입니다!</h3>
     
     <p>여기서부터 단락입니다.</p>
     ```

3. 서식

   강조 효과

   - HTML 문서에서 텍스트를 굵게 표현하고 싶을 때에는 <b>태그(bold text)나 <strong>태그를 사용하면 됩니다.

   - <b>태그는 단순히 화면의 텍스트를 굵게 표현해 줍니다.

     하지만 <strong>태그는 텍스트를 굵게 표현해줄 뿐만 아니라 그 내용이 중요하다는 의미도 함께 포함해 줍니다.

   - HTML 문서에서 이탤릭체를 표현하고 싶을 때에는 <i>태그(italic text)나 <em>태그(emphasized text)를 사용합니다.

   - <i>태그는 단순히 화면의 텍스트를 이탤릭체로 표현해 줍니다.

     하지만 <em>태그는 텍스트를 이탤릭체로 변환해줄 뿐만 아니라 그 내용이 중요하다는 의미도 함께 포함해 줍니다.

     ```html
     <p>
             <b>진하게(&lt;b&gt;)</b><br/>
             <strong>강하게(&lt;strong&gt;)</strong><br>
             <i>기울임(&lt;i&gt;)</i><br>
             <em>강조하여(&lt;em&gt;)</em><br>
             <small>작은 텍스트, 코멘드 (&lt;small&gt;)</small><br>
             위<sup>첨자</sup>(&lt;sup&gt;)<br>
             아래<sub>첨자</sub>(&lt;sub&gt;)<br>
             <ins>내용 추가</ins>(&lt;ins&gt;)<br>
             <del>내용 삭제</del>(&lt;del&gt;)
         </p>
     ```

     

4. 짧은 인용구

   - 짧은 인용구는 <q>태그(quotation)를 사용하여 표현할 수 있으며, 자동으로 앞뒤에 큰따옴표가 붙습니다.

     ```html
     <p>HTML의 정의는
     
     <q>웹 페이지를 만들기 위한 하이퍼텍스트 마크업 언어</q>
     
     입니다.</p>
     ```

5. 엔티티

   - HTML에는 미리 예약된 몇몇 문자가 있으며, 이러한 문자를 HTML 예약어(reserved characters)라고 부릅니다.

     이러한 HTML 예약어를 HTML 코드에서 사용하면, 웹 브라우저는 그것을 평소와는 다른 의미로 해석합니다.

     따라서 HTML 예약어를 기존에 사용하던 의미 그대로 사용하기 위해 별도로 만든 문자셋을 엔티티(entity)라고 합니다.

     | 엔티티 문자 | 엔티티 이름 | 16진수 엔티티 숫자 |       설명        |
     | :---------: | :---------: | :----------------: | :---------------: |
     |             |   &nbsp;    |       &#160;       | 줄 바꿈 없는 공백 |
     |      <      |    &lt;     |       &#60;        |     보다 작은     |
     |      >      |    &gt;     |       &#62;        |      보다 큰      |
     |      &      |    &amp;    |       &#38;        |     AND 기호      |
     |      "      |   &quot;    |       &#34;        |     큰따옴표      |
     |      '      |   &apos;    |       &#39;        |    작은따옴표     |



## HTML 기본 요소

HTML 요소의 style 속성(attribute)을 이용하면 CSS 스타일을 HTML 요소에 직접 설정할 수 있습니다.

하지만 이러한 style 속성을 이용한 방법은 오직 단 하나의 HTML 요소에만 스타일을 적용할 수 있습니다.

```html
<태그이름 style="속성이름:속성값">
```



1. 배경색 변경

   ```html
   <h1 style="background-color:white">
   
       style 속성을 이용한 배경색 변경
   
   </h1>
   ```

2. 글자색 및 글자 크기 변경

   ```html
   <h1 style="color:maroon">
       style 속성을 이용한 글자색 변경
   
   </h1>
   
   <h1 style="font-size:300%">
       style 속성을 이용한 글자 크기 변경
   
   </h1>
   ```

3. 문단 정렬 변경

   ```html
   <h1 style="text-align:center">
   
       style 속성을 이용한 문단 정렬 변경
   
   </h1>
   ```

4. 이미지

   - HTML 문서에 이미지를 삽입할 때는 <img>태그를 사용합니다.

     <img>태그는 종료 태그가 없는 빈 태그(empty tag)이며, 다음과 같은 문법으로 사용됩니다.

     src 속성은 이미지가 저장된 주소의 URL 주소를 명시합니다.

     alt 속성으로 이미지가 로딩될 수 없는 상황에서 이미지 대신 나타날 문자열을 설정할 수 있습니다.

     ```html
     <h1>이미지</h1>
         <!--
             속성
             src : 경로
             alt : 설명(그림이 로딩되지 않을 경우)
             width : 너비 (가로)
             height : 높이 (세로)
         -->
         <img src="./images/img.jpg" alt="그림입니다" width="400px" height="400px">
         <!--
             px : 픽셀 (해상도 별 상대크기)
             pt : 포인트 (1pt = 약 0.72인치)
             % , em : 지정/상속 등에 대한 백분율 (부모에 대한 상대크기)
         -->
     
         <!--이미지에 링크 걸기-->
         <a href="index.html">
             <img src="images/img.jpg" alt='그림 링크입니다.' width="50px" height="50px">
         </a>
         <br/>
        
         <!--이미지의 특정 부분에 링크 걸기 (image map)-->
         <img src ="images/img.jpg" alt="그림입니다." 
             width="200px" height="200px" usemap="#my">
     
         <map name="my">
             <area shape ='rect' coords="25 , 25 , 175 , 175" href="index.html" alt="그림입니다"
         </map>
     ```



5. 테이블

   테이블(Table)이란 여러 종류의 데이터(data)를 보기 좋게 정리하여 보여주는 표를 의미합니다.

   HTML에서는 <table>태그를 사용하여 이러한 테이블을 작성할 수 있습니다.

   1. <tr>태그는 테이블에서 열을 구분해 줍니다.

   2. <th>태그는각 열의 제목을 나타내며, 모든 내용은 자동으로 굵은 글씨에 가운데 정렬이 됩니다.

   3. <td>태그는 테이블의 열을 각각의 셀(cell)로 나누어 줍니다.

   ```html
   <h1>table</h1>
       <h2>기본 테이블</h2>
       <table>
           <tr>
               <th>컬럼1</th>
               <th>컬럼2</th>
           </tr>
           <tr>
               <td>데이터1</td>
               <td>데이터2</td>
           </tr>
           <tr>
               <td>데이터3</td>
               <td>데이터4</td>
           </tr>
       </table>
   ```

   ```html
   <h2>추가</h2>
       <table border="1"> <!--뒤의 숫자는 선 굵기-->
           <caption>테이블 제목</caption>
           <colgroup>
               <col width = "100px" style="background-color: blueviolet;">
               <col width = "300px">
               <col width = "500px">
           </colgroup>
   
           <thead>
               <tr>
                   <th>컬럼1</th>
                   <th>컬럼2</th>
                   <th>컬럼3</th>
               </tr>
           </thead>
   
           <tfoot>
               <tr>
                   <td>foot1</td>
                   <td>foot2</td>
                   <td>foot3</td>
               </tr>
           </tfoot>
   
           <tbody>
               <tr style="color: red;">
                   <td>1</td>
                   <td>2</td>
                   <td>3</td>
               </tr>
               <tr style="color: seagreen;">
                   <td>4</td>
                   <td>5</td>
                   <td>6</td>
               </tr>
               <tr>
                   <td>7</td>
                   <td>8</td>
                   <td>9</td>
               </tr>
           </tbody>
       </table>
   ```

   ```html
   <h2>셀 병합</h2>
       <table border = "1">
           <colgroup>
               <col width = "200px">
               <col width = "200px">
               <col width = "200px">
               <col width = "200px">           
           </colgroup>
   
           <thead>
               <tr>
                   <th>컬럼1</th>
                   <th>컬럼2</th>
                   <th>컬럼3</th>
                   <th>컬럼4</th>
               </tr>
           </thead>
   
           <tbody>
               <tr>
                   <td rowspan ="2"> 1 (열합치기)</td>
                   <td>2</td>
                   <td>3</td>
                   <td>4</td>
               </tr>
               <tr>
                   <td>6</td>
                   <td colspan="2">7 (행 합치기)</td>
   
               </tr>
               <tr>
                   <td>9</td>
                   <td>10</td>
                   <td>11</td>
                   <td>12</td>
               </tr>
           </tbody>
   
           <tfoot>
               <tr>
                   <td colspan="4" align="center">행 4개 합치기</td>
               </tr>
           </tfoot>
   
       </table>
   ```

6. 리스트

   리스트(list)란 여러 요소들을 일렬로 나열한 목록이나 명단을 의미합니다.

   HTML에서는 이러한 리스트를 표현하기 위해 다음과 같은 리스트를 제공하고 있습니다.

   1. 순서가 없는 리스트(unordered list)

   2. 순서가 있는 리스트(ordered list)

   3. 정의 리스트(definition list)

   ```html
       <h2>순차적 목록</h2>
       <!--ol : ordered list-->
       <!--li : 실제 리스트-->
       <ol>
           학원 오는 순서
           <li>눈을 뜬다</li>
           <li>침대에서 나온다</li>
           <li>씻는다
               <ol>
                   <li>양치한다</li>
                   <li>머리감는다</li>
                   <li>샤워한다</li>
               </ol>
           </li>
           <li>옷입는다</li>
           <li>출발한다</li>
       </ol>
   ```

   ```html
   <h2>비 순차적 목록</h2>
       <!--ul : unordered list-->
       <ul>
           점심 고르기
           <li>굶는다</li>
           <li>짜파게티</li>
           <li>편의점
               <ul>
                   <li>불닭 + 치즈볶</li>
                   <li>도시락</li>
                   <li>컵라면+참김</li>
                   <li>삼각김밥</li>
                   <li>샌드위치</li>
               </ul>
           </li>
       </ul>
   ```

   ```html
    <h2>정의형 목록</h2>
       <!--dl : definition list(description list)-->
       <dl>
           <dt>제목</dt>
           <dd>내용</dd>
       </dl>
   
       <dl>
           <dt>ds/de 커리큘럼</dt>
           <dd>python</dd>
           <dd>numpy/pandas</dd>
           <dd>html css js jq</dd>
           <dd>django</dd>
           <dd>crawling / visualization</dd>
           <dd>
               <dl>
                   <dt>ds</dt>
                   <dd>ml</dd>
                   <dd>dl</dd>
                   <dd>...</dd>
               </dl>
               <dl>
                   <dt>de</dt>
                   <dd>ml</dd>
                   <dd>hadoop / spark</dd>
               </dl>
           </dd>
       </dl>
   ```



## 블록과 인라인

HTML의 모든 요소는 해당 요소가 웹 브라우저에 어떻게 보이는가를 결정짓는 display 속성을 가집니다.

대부분의 HTML 요소는 이러한 display 속성값으로 다음 두 가지 값 중 하나를 가지게 됩니다.

1. 블록(block) 타입

   display 속성값이 블록(block)인 요소는 언제나 새로운 라인(line)에서 시작하며, 해당 라인의 모든 너비를 차지합니다.

   ```html
   <p style="border: 3px solid red">
   
       p요소는 display 속성값이 블록인 요소입니다.
   
   </p>
   ```

```
<p>, <div>, <h>, <ul>, <ol>, <form>요소는 display 속성값이 블록(block)인 대표적인 요소입니다.
```



- div 요소

  ```
  <div>요소는 다른 HTML 요소들을 하나로 묶는 데 자주 사용되는 대표적인 블록(block) 요소입니다.
  
  <div>요소는 주로 여러 요소들의 스타일을 한 번에 적용하기 위해 사용됩니다.
  ```

  ```html
  <div style="background-color:lightgrey; color:green; text-align:center">
  
      <h1>div요소를 이용한 스타일 적용</h1>
  
      <p>이렇게 div요소로 여러 요소들을 묶은 다음에 style 속성과 클래스 등을 이용하여
  
      한 번에 스타일을 적용할 수 있습니다.</p>
  
  </div>
  ```

  ```html
  <h2 style="background-color:blue;">block</h2>
      <p>줄바꿈</p>
      <div>
          블록 요소 안에 텍스트, <strong>인라인 요소</strong> 포함 가능
          <p>블록 요소 안에 블록 요소 포함 가능</p>
      </div>
  ```



2. 인라인(inline)타입

​		display 속성값이 인라인(inline)인 요소는 새로운 라인(line)에서 시작하지 않습니다.

​		또한, 요소의 너비도 해당 라인 전체가 아닌 해당 HTML 요소의 내용(content)만큼만 차지합니다.

```html
<p>

    <span style="background-color:grey; color:orange">span태그</span>는 display 속성값이 인라인인 요소입니다.

</p>
```

```
<span>, <a>, <img>요소는 display 속성값이 인라인(inline)인 대표적인 요소입니다.
```

- span 요소

  ```
  <span>요소는 텍스트(text)의 특정 부분을 묶는 데 자주 사용되는 인라인(inline) 요소입니다.
  
  <span>요소는 주로 텍스트의 특정 부분에 따로 스타일을 적용하기 위해 사용됩니다.
  ```

  ```html
  <p>이렇게
  
  <span style="border: 3px solid red">span요소로 텍스트의 일부분</span>
  
  만을 따로 묶은 후에 스타일을 적용할 수 있습니다.</p
  ```

  ```html
  <h2>inline</h2>
      <a href="#">줄바꿈X</a>
      <q style = "background-color: red">인라인 요소 안에 텍스트, <b>인라인 요소</b>포함 가능</q><br/>
      <span>인라인 요소 안에 <p>블록 요소</p> 포함 불가</span>
      <!--사용은 가능하나, 지양하자!!-->
  ```

  -> 인라인 요소 안에 블록요소 사용은 가능하지만 지양해야 한다.



## 레이아웃

1. 레이아웃 1번 유형 (id로 구분)

   ```html
   <!-- style type=css 스타일로 하겠다 라는 뜻-->
       <!-- padding과 margin을 0으로 만들고 시작-->
       <style type="text/css">        
   
           *{
               padding: 0px;
               margin: 0px;
           }
   
           div{
               border: 1px dashed blue;
               margin: 10px;
           }
   
           #body{
               height: 400px;
           }
   
           #left{
               width: 48%;
               height:90%;
               float: left;
   
           }
           #right{
               width:48%;
               height:90%;
               float:right;
           }
   
       </style>
   </head>
   <body>
   
       <div id="header">
           <h1>제목</h1>
           <div>
               <span><a href="#">메뉴1</a></span>
               <span><a href="#">메뉴2</a></span>
               <span><a href="#">메뉴3</a></span>
               <span><a href="#">메뉴4</a></span>
           </div>
       </div>
       <div id="body">
           <div id="left">
               <p>내용1</p>
           </div>
           <div id="right">
               <p>내용2</p>
           </div>
       </div>
   
       <div id="footer">
           <address>copyright &copy; all rights reserved.... </address>
       </div>
       
   </body>
   </html>
   ```



2. 레이아웃 2번 유형(header , section , footer로 구분)

   ```html
   <style type="text/css">
           *{
               padding:0px;
               margin:0px;
           }
   
           .html5{
               border : 1px dotted red;
               margin : 10px;
           }
           section{
               height: 400px;
           }
   
           #left{
               width: 48%;
               height:90%;
               float: left;
   
           }
           #right{
               width:48%;
               height:90%;
               float:right;
           }
       </style>
   </head>
   <body>
   
       <header class="html5">
           <h1>제목</h1>
           <nav class="html5">
               <span><a href="#">메뉴1</a></span>
               <span><a href="#">메뉴2</a></span>
               <span><a href="#">메뉴3</a></span>
               <span><a href="#">메뉴4</a></span>
   
           </nav>
       </header>
   
       <section class="html5">
           <article class="html5" id="left">
               <p>내용1</p>
           </article>
   
           <article class="html5" id="right">
               <p>내용2</p>
           </article>
       </section>
   
       <footer class="html5">
           <address>copyright &copy; all rights reserved.... </address>
       </footer>
       
   </body>
   ```

   

## Form

웹 페이지에서는 form 요소를 사용하여 사용자로부터 입력을 받을 수 있습니다.

또한, 사용자가 입력한 데이터를 서버로 보낼 때에도 form 요소를 사용합니다.

form 요소는 다음과 같은 문법으로 사용합니다.

```html
<form action=‘경로’ method=‘전송 방식’>
<input type=‘형태’ name=‘name’ value=‘value’/>
<input type=‘submit’ value=‘전송’/>
</form>
```

- 전송 방식

  - GET : request header에 data를 담아서 전송 (queryString)
    - 주소에 데이터를 추가하여 전달하는 방식이며, 전송할 수 있는 데이터가 제한적이다.
    - 크기가 작고 중요도가 낮은 정보를 보낼 때 주로 사용한다.
  - POST : request body에 data를 담아서 전송
    - 데이터가 외부에 드러나지 않고 별도로 첨부하여 전달, 데이터의 크기 또한 제한이 없다.
    - queryString : url?name=value&name=value 형태

- action 속성은 입력받은 데이터를 처리할 서버 상의 스크립트 파일의 주소를 명시합니다.

  이렇게 전달받은 데이터를 처리하는 스크립트 파일을 폼 핸들러(form-handler)라고 합니다.

  method 속성은 입력받은 데이터를 서버에 전달할 방식을 명시합니다.

  따라서 사용자가 form 요소를 통해 입력한 데이터는 action 속성에 명시된 위치로 method 속성의 방식을 통해 전달됩니다.

  form 태그 안에 있는 name 및 value 속성을 가지고 action에 요청을 합니다.

  ```html
  <body>
  
      <form action="html-form-res.html" method="post">
          <fieldset>
              <legend>회원가입</legend>
  
              <p>ID : <input type ="text" name ="id" /></p>
              <p>PW : <input type="password" name="pw"></p>
  
              <p>Email 수신 여부 <br>
                  <input type="radio" name="rdo" value="y"> y
                  <input type="radio" name="rdo" value="n"> n
  
              </p>
              <p>관심분야 <br>
                  <input type="checkbox" name="web" value="web">WEB <br>
                  <input type="checkbox" name="ai" value="ai"> Data Science <br>
                  <input type="checkbox" name="engi" value="engi"> Data Engineer
              </p>
              <p>하고싶은 말
                  <textarea name="etc" cols="60" rows="10"></textarea>
              </p>
              <p>
                  <input type="button" value="그냥 버튼"><br>
                  <input type="reset" value="취소"><br>
                  <input type="submit" value="전송">
              </p>
          </fieldset>
  
      </form>
      
  </body>
  ```

  

  - Select 방식으로 Form 구성

  ```html
  <body>
  
      <h1>select</h1>
  
      <form action="html-form-res.html" method="get">
          <p>
              점심
              <select name="lunch" >
                  <option value="chicken">치킨</option>
                  <option value="pizza">피자</option>
                  <option value="sushi">초밥</option>
                  <option value="yangjangpi">양장피</option>
                  <option value="maratang">마라탕</option>
              </select>
          </p>
  
          <p>
              저녁
          <select name="dinner">
              <optgroup label="한식">
                  <option value="sinsunro">신선로</option>
                  <option value="dduckgalbi">떡갈비</option>
                  <option value="kukbab">소머리국밥</option>
                  <option value="bulgogi">불고기</option>
                  <option value="coldnoodle">냉면</option>
  
              </optgroup>
  
              <optgroup label="양식">
                  <option value="steak">스테이크</option>
                  <option value="pasta">파스타</option>
                  <option value="taco">타코</option>
              </optgroup>
          </select>
          </p>
          <p>
              <input type="submit" value="선택">
          </p>
  
  
      </form>
      
  </body>
  ```

  

  