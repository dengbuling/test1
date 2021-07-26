console.error("hello word");
console.log("hello word");
console.warn("hello word");

/*let age=10;
console.log(age);*/

const age = 10;
const name = 'peter';
const isgood = true;
const point = 9.9;
const x = null;
console.log(typeof age);
console.log(typeof name);
console.log(typeof isgood);
console.log(typeof point);
console.log(typeof x);
console.log(name.substring(0,2).toUpperCase())
const s = 'peter, ball, harry, potter';
console.log(s.split(", "));

const people = ["peter", "ball", "harry", "potter"];
console.log(people[0]);

const people1 = ["peter", "ball", "harry", "potter"];
people1.push("tom")
people1.pop()
people1.unshift("tom")
console.log(people1);
console.log(people1.indexOf("tom"));

for(i = 0; i < 10; i++){
    //反向单引号
    console.log(`number: ${i}`);
}

const foods = [
    {
        id:1,
        name:"tomato",
        color:"tomato",
    },
    {
        id:2,
        name:"pink",
        color:"pink",
    },
    {
        id:3,
        name:"blue",
        color:"blue",
    },
];
//循环数组
/*for(food of foods){
    console.log(food.name);
}*/
//foreach(迭代器)
/*
foods.forEach(function(food) {
    if (foods.length===3){
        console.log(food.name);
    }
});*/
//map返回新的数组(迭代器)
/*const foodtext = foods.map(function(food){
    if (foods.length === 3){
        return food.color;
    }
})
console.log(foodtext);*/
//filter选择器
const foodfilter = foods.filter(function(food){
    return food.color==='blue';
}).map(function(food)
{
    return food.name;
})
console.log(foodfilter)

const A = 11;
const color = A > 10 ? 'red' : 'blue';

switch(color) {
    case 'red':
        console.log(`color is:${color}`)
        break;
    case 'blue':
        console.log(`color is:${color}`)
        break;
    default:
        console.log('no color')
        break;
}
function addnum(num1, num2) {
    return num1+num2
}
console.log(addnum(3,4))

const add = (num3 ,num4) => num3+num4;
console.log(add(6,7))
