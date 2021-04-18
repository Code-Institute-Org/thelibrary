let deleteBtns = document.getElementsByClassName('deleteBtn');
let postID = deleteBtns[0].getAttribute('data-post-pk');

for (let i = 0; i < deleteBtns.length; i++) {
    deleteBtns[i].addEventListener('click', function () {
        let ask = confirm("This will permanently delete your post, are you sure?");
        let currentURL = window.location.href;
        let splitStr = currentURL.split('posts/');
        let url = splitStr[0] + 'posts/delete/' + postID;
        window.location.href = url;
    });
}