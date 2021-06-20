# The Library

A hobby project to create a library of community generated resources. Built with Django.

## User Stories

### CI students
1. As a CI student, I want to be able to log into The Library using my Slack account, so that the authentication system is smooth and easy for me.
- Site login should work through Slack accounts.
- Only CI students who have a slack account should be able to log into The Library.
2. As a CI student, I want to be able to easily find posts in the library relevant to the course that I am on.
- Search results should be labelled clearly when posts are specific to one course.
3. As a CI student, I want to be able to ask questions about the posts in the library, so that i can clear up any confusion I may still have.
- Post detail pages should include a link back to the relevant slack channel, so students can ask questions about the post in Slack.
4. As a CI student, I want to be able to share posts from the library back into slack
- Post urls should include title in the slug, making it clear what the post is about to the community.
5. As a CI student, I want to be able to bookmark posts, so that I can come back to the ones I find most useful.
- Post detail page should include bookmark button
6. As a CI student, I want to sort my bookmarks so I can find what I am looking for easily.
- Bookmarks page should include ability to sort by most recent, title, author and category

### Authors
1. As a CI student author, I want to be able to create posts, so other students can benefit from the things I have learned on the course.
2. As an author, I want to be able to edit my post content using a rich text editor, so I have control over how my post looks, add code blocks etc. 
- Create and edit post pages should include rich text editor for creating the body of the post.
3. As an author, I want to embed YouTube videos directly into my post.
- Site should be able to collect YouTube links, retrieve the relevant ID and embed the correct video into the post.
4. As an author, I want to add images to my posts so that I can share visual media to improve my content.
- Post detail page should display up to 4 images
5. As a regular CI student author, I want my contributions to be recognized, so that other students can see that I am a regular content creator.
- Site should display kudos badges of different levels (bronze, silver, gold) for authors who create more posts.
- Kudos badges should appear with author information in search results, post detail and profile pages.
6. As a CI student author, I want to have a profile where I can share useful information about myself, so that I can connect with other students and show off my posts to potential employers.
- Site should include author profile page.
- Users should be able to add an image to their profile
- Profile page should include ability to add links to linkedin and github profiles.
- Profile page should include short bio for author
- Profile page should include kudos badge
- Profile page should include badge for library moderators
- Profile page should include list of posts created by that author.
7. As a new author, I want to understand the post submissions process, so that I am not confused why my post has not been published immediately.
- Site should include alerts to explain when a post as been submitted it is waiting for review.
- Site should email new authors when they submit their post, with a clear and easy to understand explanation of what the process is and what the next steps are for them.
8. As a post author, I want to be notified when my posts status changes.
- Site should email authors when posts are published
- Site should email authors when posts are put into review (either because of a post flag, or a requested change during the moderation process.)
- Site should include in-app notifications for authors for posts in review.
9. As a post author, I want to be able to find a list of all my posts and see essential data about them, so that I can read/update/delete my posts easily.
- Site should include dashboard view with table of relevant post data.
10. As a post author, I want other users to be able to like my posts, so that my best posts are visible to other users.
- Users should be able to like and unlike posts.
11. As a post author, I want to be able to read moderator messages if my post has been put into review, so that I can make the necessary changes to get it published again.
- Post review page should include moderator message for author.



### General users (not necessarily logged in)
1. As a general user of the Library, I want to be able to search through posts using relevant keywords, tags and categories, so that I can find other relevant and useful posts.
- Site should include post categories, and the ability to filter and search those categories.
- Search functionality should order results by relevance
- Post list views should display the category that each post belongs to, with a clickable link to view all other posts in that category.
- Post detail pages should include a list of clickable tags so that users can see other posts with the same tag on them.
2. As a reader of a CI library post, I want to be able to zoom into images to see them in more detail
- Post detail page should include lightbox option to view post images.
3. As a reader of a CI library post, I want to be able to interact with any embedded YouTube videos so that i can pause, stop, play the video as I need to.
- Post videos should be embedded with controls
4. As a visitor to The Library who has not heard of CI before, I want to be able to learn more about CI, so that I might join the student sales funnel.
- Footer text should encourage new visitors to visit the main CI marketing site, and include a link to it. 
5. As potential new student, I want to get an idea of the student community and support available to students, so that I can decide if I want to sign up for the course.
- Site should be visually in line with CI brand
- Site should be professional, easy to navigate and intuitive for new users.
6. As a general user, I want my search results to be paginated, so that the page loads at a reasonable speed, improving user experience.
- All list view pages should be paginated. 
7. As a general user, I want to view when a post was most recently updated, so I can tell quickly if a post might be out of date.
- Post detail page should include date when post was published, and date post was updated (where applicable)
8. As a general user, I want to be able to see when posts are popular, so that I can feel I can trust the content available to me.
- Like functionality should be included for posts
9. As a general user, I want to be able to explore other relevant posts, so that I can keep exploring the library.
- Post detail pages should include links to other relevant posts in the side panel.
10. As a general user, I want to understand the difference between the different courses that CI offers, so that I can be sure I am looking at content relevant to me.
- Site should include a modal that pops up on clicking a "what's this" button. With clear info on the difference between the P4 and P5 courses anywhere they are referenced in search results and individual posts.


### Staff users
1. As a CI staff member, I want to be able to skip the moderation process for posts so that my posts are published instantly.
- Users who are staff should skip moderation process for new posts
2. As a CI staff member, I want the CI logo to show next to my username within the app, so that I am easily identifiable as a staff member.
- CI logo should display next to users who have is_staff = True in the UserProfile 

