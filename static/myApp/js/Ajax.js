function CreateXml() {
    if (window.XMLHttpRequest){
        var xhr = new XMLHttpRequest();
        console.log('1122334455');
    }else{
        var xhr = new ActiveXObject("Microsoft.XMLHTTP");
    }
    return xhr
};


document.querySelector('.box16').onclick = function getXhr(){
    var xhr = CreateXml();
    //创建请求
    xhr.open('GET', '/title1/', true);
    //事件回调（XHR状态变化就会执行）
    xhr.onreadystatechange = function(){
        if(xhr.readyState == 4 && xhr.status == 200){
            document.querySelector('.box13').innerHTML = xhr.responseText;
            console.log('1122');
            console.log(xhr.responseText);
        }
    }
    xhr.send(null)
};

document.querySelectorAll('p')[21].innerHTML = 'xhr.responseText';

const X = document.querySelectorAll('p')
X.forEach(function(list){
    list.innerHTML = 'xhr.responseText';
})


