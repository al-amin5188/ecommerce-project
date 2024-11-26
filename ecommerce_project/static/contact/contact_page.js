// FAQ section: Toggle answers on click
document.addEventListener('DOMContentLoaded', function() {
    const questions = document.querySelectorAll('.faq-item h3');
    questions.forEach(question => {
        question.addEventListener('click', function() {
            const answer = question.nextElementSibling;
            answer.style.display = answer.style.display === 'block' ? 'none' : 'block';
        });
    });
});

// Contact Form Submission (Simple Validation)
document.getElementById('contact-form').addEventListener('submit', function(e) {
    e.preventDefault(); // Prevent form submission to server
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const message = document.getElementById('message').value;

    if (name && email && message) {
        alert('Your message has been sent successfully!');
        // Here you can implement AJAX or Django backend integration later
    } else {
        alert('Please fill out all fields.');
    }
});
