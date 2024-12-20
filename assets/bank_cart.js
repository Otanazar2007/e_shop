document.getElementById('card-form').addEventListener('submit', function(event) {
    event.preventDefault();

    // Очистка старых ошибок
    document.querySelectorAll('.error-message').forEach(msg => (msg.style.display = 'none'));

    const cardNumber = document.getElementById('card-number').value.trim();
    const cardName = document.getElementById('card-name').value.trim();
    const expiryDate = document.getElementById('expiry-date').value.trim();
    const cvv = document.getElementById('cvv').value.trim();

    let isValid = true;

    // Валидация номера карты
    if (!/^\d{16}$/.test(cardNumber)) {
        const error = document.getElementById('card-number-error');
        error.textContent = 'Номер карты должен содержать ровно 16 цифр.';
        error.style.display = 'block';
        isValid = false;
    }

    // Валидация имени на карте
    if (cardName.length === 0) {
        const error = document.getElementById('card-name-error');
        error.textContent = 'Введите имя на карте.';
        error.style.display = 'block';
        isValid = false;
    }

    // Валидация срока действия карты
    if (!/^(0[1-9]|1[0-2])\/\d{2}$/.test(expiryDate)) {
        const error = document.getElementById('expiry-date-error');
        error.textContent = 'Введите срок действия в формате MM/YY.';
        error.style.display = 'block';
        isValid = false;
    }

    // Валидация CVV
    if (!/^\d{3}$/.test(cvv)) {
        const error = document.getElementById('cvv-error');
        error.textContent = 'CVV должен содержать ровно 3 цифры.';
        error.style.display = 'block';
        isValid = false;
    }

    if (isValid) {
        // Собираем данные
        const data = {
            cardNumber: cardNumber,
            cardName: cardName,
            expiryDate: expiryDate,
            cvv: cvv
        };

        // Отправка данных на сервер
        fetch('/bank_cart/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken') // CSRF токен для защиты
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(data => {
            // Ответ от сервера
            if (data.status === 'success') {
                alert('Оплата прошла успешно!');
                window.location.href = '/bank_cart_right'; // Перенаправление на успешную страницу
            } else {
                alert('Ошибка: ' + data.message);
            }
        })
        .catch(error => {
            console.error('Ошибка при отправке данных:', error);
            alert('Произошла ошибка при оплате.');
        });
    }
});

// Функция для получения CSRF токена из cookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
