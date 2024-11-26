// open pop-up
const openPopup = document.getElementById("open-popup");
const popup = document.getElementById("popup");

openPopup.addEventListener("click", () => {
    popup.style.display = "flex";
});

// close pop-up
const closePopup = document.getElementById("close-popup");

closePopup.addEventListener("click", () => {
    popup.style.display = "none";
});

// Window click close 
window.addEventListener("click", (event) => {
    if (event.target === popup) {
        popup.style.display = "none";
    }
});


// Rating system
const ratingInputs = document.querySelectorAll('.rating input');
const ratingOutput = document.getElementById('rating-output');

ratingOutput.textContent = 'Your rating: 3 Star';
ratingInputs.forEach(input => {
    input.addEventListener('change', function() {
        const ratingValue = this.value;
        ratingOutput.textContent = `Your rating: ${ratingValue} Star`;
    });
});