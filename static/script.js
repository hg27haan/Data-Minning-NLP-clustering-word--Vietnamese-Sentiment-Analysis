document.addEventListener('DOMContentLoaded', function() {
    const commentInput = document.querySelector('textarea[name="comment_input"]');
    
    if (commentInput) {
        let generatedText = '';
        let tabPressed = false;

        commentInput.addEventListener('keydown', function(event) {
            if (event.key === 'Tab') {
                event.preventDefault();
                tabPressed = true;
            } else if (event.key === ' ') {
                tabPressed = false;
            }
        });

        commentInput.addEventListener('keyup', function(event) {
            if (event.key === 'Tab' && tabPressed) {
                event.preventDefault();
                let comment = commentInput.value.trim();
                fetch('/generate_text', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded',
                    },
                    body: new URLSearchParams({ comment: comment })
                })
                .then(response => response.json())
                .then(data => {
                    if (data.generated_text) {
                        generatedText = data.generated_text;
                        commentInput.value += generatedText;
                    }
                })
                .catch(error => console.error('Error:', error));
            }
        });
    }

    // Pagination for phone list
    const phoneList = document.querySelector('.phone-list');
    const items = document.querySelectorAll('.phone-item');
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');

    if (phoneList && items.length > 0) {
        let currentIndex = 0;
        const itemsPerPage = 5;

        function showItems() {
            const offset = -currentIndex * 100 / itemsPerPage;
            phoneList.style.transform = `translateX(${offset}%)`;
        }

        prevBtn.addEventListener('click', function() {
            if (currentIndex > 0) {
                currentIndex -= itemsPerPage;
            } else {
                currentIndex = Math.max(0, items.length - itemsPerPage);
            }
            showItems();
        });

        nextBtn.addEventListener('click', function() {
            if (currentIndex < items.length - itemsPerPage) {
                currentIndex += itemsPerPage;
            } else {
                currentIndex = 0;
            }
            showItems();
        });

        showItems();
    }
});
