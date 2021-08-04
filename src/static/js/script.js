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
 * Source: https://www.sohamkamani.com/blog/javascript-localstorage-with-ttl-expiry/#full-example
 * @param {obj} e
 */
function setDismissedWithExpiry(e) {
    e.preventDefault();

    const now = new Date();

    const dismissedData = {
        value: true,
        expiry: now.getTime() +  (1000 * 60 * 60 * 24 * 14)  // 2 weeks
    };
    localStorage.setItem("dismissedData", JSON.stringify(dismissedData));
}


/**
 * Checks if dismissedData exists in localStorage,
 * if it does, checks if current date is within registered expiry date.
 * If beyond expiry date, removes localStorage data and returns null.
 * If within expiry date, returns the value of the data so JS knows to
 * hide the sales banner from this user.
 * @returns value of dismissedData object
 */
function getDismissedDataWithExpiry() {
    const itemStr = localStorage.getItem('dismissedData');

    // If data doesn't exist, return null
    if (!itemStr) {
        return null;
    }
    const dismissedDataStr = JSON.parse(itemStr);
    const now = new Date();

    // compare expiry time with current time
    if (now.getTime() > dismissedDataStr.expiry) {
        // If the time is expired, delete data from storage
        localStorage.removeItem('dismissedData');
        return null;
    }

    return dismissedData.value;
}

// Checks if sales-banner element exists, 
// if it does: applies rememberClosed click event listener
if (document.getElementById('sales-banner')) {
    let salesBanner = document.getElementById('sales-banner');

    salesBanner.addEventListener('click', setDismissedWithExpiry);
}


// Removes sales-banner it exists, and salesBannerDismissed value is in local storage.
if (getDismissedDataWithExpiry() && document.getElementById('sales-banner')) {
    document.getElementById('sales-banner').remove();
}
