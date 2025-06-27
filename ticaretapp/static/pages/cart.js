async function fetchCart() {
    const cartContainer = document.getElementById('cart-container');
    if (!auth.getToken()) {
        cartContainer.innerHTML = '<p>Sepetinizi görmek için lütfen <a href="/login">giriş yapın</a>.</p>';
        return;
    }

    try {
        const cart = await apiRequest('/cart');

        if (cart.items.length === 0) {
            cartContainer.innerHTML = '<p>Sepetiniz boş.</p>';
            return;
        }

        let cartHTML = '<ul>';
        let subtotal = 0;

        cart.items.forEach(item => {
            const itemPrice = (item.product.price / 100).toFixed(2);
            subtotal += item.product.price * item.quantity;
            cartHTML += `
                <li class="cart-item">
                    <div class="cart-item-details">
                        <span class="cart-item-title">${item.product.name}</span>
                        <span class="cart-item-price">${item.quantity} x ${itemPrice} TL</span>
                    </div>
                    <button class="btn btn-icon" onclick="removeFromCart(${item.product.id})">
                        <i class="fas fa-trash"></i>
                    </button>
                </li>
            `;
        });
        cartHTML += '</ul>';

        const shippingCost = 8000;
        const total = subtotal + shippingCost;

        cartHTML += `
            <div class="cart-summary">
                <div class="summary-row">
                    <span>Ara Toplam:</span>
                    <span>${(subtotal / 100).toFixed(2)} TL</span>
                </div>
                <div class="summary-row">
                    <span>Kargo Ücreti:</span>
                    <span>${(shippingCost / 100).toFixed(2)} TL</span>
                </div>
                <div class="summary-row summary-total">
                    <span>TOPLAM:</span>
                    <span>${(total / 100).toFixed(2)} TL</span>
                </div>
                <button class="btn btn-primary" style="width: 100%; margin-top: 1rem;">Siparişi Tamamla (Fake)</button>
            </div>
        `;

        cartContainer.innerHTML = cartHTML;

    } catch (error) {
        cartContainer.innerHTML = '<p class="error-text">Sepet yüklenirken bir hata oluştu.</p>';
    }
}

async function removeFromCart(productId) {
    if (!confirm('Bu ürünü sepetten kaldırmak istediğinize emin misiniz?')) return;

    try {
        await apiRequest(`/cart/items/${productId}`, { method: 'DELETE' });
        fetchCart();
        auth.updateHeader();
    } catch (error) {
        console.error('Failed to remove item:', error);
    }
}

fetchCart();