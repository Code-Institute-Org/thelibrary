/**
 * 
 * @param {str} postID 
 * if user clicks confirm on confirm window, function gets the local url,
 * then redirects to the delete_post url with the postID attached.
 * Local url is needed so code will work in development and deployed site
 * @returns false if user clicks cancel on confirm window
 */
function checkDeletePost(postID) {
    let check = confirm("This will permanently delete this post, are you sure?");

    if (check) {
        let currentURL = window.location.href;
        let splitStr = currentURL.split('/');
        let url = `${splitStr[0]}//${splitStr[2]}/posts/delete/${postID}?next=${currentURL}`;
        window.location.href = url;
        return
    } else {
        return false;
    }
};

function goBack() {
    window.history.back();
}

let deleteBtns = document.getElementsByClassName('deleteBtn');

for (let i = 0; i < deleteBtns.length; i++) {
    let postID = deleteBtns[i].getAttribute('data-post-pk');
    deleteBtns[i].addEventListener('click', function () {
        checkDeletePost(postID);
    });
}

if (document.getElementById('back-btn')) {
    let backBtn = document.getElementById('back-btn');
    backBtn.addEventListener('click', function () {
        goBack();
    });
}

function checkDeleteEditorsNote(postID) {
    let check = confirm("Are you sure you want to delete this editors note?");
    if (check) {
        let currentURL = window.location.href;
        let splitStr = currentURL.split('/');
        let url = `${splitStr[0]}//${splitStr[2]}/manager/editors_note/delete/${postID}`;
        window.location.href = url;
        return
    } else {
        return false;
    }
}

let editorsNoteDeleteBtn = document.getElementById('editorsNoteDeleteBtn');

if (editorsNoteDeleteBtn) {
    editorsNoteDeleteBtn.addEventListener('click', function () {
        let postID = editorsNoteDeleteBtn.getAttribute('data-post-pk');
        checkDeleteEditorsNote(postID);
    });
}

function checkDeleteFlag(flagID) {
    let check = confirm("Are you sure you want to dismiss this flag?");
    if (check) {
        let currentURL = window.location.href;
        let splitStr = currentURL.split('/');
        let url = `${splitStr[0]}//${splitStr[2]}/manager/delete_flag/${flagID}`;
        window.location.href = url;
        return
    } else {
        return false;
    }
}

let deleteFlagBtn = document.getElementById('deleteFlag');
deleteFlagBtn.addEventListener('click', function () {
    let flagID = deleteFlagBtn.getAttribute('data-flag-id');
    checkDeleteFlag(flagID);
});