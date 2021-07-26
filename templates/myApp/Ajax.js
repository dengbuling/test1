document.querySelector('.box16').onclick = function CreateXml() {
    if (window.XMLHttpRequest){
        var xhr = new XMLHttpRequest();
        //console.log('hahaha');
    else{
        var xhr = new ActiveXObject(S:'Microsoft.XMLHTTP');
    }
    return xhr;
    }
};


function getXhr(){
    var xhr = CreateXml();
    xhr.open('GET', '/title1/', true)
    xhr.onreadystatechange = function(){
        if(xhr.readyState == 4 && xhr.status == 200){
            document.querySelector('p').innerHtml = xhr.responseText;
        }
    }
};
xhr.send(null)
