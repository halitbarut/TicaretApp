function logout() {
    auth.clearToken();
    window.location.href = '/login';
}

const auth = {
    getToken: () => localStorage.getItem('accessToken'),
    setToken: (token) => localStorage.setItem('accessToken', token),
    clearToken: () => localStorage.removeItem('accessToken'),

    updateHeader: async () => {
        const token = auth.getToken();
        const userInfoDiv = document.getElementById('user-info');
        const cartCountSpan = document.getElementById('cart-item-count');

        if (token) {
            try {
                const userData = await apiRequest('/users/me');
                const cartData = await apiRequest('/cart');

                userInfoDiv.innerHTML = `
                    <span class="user-email">${userData.email}</span>
                    <button onclick="logout()" class="btn-logout">Çıkış Yap</button>
                `;
                cartCountSpan.textContent = cartData.items.length;

            } catch (error) {
                console.error('Failed to fetch user/cart data:', error.message);
                userInfoDiv.innerHTML = '<a href="/login">Giriş Yap</a>';
                cartCountSpan.textContent = '0';
            }
        } else {
            userInfoDiv.innerHTML = '<a href="/login">Giriş Yap</a>';
            cartCountSpan.textContent = '0';
        }
    }
};

document.addEventListener('DOMContentLoaded', auth.updateHeader);