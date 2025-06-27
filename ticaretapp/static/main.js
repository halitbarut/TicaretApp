async function apiRequest(url, options = {}) {
    const token = auth.getToken();
    const headers = {
        'Content-Type': 'application/json',
        ...options.headers,
    };

    if (token) {
        headers['Authorization'] = `Bearer ${token}`;
    }

    try {
        const response = await fetch(`/api${url}`, { ...options, headers });

        if (!response.ok) {
            if (response.status === 401) {
                alert("Oturumunuzun süresi doldu veya geçersiz. Lütfen tekrar giriş yapın.");
                auth.clearToken();
                window.location.href = '/login';
                throw new Error("Session expired");
            }

            const errorData = await response.json().catch(() => null);
            const errorMessage = errorData?.detail || `Sunucudan bir hata döndü: ${response.statusText} (${response.status})`;
            throw new Error(errorMessage);
        }

        if (response.status === 204) {
            return null;
        }

        return response.json();

    } catch (error) {
        console.error('API Request Error:', error.message);
        throw error;
    }
}