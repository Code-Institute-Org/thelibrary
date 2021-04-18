let deleteBtns = document.getElementsByClassName('deleteBtn');
let postID = deleteBtns[0].getAttribute('data-post-pk');

for (let i = 0; i < deleteBtns.length; i++) {
    deleteBtns[i].addEventListener('click', function () {
        checkDelete(postID);
    });
}

/**
 * 
 * @param {str} postID 
 * if user clicks confirm on confirm window, function gets the local url,
 * then redirects to the delete_post url with the postID attached.
 * Local url is needed so code will work in development and deployed site
 * @returns false if user clicks cancel on confirm window
 */
function checkDelete(postID) {
    let check = confirm("This will permanently delete your post, are you sure?");

    if (check) {
        let currentURL = window.location.href;
        let splitStr = currentURL.split('posts/');
        let url = splitStr[0] + 'posts/delete/' + postID;
        window.location.href = url;
        return
    } else {
        return false
    }
};
