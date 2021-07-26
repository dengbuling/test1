
$(".box17").click(function(){
    $.ajax({
        url:"/title1/",
        type: "GET",
        success:function(result){
        $(".box13").html(result)
        }
    });


});