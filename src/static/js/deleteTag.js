document.addEventListener("DOMContentLoaded", function () {

    /**
     * @param {str} tagID 
     * @param {str} tagName 
     * Function to check with the user if they really want to delete the selected tag.
     * If user confirms deletion, the client is redirected to the correct URL to complete
     * the deletion.
     */
    function checkDeleteTag(tagID, tagName) {
        let check = confirm(`"This will permanently delete the '${tagName}' tag \
and remove it from any posts that it belongs to. Are you sure?"`);

        if (check) {
            let currentURL = window.location.href;
            let splitStr = currentURL.split('/');
            let url = `${splitStr[0]}//${splitStr[2]}/manager/delete_tag/${tagID}`;
            window.location.href = url;
        } else {
            return false;
        }

    }

    let deleteBtns = document.getElementsByClassName('tagDeleteBtn');

    for (let i = 0; i < deleteBtns.length; i++) {
        let tagID = deleteBtns[i].getAttribute('data-tag-id');
        let tagName = deleteBtns[i].getAttribute('data-tag-name');
        deleteBtns[i].addEventListener('click', function () {
            checkDeleteTag(tagID, tagName);
        });
    }
});