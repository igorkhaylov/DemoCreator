const form = document.querySelector('.form')
const firstName = document.getElementById('id_first_name')
const eFirstName = document.querySelector('.first_name')
const lastName = document.getElementById('id_last_name')
const eLastName = document.querySelector('.last_name')
const email = document.getElementById('id_email')
const eEmail = document.querySelector('.email')
const username = document.getElementById('id_username')
const eUsername = document.querySelector('.username')
const password1 = document.getElementById('id_new_password1')
const e1Password = document.querySelector('.password-err1')
const e2Password = document.querySelector('.password-err2')
const e3Password = document.querySelector('.password-err3')
const password2 = document.getElementById('id_new_password2')
const ePassword2 = document.querySelector('.password2')
const loginPassword = document.getElementById('id_password')
const eLoginPassword = document.querySelector('.password')


let pass1
let pass2
let val
let err = 0
const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
const pas1  = /[~`!#$%\^&*+=\-\[\]\\';,/{}|\\":<>\?]/
const pas2  = /[0-9]{5,}|qwerty|q1w2e3|123asd|asd123|password|1q2w3e/
function classRemove(nameTag) {
    nameTag.classList.remove('err')
}
function showError(nameTag) {
    
    nameTag.classList.add('err')  
    setTimeout(classRemove,5000 ,nameTag) 
    err++
} 
function Blur(nameInput,nameErr ,functionName,nameErr2,nameErr3) {
    if(nameInput){nameInput.addEventListener('blur',()=>{
    functionName(nameInput,nameErr,nameErr2,nameErr3)
    })}
}
function checkInput(nameInput,nameErr) {
    if(nameInput ){ 
        if(document.getElementById(nameInput.id).value == ""){
            showError(nameErr) 
        }
    }
    
}

function checkEmail(nameInput,nameErr) {
    if(nameInput){
        val = document.getElementById(nameInput.id).value
        if(! re.test(String(val).toLowerCase())){   
            showError(nameErr)          
        }
    }  
}




function checkPassword1(nameInput,nameErr1, nameErr2,nameErr3) {
    if(nameInput){
        pass1 = document.getElementById(nameInput.id).value
        if(pass1.length < 8){
            showError(nameErr1) 
        }
        else if(! pas1.test(String(pass1))){
            showError(nameErr2)
        }
        else if(pas2.test(String(pass1))){
            showError(nameErr3)
        }
      }
    
}function checkPassword2(nameInput,nameErr1, nameErr2,nameErr3) {
    if(nameInput){
        pass1 = document.getElementById('id_new_password1').value
        pass2 = document.getElementById('id_new_password2').value
        if(pass1 != pass2){
            showError(nameErr1) 
        }
      
      }
    
}







Blur(firstName,eFirstName , checkInput)
Blur(lastName,eLastName , checkInput)
Blur(email,eEmail,checkEmail)
Blur(username, eUsername,checkInput)
Blur(loginPassword,eLoginPassword,checkInput)
Blur(password1,e1Password,checkPassword1,e2Password,e3Password)
Blur(password2,ePassword2,checkPassword2)


if(form){  form.addEventListener('submit', (e)=>{
    e.preventDefault()
    err = 0
    
    checkInput(firstName,eFirstName )
    checkInput(lastName,eLastName  )
    checkEmail(email,eEmail)
    checkInput(username, eUsername )
    checkInput(loginPassword,eLoginPassword )
    checkPassword1(password1,e1Password,e2Password,e3Password)
    checkPassword2(password2,ePassword2)
    
        if(err === 0){
            form.submit()
        }
        else{ err = 0 }
    
})

}


