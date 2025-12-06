document.addEventListener('DOMContentLoaded', function() {
    const token = localStorage.getItem('access_token');
    if (!token) {
        window.location.href = '/login/';
        return;
    }

    loadUserProfile();
});

function loadUserProfile() {
    const token = localStorage.getItem('access_token');
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    console.log('Отправляю:', { username, password });

    fetch('/accounts/', {
        headers: {
            'Authorization': 'Bearer ' + token
        }
    })
        .then(res => {
            if (res.status === 401) {
                // Токен невалиден - редирект на логин
                localStorage.removeItem('access_token');
                localStorage.removeItem('refresh_token');
                window.location.href = '/login/';
                return;
            }
            return res.json();
        })
        .then(data => {
            if (data) {
                renderUserProfile(data);
            }
        })
        .catch(err => {
            console.error('Ошибка загрузки профиля:', err);
        });
}

function renderUserProfile(user) {
    document.getElementById('user-avatar').textContent =
        user.first_name ? user.first_name[0].toUpperCase() : user.username[0].toUpperCase();

    document.getElementById('user-name').textContent =
        user.first_name && user.last_name
            ? user.first_name + ' ' + user.last_name
            : user.username;

    document.getElementById('user-email').textContent = user.email;

    document.getElementById('profile-first-name').textContent = user.first_name || '-';
    document.getElementById('profile-last-name').textContent = user.last_name || '-';
    document.getElementById('profile-email').textContent = user.email;

    const dateJoined = new Date(user.date_joined);
    document.getElementById('profile-date-joined').textContent = dateJoined.toLocaleDateString('ru-RU');
}