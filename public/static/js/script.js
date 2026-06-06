function moreinfo_closePopup() {
    document.getElementById('moreinfo_popup').style.display = 'none';
}

document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.moreinfo_button').forEach(function (button) {
        button.addEventListener('click', function () {
            var productId = this.getAttribute('data-id');
            var fileName = this.getAttribute('data-file');
            fetch('/product-details/' + productId + '/' + fileName + '/')
                .then(function (response) { return response.json(); })
                .then(function (data) {
                    document.getElementById('popup-image').src =
                        'public/static/media/' + fileName + '/' + productId + '/pic1.jpg';
                    document.getElementById('popup-name').textContent = data.title_fa;
                    document.getElementById('popup-attributes').textContent = data.attributes || '';
                    document.getElementById('popup-digikalapage').href = data.image_link || '#';
                    document.getElementById('moreinfo_popup').style.display = 'block';
                })
                .catch(function (err) { console.error('Error loading product details:', err); });
        });
    });
});
