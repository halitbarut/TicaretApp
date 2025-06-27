document.addEventListener('DOMContentLoaded', () => {
    if (auth.getToken()) {
        window.location.href = '/';
        return;
    }

    const registerForm = document.getElementById('register-form');
    const messageBox = document.getElementById('message-box');

    registerForm.addEventListener('submit', async (event) => {
        event.preventDefault();

        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;

        messageBox.style.display = 'none';
        messageBox.textContent = '';
        messageBox.className = 'message-box';

        try {
            await apiRequest('/users/', {
                method: 'POST',
                body: JSON.stringify({
                    email: email,
                    password: password
                })
            });

            messageBox.textContent = 'Hesabınız başarıyla oluşturuldu! Giriş sayfasına yönlendiriliyorsunuz...';
            messageBox.classList.add('success-box');
            messageBox.style.display = 'block';

            setTimeout(() => {
                window.location.href = '/login';
            }, 2000);

        } catch (error) {
            messageBox.textContent = `Kayıt başarısız: ${error.message}`;
            messageBox.classList.add('error-box');
            messageBox.style.display = 'block';
        }
    });
});