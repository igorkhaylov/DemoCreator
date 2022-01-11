const form = document.querySelector('.form')
const password1 = document.getElementById('id_new_password1')
const e1Password = document.querySelector('.password-err1')
const e2Password = document.querySelector('.password-err2')
const e3Password = document.querySelector('.password-err3')
const password2 = document.getElementById('id_new_password2')
const ePassword2 = document.querySelector('.password2')

let pass1
let pass2
let err = 0
const pas1  = /[~`!#$%\^&*+=\-\[\]\\';,/{}|\\":<>\?]/
const pas2  = /[0-9]{5,}|qwerty|q1w2e3|123asd|asd123|password|1q2w3e/

function classRemove(nameTag) {
    nameTag.classList.remove('err')
}
function showError(nameTag) {
    nameTag.classList.add('err')  
    setTimeout(classRemove,5000 ,nameTag) 
} 

password1.addEventListener('blur', (e)=>{
    pass1 = document.getElementById('id_new_password1').value
    if(pass1.length < 8){
        showError(e1Password) 
    }
    else if(! pas1.test(String(pass1))){
        showError(e2Password) 
    }
    else if(pas2.test(String(pass1))){
        showError(e3Password) 
    }
})  

    


password2.addEventListener('blur', (e)=>{
    pass1 = document.getElementById('id_new_password1').value
    pass2 = document.getElementById('id_new_password2').value
    if(pass1 != pass2){
        showError(ePassword2) 
    }

})  

form.addEventListener('submit', (e)=>{

    e.preventDefault()
    
              pass1 = document.getElementById('id_new_password1').value
            if(pass1.length < 8){
                showError(e1Password) 
                err++
            }
            else if(! pas1.test(String(pass1))){
                showError(e2Password)
                err++
            }
            else if(pas2.test(String(pass1))){
                showError(e3Password)
                err++ 
            }
        pass1 = document.getElementById('id_new_password1').value
        pass2 = document.getElementById('id_new_password2').value
        if(pass1 != pass2){
            showError(ePassword2) 
            err++
        }
    
        if(err === 0){
            document.querySelector('.form_button-submit').submit
            form.submit()
        }
        else{err=0}
    
})
