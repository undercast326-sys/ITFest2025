document.addEventListener('DOMContentLoaded', function() {
    loadUniversityDetail();
});

function loadUniversityDetail() {
    fetch('/api/universities/' + universityId + '/')
        .then(res => res.json())
        .then(data => {
            renderUniversityDetail(data);
        })
        .catch(err => {
            console.error('Ошибка:', err);
            document.getElementById('loading').innerHTML = 'Ошибка загрузки данных';
        });
}

function renderUniversityDetail(uni) {
    document.getElementById('loading').style.display = 'none';
    const content = document.getElementById('university-content');
    content.style.display = 'block';

    const scholarshipBadge = uni.scholarships ? '<span class="badge">Стипендии</span>' : '';
    const internshipBadge = uni.internships ? '<span class="badge">Стажировки</span>' : '';

    content.innerHTML =
        '<div class="university-detail">' +
            '<div class="university-header">' +
                '<img src="' + uni.image_url + '" alt="' + uni.name + '" class="university-image">' +
                '<div class="university-info">' +
                    '<h1>' + uni.name + '</h1>' +
                    '<p>' + uni.description + '</p>' +
                    '<div>' +
                        scholarshipBadge +
                        internshipBadge +
                    '</div>' +
                '</div>' +
            '</div>' +

            '<div class="info-grid">' +
                '<div class="info-card">' +
                    '<h3>Город</h3>' +
                    '<p>' + uni.city + '</p>' +
                '</div>' +
                '<div class="info-card">' +
                    '<h3>Минимальный балл ЕНТ</h3>' +
                    '<p>' + uni.min_unt_score + '</p>' +
                '</div>' +
                '<div class="info-card">' +
                    '<h3>Стоимость обучения</h3>' +
                    '<p>' + uni.tuition_fee + ' ₸</p>' +
                '</div>' +
                '<div class="info-card">' +
                    '<h3>Тип университета</h3>' +
                    '<p>' + uni.type.name + '</p>' +
                '</div>' +
            '</div>' +

            '<div class="section">' +
                '<h2>Языки обучения</h2>' +
                '<p>' + uni.languages + '</p>' +
            '</div>' +
        '</div>';
}