$(".box16").click(function(){
    $.ajax({
        url:'/students2/',
        type:'GET',
        dataType: 'json',
        success: function(result){
//            $(".td1").html(result.name).css("background","red")
            var html = ''
            $.each(result, function(i ,obj){
                html += "<tr>"
                html += "<td>"+obj.name+"</td>"
                html += "<td>"+obj.age+"</td>"
                html += "</tr>"

            });
            $(".show").html(html)
        }

    });
});