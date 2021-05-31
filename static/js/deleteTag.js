document.addEventListener("DOMContentLoaded", function () {

    function checkDeleteTag(tagID) {
        let check = confirm("This will permanently delete this tag \
and remove it from any posts that it belongs to. Are you sure?");

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
        deleteBtns[i].addEventListener('click', function () {
            checkDeleteTag(tagID);
        });
    }
})