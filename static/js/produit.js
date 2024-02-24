let currentImageIndex = 0;
const images = document.querySelectorAll('.product-image');
let cartContainer = document.getElementById('cart-container');
function showImage(index) {
    images.forEach((img, idx) => {
        img.style.display = idx === index ? 'block' : 'none';
    });
}

function changeImage(step) {
    currentImageIndex += step;
    if (currentImageIndex >= images.length) currentImageIndex = 0;
    if (currentImageIndex < 0) currentImageIndex = images.length - 1;
    showImage(currentImageIndex);
}

// Affichez la première image au chargement
document.addEventListener("DOMContentLoaded", () => {
    showImage(currentImageIndex);
});


function updateCartHtml(data) {

    let products = Array.isArray(data) ? data : (data.products || []);

    var cartItemsContainer = document.createElement('div');
    cartItemsContainer.className = 'cart-items';
    data.products.forEach(product => {
        var cartItemHtml = `
            <div class="cart-item">
                <div class="cart-item-image">
                    <img src="${product.images[0]}" alt="${product.name}">
                </div>
                <div class="cart-item-details">
                <h3>${product.name}</h3>
                <p>Quantité: <span id="quantity-value-${product.id}">${product.quantity}</span></p>
                <p>Prix Unité: <span id="prix-unité-${product.id}">${product.price}</span> €</p>
                <p>Prix*Quantité: <span id="prix-quantité-${product.id}">${(product.price*product.quantity).toFixed(2)}</span> €</p>
                <button onclick="decrementer_quantity(${product.id})">-</button>
                <button onclick="incrementer_quantity(${product.id})">+</button>
                <button onclick="removeFromCart(${product.id})"><i class="fas fa-trash"></i></button>
            </div>
            </div>
        `;
        cartItemsContainer.innerHTML += cartItemHtml;
    });

    var existingItemsContainer = document.querySelector('#cart-container .cart-items');
    if (existingItemsContainer) {
        existingItemsContainer.remove();
    }
    cartContainer.appendChild(cartItemsContainer);
}

document.addEventListener("DOMContentLoaded", function() {
    var cartLink = document.querySelector('.cart-link');
    var cartContainer = document.getElementById('cart-container');

    cartLink.addEventListener('click', function(event) {
        event.preventDefault();
        toggleCart();
    });

    function toggleCart() {
        cartContainer.classList.toggle('open');
        if (cartContainer.classList.contains('open')) {
            loadAndDisplayCart();
        }
    }

    function loadAndDisplayCart() {
        fetch('/cart_detail/')
            .then(response => response.json())
            .then(data => {
                updateCartHtml(data);
            })
            .catch(error => console.error('Erreur:', error));
    }

    updateCartItemCount();

    function updateCartItemCount() {
        fetch('/cart/item_count/')  
            .then(response => response.json())
            .then(data => {
                document.querySelector('.badge').innerText = data.count;
            })
            .catch(error => console.error('Error:', error));
    }


});

function toggleCart() {
    var cartContainer = document.getElementById('cart-container');
    cartContainer.classList.toggle('open');
}




function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function removeFromCart(productId) {
    const csrftoken = getCookie('csrftoken');

    fetch(`/remove_from_cart/${productId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken, // Ajoutez le token CSRF ici
        },
    })
    .then(response => {
        if(response.ok) {
            console.log('Produit retiré avec succès');
            location.reload(); // Ceci recharge la page pour refléter les changements dans le panier
        } else {
            console.error('Erreur lors de la suppression du produit');
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

function decrementer_quantity(productId) {
    const csrftoken = getCookie('csrftoken');

    fetch(`/decrementer_quantity/${productId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken, // Ajoutez le token CSRF ici
        },
    })
    .then(response => {
        if(response.ok) {
            console.log('Quantité Produit decrementer avec succès');
            return response.json();
            
            //location.reload(); 
        } else {
            console.error('Erreur lors de la decrementation du produit');
        }
    })
    .then(data => { document.querySelector(`#quantity-value-${productId}`).innerText = data.quantity; 
        document.querySelector(`#prix-unité-${productId}`).innerText = data.price;
        document.querySelector(`#prix-quantité-${productId}`).innerText = (data.price*data.quantity).toFixed(2);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}


function incrementer_quantity(productId) {
    const csrftoken = getCookie('csrftoken');

    fetch(`/incrementer_quantity/${productId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken, // Ajoutez le token CSRF ici
        },
    })
    .then(response => {
        if(response.ok) {
            console.log('Quantité Produit incrementer avec succès');
            return response.json();
            
            //location.reload(); 
        } else {
            console.error('Erreur lors de l incrementation du produit');
        }
    })
    .then(data => { document.querySelector(`#quantity-value-${productId}`).innerText = data.quantity; 
        document.querySelector(`#prix-unité-${productId}`).innerText = data.price;
        document.querySelector(`#prix-quantité-${productId}`).innerText = (data.price*data.quantity).toFixed(2);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}