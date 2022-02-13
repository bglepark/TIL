function fileFunction(){
    window.alert("외부 js file에서 실행됨!!");
    
}

// onload 는 모든걸 다 한다음에 수행해라 라는 뜸
window.onload = function(){
    alert("윈도우 로딩 됨! (로딩 후)");
}