### Moderator users
1. As a moderator, I want to get a notification when new posts are waiting for review so that I can review them in a timely manner.
- Site should include a notification for moderators when new posts are waiting for review.
2. As a moderator, I want to be able to manage my notification settings between in-app or email notifications so that I can manage how often I am contacted to moderate content.
- Site should include a moderator manager panel that allows mods to choose email or in-app only notifications.
3. As a moderator, I want to be able to view everything I need to review in one place, so I can be sure I have checked everything before approval.
- Review page should include preview of the search results card as well as the full posts for moderators.
4. As a moderator, I want my status to be visible, so that other users are aware of my contribution to the library.
- Site should display badge for users who are moderators.

### Admin users
1. As a CI Library Admin, I want to be able to review flagged posts so that I can ensure the library content remains good quality.
- Post detail pages should include a flag button
- Post flags should have options for inappropriate, incorrect and outdated content
- Post flags should include text field for flaggers to explain in detail why they are flagging a post.
- Admins should be able to dismiss flags
- Admins should be able to put posts into review and request changes to the post
2. As a CI Library Admin, I want to be able to add an editors note above posts, so that I can inform users of any specific things they need to be aware of in the post. Without actually editing the post itself.
- Editors note option should be available for Admins on post detail pages.
- Admins should be able to add, edit and delete editors note.
- Editors note should be displayed in an obvious place above the actual post.
3. As a CI Library Admin, I want CRUD options for post categories, tags and slack channels to the library database, so that new course changes can be easily reflected in the library app.
- Site should include admin pages to edit and add categories and slack channels.
- Site should include admin pages to edit, add and delete post tags.
4. As a CI library admin, I want to be able to search users so that I can adjust their moderator, staff and admin status.
- Site should include admin pages to search users by username, first or last name.
- Admins should be able to change user profile status of users for is_staff is_mod and is_admin
5. As a CI library admin, I want the moderators to be notified when new posts are submitted, so that posts are reviewed and published in a timely manner.
- Site should notify moderators in-app and by email when new posts are waiting for review
- Site should send email notifications once a day, with a list of posts waiting for review and a button to take the moderator to the review posts pg.

## UX/UI design
### Wireframes
- [Home page](https://ibb.co/8MMzCmz)
- [List view for posts](https://ibb.co/T0SdJtX)
- [Create and Edit post page](https://ibb.co/JFvpZph)
- [Post detail](https://ibb.co/cT71jt4)
- [Settings](https://ibb.co/L8HX30s)
- [Author profile](https://ibb.co/PQkPZCS)
- [Your profile](https://ibb.co/nzqbBJ2)

## Setting up project

### Project requirements
- Python 3
- Git

## Technologies Used


### Tools

- [Pillow](https://pillow.readthedocs.io/en/stable/) as python imaging library to aid in processing image files to store in the database.
### Libraries

- [Bootstrap](https://getbootstrap.com/) to simplify the structure of the website and make the website responsive easily.

## Credits

### code
- Code to animate notification bell in the navbar by [Fazlur Rahman](https://codepen.io/fazlurr/pen/xeXpqx)
- Code to handle pagination in function based views from [simpleisbetterthancomplex.com](https://simpleisbetterthancomplex.com/tutorial/2016/08/03/how-to-paginate-with-django.html)
- Code to create triangle in post card corners for course indication from [This stack overflow post](https://stackoverflow.com/questions/18531959/how-to-create-triangle-shape-in-the-top-right-angle-of-another-div-to-look-divid)
- Loading spinner code from [W3Schools](https://www.w3schools.com/howto/howto_css_loader.asp) 

### images
- Library background image by [mentatdgt on Pexels.com](https://www.pexels.com/photo/library-photo-1319854/)

## Testing

### solved bugs
1. **z-index was not working on absolute positioned elements, causing user avatars on list view cards to overlap the menu dropdown options.**
- Issue was solved by adding position: relative; to the navbar and then adding a z-index of 99.
- Solution found in this post on [Stack Overflow](https://stackoverflow.com/questions/16315125/position-absolute-has-greater-z-index-than-position-fixed)

2. **Adding the `selected` attribute to the category `<option>` elements, conditional on which value was in the kwargs was not working.**

```html
{% if category.pk == category_pk %}selected{% endif %}
```
- When printing `{{ category.pk }}` and `{{ category_pk }}` to the template, they were printing as the same. However the comparison of the two with `==` was not evaluating to True. 
- After some digging I realized that one was a string and the other was an int. Using the `stringformat` filter fixed the problem:
```html
{% if category.pk|stringformat:"i" == category_pk %}selected{% endif %}
```

3. **In the EditPostView, saving instances of PostTag to the tags ManyToManyField was throwing an error, despite the code actually working.** 
- Full details, and the solution can be found in this [Stack Overflow Post](https://stackoverflow.com/questions/67391651/saving-instances-of-model-to-manytomany-field-thows-attributeerror-post-object)

4. **If statement in ReviewPostView to allow the author to view this page even when they are not a mod not working**

- Despite these values being identical in the terminal:
```python
# code
print(user)
print(post.author.user)
print(type(user))
print(type(post.author.user))
```
```
# terminal output:
username
username
<class 'django.contrib.auth.models.User'>
<class 'django.contrib.auth.models.User'>
```
- This comparison was returning False
```python
if post.author.user is user:
```

- When changed to compare with the `user.id` it worked.
```python
# Working code
def get(self, *args, **kwargs):
    user = get_object_or_404(User, pk=self.request.user.pk)
    post = get_object_or_404(Post, pk=self.kwargs['pk'])

    # comparison with user.id needed here to solve bug #
    if post.author.user.id is user.id or user.userprofile.is_mod:
        return super(ReviewPostView, self).get(*args, **kwargs)
    else:
        return redirect('home')
```