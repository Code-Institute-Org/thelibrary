/**
 * Hides loading gif, giving content enough time to load before the user can see it.
 */
function hideLoader() {
    document.getElementById('loadingGifBg').style.display = 'none';
}

setTimeout(function () {
    hideLoader();
}, 600);


/**
 * Function sets a local storage value to remember
 * the user has dismissed the sales banner. This then prevents the
 * banner from being shown again on other pages.
 * @param {event} e 
 */
function rememberClosed(e) {
    e.preventDefault();

    localStorage.setItem("salesBannerDismissed", true);
}


// Checks if sales-banner element exists, 
// if it does: applies rememberClosed click event listener
if (document.getElementById('sales-banner')) {
    let salesBanner = document.getElementById('sales-banner');

    salesBanner.addEventListener('click', rememberClosed);
}

// Removes sales-banner it exists, and salesBannerDismissed value is in local storage.
if (localStorage.getItem('salesBannerDismissed') && document.getElementById('sales-banner')) {
    document.getElementById('sales-banner').remove();
}