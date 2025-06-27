async function fetchProducts() {
    const productListDiv = document.getElementById('product-list');

    try {
        const products = await apiRequest('/products/');

        productListDiv.innerHTML = '';

        products.forEach(product => {
            const productCard = document.createElement('div');
            productCard.className = 'product-card';

            const priceInTL = (product.price / 100).toFixed(2);

            productCard.innerHTML = `
                <div class="card-content">
                    <h3>${product.name}</h3>
                    <p class="description">${product.description || 'Açıklama mevcut değil.'}</p>
                </div>
                <div class="card-footer">
                    <div class="price">${priceInTL} TL</div>
                    <button class="btn btn-icon add-to-cart-btn" data-product-id="${product.id}">
                        <i class="fas fa-cart-plus"></i>
                    </button>
                </div>
            `;

            productListDiv.appendChild(productCard);
        });

        document.querySelectorAll('.add-to-cart-btn').forEach(button => {
            button.addEventListener('click', handleAddToCart);
        });

    } catch (error) {
        console.error('Fetch error:', error);
        productListDiv.innerHTML = '<p class="error-text">Ürünler yüklenirken bir hata oluştu.</p>';
    }
}

async function handleAddToCart(event) {
    const button = event.currentTarget;
    const productId = button.dataset.productId;

    if (!auth.getToken()) {
        alert('Lütfen önce giriş yapın.');
        window.location.href = '/login';
        return;
    }

    try {
        await apiRequest('/cart/items', {
            method: 'POST',
            body: JSON.stringify({
                product_id: parseInt(productId),
                quantity: 1
            })
        });

        alert('Ürün sepete eklendi!');
        auth.updateHeader();
    } catch (error) {
        console.error('Failed to add item to cart:', error);
    }
}

fetchProducts();