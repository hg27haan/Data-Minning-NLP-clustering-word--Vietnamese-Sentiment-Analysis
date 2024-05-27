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
});
