document.addEventListener('DOMContentLoaded', () => {
    if (auth.getToken()) {
        window.location.href = '/';
        return;
    }

    const loginForm = document.getElementById('login-form');
    const errorMessageDiv = document.getElementById('error-message');

    loginForm.addEventListener('submit', async (event) => {
        event.preventDefault();

        const formData = new URLSearchParams();
        formData.append('username', document.getElementById('email').value);
        formData.append('password', document.getElementById('password').value);

        try {
            const response = await fetch('/api/token', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: formData,
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.detail || 'Giriş yapılamadı.');
            }

            const data = await response.json();

            auth.setToken(data.access_token);

            window.location.href = '/';

        } catch (error) {
            errorMessageDiv.textContent = `Hata: ${error.message}`;
            errorMessageDiv.style.display = 'block';
        }
    });
});