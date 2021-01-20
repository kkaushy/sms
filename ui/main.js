var baseURL = "https://sfva061pkj.execute-api.ap-south-1.amazonaws.com/dev/api/"

var image = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAACqUlEQVR4Xu2Y60tiURTFl48STFJMwkQjUTDtixq+Av93P6iBJFTgg1JL8QWBGT4QfDX7gDIyNE3nEBO6D0Rh9+5z9rprr19dTa/XW2KHl4YFYAfwCHAG7HAGgkOQKcAUYAowBZgCO6wAY5AxyBhkDDIGdxgC/M8QY5AxyBhkDDIGGYM7rIAyBgeDAYrFIkajEYxGIwKBAA4PDzckpd+322243W54PJ5P5f6Omh9tqiTAfD5HNpuFVqvFyckJms0m9vf3EY/H1/u9vb0hn89jsVj8kwDfUfNviisJ8PLygru7O4TDYVgsFtDh9Xo9NBrNes9cLgeTybThgKenJ1SrVXGf1WoVDup2u4jFYhiPx1I1P7XVBxcoCVCr1UBfTqcTrVYLe3t7OD8/x/HxsdiOPqNGo9Eo0un02gHkBhJmuVzC7/fj5uYGXq8XZ2dnop5Mzf8iwMPDAxqNBmw2GxwOBx4fHzGdTpFMJkVzNB7UGAmSSqU2RoDmnETQ6XQiOyKRiHCOSk0ZEZQcUKlU8Pz8LA5vNptRr9eFCJQBFHq//szG5eWlGA1ywOnpqQhBapoWPfl+vw+fzweXyyU+U635VRGUBOh0OigUCggGg8IFK/teXV3h/v4ew+Hwj/OQU4gUq/w4ODgQrkkkEmKEVGp+tXm6XkkAOngmk4HBYBAjQA6gEKRmyOL05GnR99vbW9jtdjEGdP319bUIR8oA+pnG5OLiQoghU5OElFlKAtCGr6+vKJfLmEwm64aosd/XbDbbyIBSqSSeNKU+HXzlnFAohKOjI6maMs0rO0B20590n7IDflIzMmdhAfiNEL8R4jdC/EZIJj235R6mAFOAKcAUYApsS6LL9MEUYAowBZgCTAGZ9NyWe5gCTAGmAFOAKbAtiS7TB1Ng1ynwDkxRe58vH3FfAAAAAElFTkSuQmCC"
var token = "";
var currentChatId = "1"
var loggedInID = "1"
$(document).ready(function(){
    login()
})

function getUsers(){
    $.ajax({
        url: baseURL+"user",
        type: 'GET',
        dataType: 'json',
        headers: {
            'Authorization': token,
        },
        contentType: 'application/json;',
        success: function (data) {
            for (i in data){
                var username = data[i].username
                var userid = data[i].id
                if (userid!=loggedInID){  
                    usertemplate = '<div class="media conversation" onclick="getUserChat('+userid+')"><a class="pull-left" href="#"><img class="media-object" data-src="holder.js/64x64" alt="64x64" style="width: 50px; height: 50px;" src='+image+'></a><div class="media-body"><h5 class="media-heading" >'+username+'</h5></div></div>';
                    $('.conversation-wrap').append(usertemplate);    
                }
            }
            getUserChat(data[0].id)
        },
        error: function (error) {
            console.log(error);
        }
    });
}

function getUserChat(id){
    console.log(id)
    currentChatId = id
    $.ajax({
        url: baseURL+"sms?reciever="+currentChatId,
        type: 'GET',
        dataType: 'json',
        headers: {
            'Authorization': token,
        },
        contentType: 'application/json;',
        success: function (result) {
           console.log(result);
           $('.msg-wrap').html("");
           for(i in result){
               var message = result[i];
               chatTemplate = '<div class="media msg"><a class="pull-left" href="#"><img class="media-object" data-src="holder.js/64x64" alt="64x64" style="width: 32px; height: 32px;" src='+image+'></a><div class="media-body"><small class="pull-right time"><i class="fa fa-clock-o"></i> 12:10am</small><h5 class="media-heading">'+message.sender_name+'</h5><small class="col-lg-10">'+message.text+'</small></div></div>'
               $('.msg-wrap').append(chatTemplate)
           }
        },
        error: function (error) {
            console.log(error);
        }
    });
}


function sendMessage(){
    var data = {
        'reciever': currentChatId,
        'text':$('#txtMessage').val()
    }
    $.ajax({
        url: baseURL+'sms',
        type: 'post',
        data: JSON.stringify(data),
        contentType: 'application/json;',
        headers: {
            Authorization: token
        },
        dataType: 'json',
        success: function (data) {
            $('#txtMessage').val("")
            getUserChat(currentChatId)
            console.info(token);
        }
    });
}

function login(){

    $.ajax({
        url: baseURL+'login/',
        type: 'post',
        data: {
            'username': 'user2',
            'password':'welcome'
        },
        dataType: 'json',
        success: function (data) {
            token = "JWT "+data.token
            $("#loggedIn").html(data.username)
            loggedInID = data.user;
            console.info(token);
            getUsers();
        }
    });
}