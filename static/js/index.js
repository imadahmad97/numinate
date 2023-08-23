document.addEventListener("DOMContentLoaded", function() {
    const btn = document.querySelector('.button-37');
    const doneText = document.getElementById('doneText');

    btn.addEventListener('click', function() {
        // Add the fade-out class to start the animation
        btn.classList.add('fade-out');

        // After the animation completes, hide the button and show the Done text
        setTimeout(function() {
            btn.style.display = 'none';
            doneText.style.display = 'inline';
        }, 400);  // 400ms is the duration of the transition
    });
});
