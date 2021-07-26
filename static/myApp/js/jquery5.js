$('.button1').click(function(){
    $.ajax({
        url:'/students2/',
        type:'POST',
        data:{
            name:$('.text1').val(),
            csrfmiddlewaretoken:$("[name='csrfmiddlewaretoken']").val()

        },
        success:function(result){
            alert("result")
            console.log(result)
        }
    })

})