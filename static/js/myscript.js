$("#submit_form").click(function () {
    if ($("#contact-your-name-2").val() == "" ||
        $("#contact-email-2").val() == "" ||
        $("#contact-phone-2").val() == "" ||
        $("#contact-message-2").val() == "") {
        console.log("Заполните все поля");
    } else {
        console.log("Ваше сообщение успешно отправлено");
    }
});


// $(function($){
//    $(".phone").mask("+998 (99) 999-9999",{placeholder:" "});
// });
$.mask.definitions['9'] = false;
$.mask.definitions['5'] = "[0-9]";
$(function($){
   $("#contact-phone-2").mask("+998 (55) 555-55-55",{placeholder:"***********"});
});

// $(".phone").mask("+998 (55) 555-55-55",{completed:function(){alert("Вы ввели: "+this.val());}});


// $("#contact-phone").focusout(function(){
//   var value = $(this).val().trim();
//   if (value.search(/\+998\s?[\(]{0,1}9[0-9]{2}[\)]{0,1}\s?\d{3}[-]{0,1}\d{2}[-]{0,1}\d{2}$/i) != 0) {
//     $(this).notify("Номер телефона введён не корректно", "error");
//     $(this).addClass("errtextbox");
//     errorMail = true;
//   } else {
//     $(this).removeClass("errtextbox");
//     errorMail = false;
//   }
// });



// $("#submit_login").click(function () {
//     $.ajax({
//         type: "GET",
//         url: "check_login/",
//         data: {
//             'username': $("#username2").val(),
//             'password': $("#password").val(),
//         },
//         dataType: "text",
//         cache: false,
//         success: function (data) {
//             if (data == "yes") {
//                 $("#submit_login").click(function () {
//                         $("#login").submit();
//                         $(this).notify("вы успешно вошли", "error");
//
//                 });
//
//
//             } else if (data == "no") {
//
//
//                 $("#submit_login").click(function () {
//                     $(this).notify("вы безуспешно не вошли", "error");
//                 });
//                 console.log("")
//             }
//
//         }
//     });
// });
// if (data == "ok") {
            //     $("#submit_login").click(function () {
            //         $(this).notify("Такой логин уже существует", "error");
            //     });
            //     console.log("this user is already exist");
            // } else if (data == "no") {
            //     $("#submit_login").click(function () {
            //         if (!(errorNull || errorPass)) {
            //             $("#login").submit();
            //         } else {
            //             $(this).notify("Форма пустая или заполнена не корректно", "error");
            //         }
            //     });
            //     console.log("this user is doesn't exist and you can continue");
            // }

// $("#submit_login").click(function () {
//     if (!(errorNull || errorPass)) {
//         $("#login").submit();
//     } else {
//         $(this).notify("Форма пустая или заполнена не корректно", "error");
//     }
//
// });









$("#submit_register").click(function () {
    $.ajax({
        type: "GET",
        url: "check_username/",
        data: {
            'username': $("#username").val(),
            'email_user': $("#email_user").val(),
        },
        dataType: "text",
        cache: false,
        success: function (data) {
            if (data == "email exist") {
                $("#submit_register").click(function () {
                    $(this).notify("Такой Email уже существует", "error");
                });
                console.log("this email is already exist")
            } else if (data == "email is doesn't exist") {

                console.log("Email is doesn't exist")
            }
            if (data == "ok") {
                $("#submit_register").click(function () {
                    $(this).notify("Такой логин уже существует", "error");
                });
                console.log("this user is already exist");
            } else if (data == "no") {
                $("#submit_register").click(function () {
                    if (!(errorNull || errorMail || errorPass)) {
                        $("#login").submit();
                    } else {
                        $(this).notify("Форма пустая или заполнена не корректно", "error");
                    }
                });
                console.log("this user is doesn't exist and you can continue");
            }
        }
    });
});





var errorNull = true, errorMail = true, errorPass = true;
var checkNull = function(){
  $(this).val($(this).val().trim());
  if ($(this).val() =="") {
    $(this).notify("Поле нужно заполнить", "error");
    $(this).addClass("errtextbox");
    errorNull = true;
  } else {
    errorNull = false;
    $(this).removeClass("errtextbox");
  }
};


$("#first_name").focusout(checkNull);
$("#last_name").focusout(checkNull);
$("#username2").focusout(checkNull);


$("#username").keyup(function(){
  var value = $(this).val();
  if (value.length < 6 && value.length > 25 ){
    $(this).notify("Максимум 25 символов", "info");
    $(this).val(value.slice(0,24));
  }
});

$("#email_user").focusout(function(){
  var value = $(this).val().trim();
  if (value.search(/(|(([A-Za-z0-9]+_+)|([A-Za-z0-9]+\-+)|([A-Za-z0-9]+\.+)|([A-Za-z0-9]+\++))*[A-Za-z0-9]+@((\w+\-+)|(\w+\.))*\w{1,63}\.[a-zA-Z]{2,6})$/i) != 0) {
    $(this).notify("E-mail введён не корректно", "error");
    $(this).addClass("errtextbox");
    errorMail = true;
  } else {
    $(this).removeClass("errtextbox");
    errorMail = false;
  }
});

