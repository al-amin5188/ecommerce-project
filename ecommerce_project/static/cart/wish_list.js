// Function to check if the wishlist is empty
function checkWishlist() {
    const wishlistItems = document.getElementById('wishlist-items').children;
    const emptyWishlistMessage = document.getElementById('empty-wishlist');
    
    if (wishlistItems.length === 0) {
        emptyWishlistMessage.style.display = 'block';
    } else {
        emptyWishlistMessage.style.display = 'none';
    }
}

// Remove item from wishlist
function removeFromWishlist(event) {
    const item = event.target.closest('.wishlist-item');
    item.remove();
    checkWishlist(); // Recheck if wishlist is empty
}

// Event listeners for Remove buttons
const removeButtons = document.querySelectorAll('.remove-btn');
removeButtons.forEach(button => {
    button.addEventListener('click', removeFromWishlist);
});

// Call the checkWishlist function to display the empty message if needed
checkWishlist();
