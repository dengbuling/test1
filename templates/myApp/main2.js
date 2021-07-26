/*
console.log(window);
alert(1);
*/

/*
console.log(document.querySelector('.link1'))*/



/*console.log(document.getElementsByClassName('link1'))*/


/*console.log(document.querySelectorAll('.item'));
console.log(document.querySelectorAll('li'));*/

/*
const items = document.querySelectorAll('.item');
items.forEach((item) => console.log(item));*/

/*const items = document.querySelectorAll('li');
items.forEach(function(item) {
    if (items.length === 9){
        return console.log(item);
    }
})*/

const ul = document.querySelector('.link1')

/*
ul.style.background = 'red';*/


/*
未理解
ul.addEventListener('click' ,(e) => {
    e.preventDefault();
    console.log('click');
    document.querySelector('.link1').style.background = 'red';
    document.querySelector('.link1').lastElementChild.innerHTML = '<h1>hello<h1>';
})
*/



//修改HTML内容
document.querySelector('.box11').innerHTML = 'Hello';
console.log(document.querySelector('.box11'))


//操作dom元素
document.querySelector('.box14').onclick = function click() {
  document.getElementById("demo").innerHTML = Date();
}



/*
document.querySelector('.box14').addEventListener('click', clickfun)

function clickfun(){
    document.getElementById("demo").style.background = 'red';
}
*/



document.querySelector('.box14').addEventListener('click', function() {
    document.getElementById("demo").style.background = 'red';
    //创建元素
    const para = document.createElement('p');
    const node = document.createTextNode('我是增加的一行!');
    para.appendChild(node);
    document.querySelector('.box').appendChild(para)
    document.querySelector('.img').src = "2.png"
})

document.querySelector('.img').onclick = function changeImg(){
    if (document.querySelector('.img').src.match("1.png")){
        document.querySelector('.img').src = "2.png"
        const Plists = document.querySelectorAll('p')
        Plists.forEach(function(Plist){
            Plist.innerHTML = 'Date();'
})
    }
    else{
        document.querySelector('.img').src = "1.png"
    }
}


document.querySelector('.box15').addEventListener('click', function() {
    document.querySelector('.img').src = "1.png"
})


/*
const Plists = document.querySelectorAll('p')
Plists.forEach(function(Plist){
    Plist.innerHTML = 'Date();'
})*/

console.log(window.innerWidth);
console.log(window.innerHeight);
console.log(screen.availWidth);
console.log(screen.availHeight);
console.log(location.href);
/*
window.confirm("sometext");
*/
/*
确认弹窗
window.prompt("sometext","defaultText");*/

