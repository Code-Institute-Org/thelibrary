/**
 * Hides loading gif, giving content enough time to load before the user can see it.
 */
function hideLoader() {
    document.getElementById('loadingGifBg').style.display = 'none';
}

setTimeout(function () {
    hideLoader();
}, 600);

