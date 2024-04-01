document.addEventListener('DOMContentLoaded', function() {
    var card = document.querySelector('.card-content');
    var drawButton = document.getElementById('draw-card-button');
    var resetButton = document.getElementById('reset-button');
    var cardImage = document.getElementById('card-image');

    drawButton.addEventListener('click', function() {
        if (!card.classList.contains('card-flipped')) {
            fetch('/gold/draw-card/')  // 카드 데이터를 가져올 URL
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                if (data.error) {
                    alert('카드를 뽑을 수 없습니다.');
                } else {
                    // 카드 앞면을 뒤집어서 뒷면을 보이게 합니다.
                    card.classList.add('card-flipped');

                    // 가져온 데이터로 제목과 내용을 설정합니다.
                    document.querySelector('.card-title').textContent = data.title;
                    document.querySelector('.card-text').textContent = data.content;

                    // 이미지를 변경합니다.
                    cardImage.src = "/static/image2.PNG"; // 이미지 경로를 하드코딩합니다.
                }
            })
            .catch(error => {
                alert('오류가 발생했습니다.');
                console.error('Error:', error);
            });
        }
    });

    resetButton.addEventListener('click', function() {
        // 카드 뒷면을 앞면으로 되돌립니다.
        card.classList.remove('card-flipped');

        // 제목과 내용을 초기화합니다.
        document.querySelector('.card-title').textContent = '';
        document.querySelector('.card-text').textContent = '';

        // 이미지를 초기 이미지로 변경합니다.
        cardImage.src = "/static/image.PNG"; // 이미지 경로를 하드코딩합니다.
    });
});
