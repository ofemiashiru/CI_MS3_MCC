document.addEventListener("DOMContentLoaded", function () {

    // Check passwords match
    const registerForm = document.querySelector(".register-form");

    registerForm.addEventListener("submit", function(e){
        e.preventDefault();

        let password = this.elements.password.value;
        let passwordCheck = this.elements.passwordCheck.value;

        if(password === passwordCheck){
            this.submit();
        } else {
            document.querySelector(".password-check").innerHTML = "Your passwords do not match!";
        }

    });
    
});