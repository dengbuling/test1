
$(".box17").click(function(){
    var json_attr = [
    {
        "name":"tom",
        "age":19
    },
    {
        "name":"harry",
        "age":18
    },
    {
        "name":"potter",
        "age":15
    }
]

    $.ajax({
        url:"/title1/",
        type: "GET",
        success:function(result){
        $(".box13").val(result).css("background","red")
        //console.log('jhjh')
        //console.log(X.name)
        //循环json数组
        $(json_attr).each(function(i,obj){
            console.log(i)
            console.log(obj.name)
        })
        $.each(json_attr, function(i,obj){
            console.log(i)
            console.log("hhh"+obj.name)
        })
        }
    });

});



