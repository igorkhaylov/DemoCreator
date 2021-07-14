$("#submit_register").click(function () {
    $.ajax({
        type: "GET",
        url: "check_username/",
        data: {
            'username': $("#username").val(),
        },
        dataType: "text",
        cache: false,
        success: function (data) {
            if (data == "ok") {
                alert("this user is already exist")
            } else if (data == "no") {
                alert("this user is doesn't exist")
            }
        }
    });
});





