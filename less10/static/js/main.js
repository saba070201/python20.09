function send_data(){
    $.ajax({
        type: "GET",
        url: "/connect",
        dataType: "json",
        contentType: "application/json",
        data:{
            "value":document.getElementById("value").value,
            "value1":document.getElementById("value1").value,
        },
        success: function(response){
            
        }
    })
}