$("#password").focusout(function(){
  var value = $(this).val();
  if (value.length <= 7) {
    $(this).notify("Минимум 8 символов", "error");
    $(this).addClass("errtextbox");
    errorPass = true;
  } else {
    if (value.length > 24) {
      $(this).notify("Миксимум 25 символов", "error");
      $(this).addClass("errtextbox");
      errorPass = true;
    } else {
      errorPass = false;
      $(this).removeClass("errtextbox");
    }
  }
});



$("#password1").focusout(function(){
  var value = $(this).val();
  if (value.length <= 7) {
    $(this).notify("Минимум 8 символов", "error");
    $(this).addClass("errtextbox");
    errorPass = true;
  } else {
    if (value.length > 24) {
      $(this).notify("Миксимум 25 символов", "error");
      $(this).addClass("errtextbox");
      errorPass = true;
    } else {
      errorPass = false;
      $(this).removeClass("errtextbox");
    }
  }
});

$("#password2").focusout(function(){
  var value = $(this).val();
  if (value != $("#password1").val()) {
    $(this).notify("Пароль не совпадает", "error");
    $(this).addClass("errtextbox");
    errorPass = true;
  } else {
    errorPass = false;
    $(this).removeClass("errtextbox");
  }
});

// $("#submit_register").click(function(){
//   if (!(errorNull || errorMail || errorPass)) {
//       // if (false) {
//     $("#login").submit();
//   } else {
//     $(this).notify("Форма пустая или заполнена не корректно", "error");
//   }
// });

$("#submit_register").click(function (e){
    e.preventDefault()
});

// $("#submit_login").click(function (e){
//     e.preventDefault()
// });









































// $("#submit_register").click(function () {
//     $.ajax({
//         type: "GET",
//         url: "check_username/",
//         data: {
//             'username': $("#username").val(),
//             'email_user': $("#email_user").val(),
//         },
//         dataType: "text",
//         cache: false,
//         success: function (data) {
//             if (data == "email exist") {
//                 console.log("this email is already exist")
//             } else if (data == "email is doesn't exist") {
//                 console.log("Email is doesn't exist")
//             }
//             if (data == "ok") {
//                 console.log("this user is already exist");
//             } else if (data == "no") {
//                 console.log("this user is doesn't exist and you can continue");
//             }
//         }
//     });
// });
//
//
//
//
//
// var errorNull = true, errorMail = true, errorPass = true;
// var checkNull = function(){
//   $(this).val($(this).val().trim());
//   if ($(this).val() =="") {
//     $(this).notify("Поле нужно заполнить", "error");
//     $(this).addClass("errtextbox");
//     errorNull = true;
//   } else {
//     errorNull = false;
//     $(this).removeClass("errtextbox");
//   }
// };
//
// $("#first_name").focusout(checkNull);
// $("#last_name").focusout(checkNull);
// // $("#email_user").focusout(checkNull);
//
// $("#username").keyup(function(){
//   var value = $(this).val();
//   if (value.length < 6 && value.length > 25 ){
//     $(this).notify("Максимум 25 символов", "info");
//     $(this).val(value.slice(0,24));
//   }
// });
//
// $("#email_user").focusout(function(){
//   var value = $(this).val().trim();
//   if (value.search(/(|(([A-Za-z0-9]+_+)|([A-Za-z0-9]+\-+)|([A-Za-z0-9]+\.+)|([A-Za-z0-9]+\++))*[A-Za-z0-9]+@((\w+\-+)|(\w+\.))*\w{1,63}\.[a-zA-Z]{2,6})$/i) != 0) {
//     $(this).notify("E-mail введён не корректно", "error");
//     $(this).addClass("errtextbox");
//     errorMail = true;
//   } else {
//     $(this).removeClass("errtextbox");
//     errorMail = false;
//   }
// });
//
// $("#password1").focusout(function(){
//   var value = $(this).val();
//   if (value.length <= 4) {
//     $(this).notify("Минимум 5 символов", "error");
//     $(this).addClass("errtextbox");
//     errorPass = true;
//   } else {
//     if (value.length > 9) {
//       $(this).notify("Миксимум 10 символов", "error");
//       $(this).addClass("errtextbox");
//       errorPass = true;
//     } else {
//       errorPass = false;
//       $(this).removeClass("errtextbox");
//     }
//   }
// });
//
// $("#password2").focusout(function(){
//   var value = $(this).val();
//   if (value != $("#password1").val()) {
//     $(this).notify("Пароль не совпадает", "error");
//     $(this).addClass("errtextbox");
//     errorPass = true;
//   } else {
//     errorPass = false;
//     $(this).removeClass("errtextbox");
//   }
// });
//
// $("#submit_register").click(function(){
//   if (!(errorNull || errorMail || errorPass)) {
//       // if (false) {
//     $("#login").submit();
//   } else {
//     $(this).notify("Форма пустая или заполнена не корректно", "error");
//   }
// });
//
// $("#submit_register").click(function (e){
//     e.preventDefault()
// });



