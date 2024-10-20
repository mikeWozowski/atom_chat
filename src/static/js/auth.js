document.addEventListener("DOMContentLoaded", function() {
    const toggleButton = document.getElementById("toggle-form");
    const registerForm = document.getElementById("register-form");
    const loginForm = document.getElementById("login-form");

    toggleButton.addEventListener("click", function() {
        if (registerForm.style.display === "none") {
            registerForm.style.display = "block";
            loginForm.style.display = "none";
            toggleButton.textContent = "Переключить на Вход";
        } else {
            registerForm.style.display = "none";
            loginForm.style.display = "block";
            toggleButton.textContent = "Переключить на Регистрацию";
        }
    });
});