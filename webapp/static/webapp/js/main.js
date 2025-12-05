document.addEventListener('DOMContentLoaded', function() {
    loadUniversities();
});

function loadUniversities() {
    fetch('/api/universities/')
        .then(res => res.json())
        .then(data => {
            renderUniversities(data);
        })
        .catch(err => {
            console.error('Ошибка:', err);
            document.getElementById('universities-list').innerHTML = '<li>Ошибка загрузки данных</li>';
        });
}

function renderUniversities(universities) {
    const list = document.getElementById('universities-list');
    list.innerHTML = '';

    universities.forEach(uni => {
        const li = document.createElement('li');
        li.className = 'university-item';

        const scholarshipBadge = uni.scholarships ? '<span class="badge">Стипендии </span>' : '';
        const internshipBadge = uni.internships ? '<span class="badge">Стажировки </span>' : '';

        li.innerHTML =

            '<img src="' + uni.image_url + '" alt="' + uni.name + '">' +
            '<h3><a href="/university/' + uni.id + '/">' + uni.name + '</a></h3>' +
            '<p>' + uni.description + '</p>' +
            '<div class="info">' +
                '<p><strong>Город:</strong> ' + uni.city + '</p>' +
                '<p><strong>Мин. балл ЕНТ:</strong> ' + uni.min_unt_score + '</p>' +
                '<p><strong>Стоимость обучения:</strong> ' + uni.tuition_fee + ' ₸</p>' +
                scholarshipBadge + internshipBadge +
            '</div>';

        list.appendChild(li);
    });
}