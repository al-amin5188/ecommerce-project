// Popup Elements
const popupModal = document.getElementById('popup-modal');
const openPopup = document.getElementById('open-popup');
const closePopup = document.getElementById('close-popup');

// Open Popup
openPopup.addEventListener('click', function () {
    popupModal.style.display = 'flex';
});

// Close Popup
closePopup.addEventListener('click', function () {
    popupModal.style.display = 'none';
});

// Close Popup on Outside Click
window.addEventListener('click', function (e) {
    if (e.target === popupModal) {
        popupModal.style.display = 'none';
    }
});


// Image Preview Function
function previewImage(event) {
    const file = event.target.files[0];
    const reader = new FileReader();
    reader.onload = function () {
        const image = document.getElementById('profile-pic-preview');
        image.src = reader.result;
    };
    reader.readAsDataURL(file);
}