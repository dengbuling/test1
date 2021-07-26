document.querySelector('.img').onclick = function changeImg(){
    if (document.querySelector('.img').src.match('111.png')){
        document.querySelector('.img').src = "/static/myApp/img/222.png"
    }
    else{
        document.querySelector('.img').src = "/static/myApp/img/111.png"
    }
};