# The Library

The Slack room for our Code Institute community of students, alumni and staff contains a wealth of useful information, tips, advice and resources created by the community for CI students. But Slack doesn't provide a good place to store, sort, search, filter and categorize the content produced by our community members. This library was created to provide a central hub of resources to support our students, with all the search and filtering functionality they need to make it accessible and useful.

## Table of Contents
1. [UX](#ux)
    - [User Goals](#user-goals)
    - [User Stories](#user-stories)
        - [CI students](#ci-students)
        - [Authors](#authors)
        - [General users](#general-users)
        - [Staff users](#staff-users)
        - [Moderator users](#moderator-users)
        - [Admin users](#admin-users)
    - [Wireframes](#wireframes)
2. [Features](#features)
3. [Information Architecture](#information-architecture)
    - [Database Choice](#database-choice)
    - [Data Models](#data-models)
        - [User](#user)
        - [UserProfile](#userprofile)
        - [PostTag](#posttag)
        - [PostCategory](#postcategory)
        - [PostFlag](#postflag)
        - [Bookmark](#bookmark)
        - [Course](#course)
        - [SlackChannel](#slackchannel)
4. [Technologies Used](#technologies-used)
    - [Tools](#tools)
    - [Databases](#databases)
    - [Libraries](#libraries)
5. [Testing](#testing)
    - [Solved Bugs](#solved-bugs)
6. [Deployment](#deployment)
    - [Run this project locally](#run-this-project-locally)
        - [Requirements](#requirements)
        - [Instructions](#instructions)
    - [Heroku Deployment](#heroku-deployment)
7. [Credits](#credits)
    - [Code](#code)
    - [Images](#images)
8. [Acknowledgements](#acknowledgements)
9. [Contact](#contact)


## UX

### User Goals
The central target users for The Library are: 
- Code Institute students
- Potential students who want to see what the CI community has to offer
- Code Institute staff who want to share useful resources outside of the course content

User goals include:
- Find posts relevant to an issue I am currently facing with my project
- Find extra resources to support my research and debugging
- Learn more about a certain coding subject
- Be able to navigate The Library easily to find what I need
- Be able to create new posts in the Library

The Library is a great way to meet these needs, because
- The website has been carefully designs with the needs of the community in mind. As the developer was herself once a CI student who created supporting content, and understands the pitfalls of the current slack pinned posts approach to the problem The Library solves.
- The navigation fits with conventions of well laid out software, emulating the Google simple icon based navigation approach.
- All the information a reader needs is easy to find and well laid out.
- Post information can be searched using keywords, categories and tags, and can be filtered by newest, oldest, popularity and category. Giving users multiple ways to find what they need within the application's database.

### User Stories

#### CI students
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

#### Authors
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

#### General users (not necessarily logged in)
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

#### Staff users
1. As a CI staff member, I want to be able to skip the moderation process for posts so that my posts are published instantly.
- Users who are staff should skip moderation process for new posts
2. As a CI staff member, I want the CI logo to show next to my username within the app, so that I am easily identifiable as a staff member.
- CI logo should display next to users who have is_staff = True in the UserProfile 

#### Moderator users
1. As a moderator, I want to get a notification when new posts are waiting for review so that I can review them in a timely manner.
- Site should include a notification for moderators when new posts are waiting for review.
2. As a moderator, I want to be able to manage my notification settings between in-app or email notifications so that I can manage how often I am contacted to moderate content.
- Site should include a moderator manager panel that allows mods to choose email or in-app only notifications.
3. As a moderator, I want to be able to view everything I need to review in one place, so I can be sure I have checked everything before approval.
- Review page should include preview of the search results card as well as the full posts for moderators.
4. As a moderator, I want my status to be visible, so that other users are aware of my contribution to the library.
- Site should display badge for users who are moderators.

#### Admin users
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

### Wireframes
- [Home page](https://ibb.co/8MMzCmz)
- [List view for posts](https://ibb.co/T0SdJtX)
- [Create and Edit post page](https://ibb.co/JFvpZph)
- [Post detail](https://ibb.co/cT71jt4)
- [Settings](https://ibb.co/L8HX30s)
- [Author profile](https://ibb.co/PQkPZCS)
- [Your profile](https://ibb.co/nzqbBJ2)


## Features 
*To be added*
## Information Architecture

### Database Choice
- As a framework Django works with SQL databases. During development on my local machine I worked with the standard **sqlite3** database installed with Django.
- On deployment, the SQL database provided by Heroku is a **PostgreSQL** database. 
- Static and media files are stored in an **AWS S3 Bucket**

### Data Models

#### User
The User model utilized for this project is the standard one provided by `django.contrib.auth.models`. This model was not adapted, instead the user data was extended into a custom UserProfile model.

#### UserProfile

Name | DB Key | Specifications | Field Type
--- | --- | --- | ---
User | user | on_delete=models.CASCADE | ForeignKey to User
Bio | bio | max_length=200 | CharField
Profile Picture | profile_pic | upload_to="images/profiles/" | ImageField
LinkedIn | linkedin | - | URLField
GitHub | github | - | URLField
Admin | is_admin | default=False | BooleanField
Moderator | is_mod | default=False | BooleanField
Staff | is_staff | default=False | BooleanField
Date Joined | date_joined | default=datetime.date.today | DateField

This model contains two methods: 
- `kudos_badge()` which finds how many posts the user has created and returns the level of kudos badge they have earned as a string. This string is then used as a class to control what color badge is displayed with the user profile information.
- `get_author_name()` which returns the authors full name, if it has been provided. If not, then the users username.

An instance of UserProfile is automatically generated for every new instance of User.

#### PostTag

Name | DB Key | Specifications | Field Type
--- | --- | --- | ---
Name | name | max_length=50 | CharField

PostTag query sets are returned ordered alphabetically.

#### PostCategory

Name | DB Key | Specifications | Field Type
--- | --- | --- | ---
Name | name | max_length=20 | CharField

PostCategory query sets are returned ordered alphabetically.

#### PostFlag

Name | DB Key | Specifications | Field Type
--- | --- | --- | ---
Flagger | flagger | on_delete=models.PROTECT | ForeignKey to User
Reason | reason | choices=FLAG_REASONS | CharField
Flag Message | message | max_length=200 | TextField

#### Post
Name | DB Key | Specifications | Field Type
--- | --- | --- | ---
Post Title | title | max_length=70 | CharField
Post Summary | summary | max_length=140 | CharField
Slug | slug | max_length=200, unique=True | SlugField
Post Body | body | - | RichTextField
Author | author | on_delete=models.CASCADE | ForeignKey to UserProfile
Date Created | created_on | default=timezone.now | DateTimeField
Date Updated | updated_on | - | DateTimeField
Post Status | status | max_length=100, choices=STATUS_CHOICES, default=SUBMITTED | CharField
Moderator Msg | mod_message | max_length=300 | TextField
Moderator | moderator | on_delete=models.PROTECT | ForeignKey to User
Post Category | category | on_delete=models.PROTECT | ForeignKey to PostCategory
Tags | tags | related_name='post_tags' | ManyToManyField to PostTag
Likes | likes | related_name='post_likes' | ManyToManyField to User
Post Image 1 | image_1 | upload_to="images/posts/" | ImageField
Post Image 2 | image_2 | upload_to="images/posts/" | ImageField
Post Image 3 | image_3 | upload_to="images/posts/" | ImageField
Post Image 4 | image_4 | upload_to="images/posts/" | ImageField
Post Flag | flag | on_delete=models.SET_NULL, related_name='flags' | ForeignKey to PostFlag
Editors Note | editors_note | max_length=400 | TextField
Slack Channel | slack_channel | on_delete=PROTECT | ForeignKey to SlackChannel
Course | course | on_delete=PROTECT | ForeignKey to Course
YouTube Video | youtube | - | URLField

This model contains one custom method: 
- `total_likes()` which returns the total number of likes a post has.

#### Bookmark
Name | DB Key | Specifications | Field Type
--- | --- | --- | ---
Post | post | on_delete=CASCADE | ForeignKey to Post
User | user | on_delete=CASCADE | ForeignKey to User
Date Bookmarked | created_on | default=timezone.now | DateTimeField

Bookmark query sets are returned ordered by when they were created.

#### Course
Name | DB Key | Specifications | Field Type
--- | --- | --- | ---
Name | name | max_length=50 | CharField

Bookmark query sets are returned ordered by their id.

#### SlackChannel
Name | DB Key | Specifications | Field Type
--- | --- | --- | ---
Name | name | max_length=50, unique=True | CharField
Channel ID | slack_channel_id | max_length=20, unique=True | CharField

Bookmark query sets are returned ordered alphabetically by their name.

## Technologies Used

### Tools
- [Visual Studio Code](https://code.visualstudio.com/) is the IDE used for developing this project. 
- [Django](https://www.djangoproject.com/) as python web framework for rapid development and clean design.
- [Django AllAuth](https://django-allauth.readthedocs.io/en/latest/overview.html) to support authentication with Slack
- [Django ckeditor](https://pypi.org/project/django-ckeditor/) to provide rich text editor for creating and editing library posts
- [AWS S3 Bucket](https://aws.amazon.com/) to store images entered into the database.
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) to enable creation, configuration and management of AWS S3.
- [Django Heroku](https://pypi.org/project/django-heroku/) to improve deployment of django projects on heroku.
- [Django Storages](https://django-storages.readthedocs.io/en/latest/) a collection of custom storage backends with django to work with boto3 and AWS S3.
- [Gunicorn](https://pypi.org/project/gunicorn/) WSGI HTTP Server for UNIX to aid in deployment of the Django project to heroku.
- [Pillow](https://pillow.readthedocs.io/en/stable/) as python imaging library to aid in processing image files to store in database.
- [Psycopg2](https://pypi.org/project/psycopg2/) as PostgreSQL database adapter for Python.
- [Whitenoise](http://whitenoise.evans.io/en/stable/) to allows the web app to serve its own static files.
- [PIP](https://pip.pypa.io/en/stable/installing/) for installation of tools needed in this project.
- [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03) to handle version control.
- [GitHub](https://github.com/) to store and share all project code remotely. 
- [Photoshop](www.adobe.com/Photoshop) to edit, crop and save images as well as utilizing the colour picker to ensure color consistency over the entire project.
- [Browserstack](https://www.browserstack.com/) to test functionality on all browsers and devices.
- [Heroku](https://heroku.com/) for deployment
- [Balsamiq](https://balsamiq.com/) to create the wireframes for this project.

### Databases
- [PostgreSQL](https://www.postgresql.org/) for production database, provided by heroku.
- [SQlite3](https://www.sqlite.org/index.html) for development database, provided by django.

### Libraries
- [Bootstrap](https://www.bootstrapcdn.com/) to simplify the structure of the website and make the website responsive easily.
- [FontAwesome](https://www.bootstrapcdn.com/fontawesome/) to provide icons for The House of Mouse webshop.
- [Google Fonts](https://fonts.google.com/) to style the website fonts.
- [Fancybox](https://fancyapps.com/fancybox/3/) to provide sleek JavaScript lightbox to view images in.

### Languages
- This project uses HTML, CSS, JavaScript and Python programming languages.

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

## Deployment

### Run this project locally

#### Requirements

Ensure you have the following tools: 
- An IDE such as VSCode
The following must be installed on your machine:
- [PIP](https://pip.pypa.io/en/stable/installing/)
- [Python 3](https://www.python.org/downloads/)
- [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03)

To allow you to access all functionality on the site locally, ensure you have created a free accounts with [AWS](https://aws.amazon.com/) and [set up an S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html)

Please click the links above for documentation on how to set these up and retrieve the necessary environment variables.

#### Instructions
1. In the terminal of your IDE type the following command to clone a copy of the repo
```
git clone https://github.com/AJGreaves/thelibrary
```
2. A virtual environment is recommended for the Python interpreter, I recommend using Pythons built in virtual environment. Enter the command:
```
python -m .venv venv
```
_NOTE: The `python` part of this command and the ones in other steps below assumes  you are working with a windows operating system. Your Python command may differ, such as `python3` or `py`_

3. Activate the .venv with the command:
```
.venv\Scripts\activate 
```
_Again this **command may differ depending on your operating system**, please check the [Python Documentation on virtual environments](https://docs.python.org/3/library/venv.html) for further instructions._

5. If needed, Upgrade pip locally with
```
pip install --upgrade pip.
```

6. Install all required modules with the command 
```
pip -r requirements.txt.
```

7. Set up the following environment variables within your IDE. 
- Create a `env.py` file in the root directory of your project, and add your environment variables as below. Do not forget to restart your machine to activate your environment variables or your code will not be able to see them: 

```python
import os

os.environ["SECRET"] = "<enter key here>"
os.environ["DEV"] = "1"
os.environ["HOSTNAME"] = "<enter hostname here>"
os.environ["DATABASE_URL"] = "<enter url here>"
os.environ["USE_AWS"] = "True"
os.environ["AWS_STORAGE_BUCKET_NAME"] = "<enter bucket name here>"
os.environ["AWS_S3_REGION_NAME"] = '<enter s3 region here>'
os.environ["AWS_ACCESS_KEY_ID"] = '<enter key here>'
os.environ["AWS_SECRET_ACCESS_KEY"] = '<enter key here>'
```

- `HOSTNAME` should be the local address for the site when running within your own IDE.
- `DEV` environment variable is set only within the development environment, it does not exist in the deployed version, making it possible to have different settings for the two environments. For example setting DEBUG to True only when working in development and not on the deployed site.

8. Migrate the admin panel models to create your database template with the terminal command
```
python manage.py migrate
```

9. Create your superuser to access the django admin panel and database with the following command, and then follow the steps to add your admin username and password:
```
python manage.py createsuperuser
```

10. You can now run the program locally with the following command: 
```
python manage.py runserver
```

11. Once the program is running, go to the local link provided and add `/admin` to the end of the url. Here, log in with your superuser account and create instances of Course, PostCategory, SlackChannel, and Post.

- Instances of Course must include courses named `5P Course` and `4P Course` for the template logic of their post labels to work.

12. Once instances of these items exist in your database your local site will run as expected.

### Heroku Deployment

To deploy The Library to heroku, take the following steps:

1. Create a `requirements.txt` file using the terminal command `pip freeze -local > requirements.txt`.

2. Create a `Procfile` with the terminal command `echo web: gunicorn thelibrary.wsgi:application > Procfile`.

3. `git add` and `git commit` the new requirements and Procfile and then `git push` the project to GitHub.

3. Create a new app on the [Heroku website](https://dashboard.heroku.com/apps) by clicking the "New" button in your dashboard. Give it a name and set the region to whichever is applicable for your location.

4. From the heroku dashboard of your newly created application, click on "Deploy" > "Deployment method" and select GitHub.

5. Confirm the linking of the heroku app to the correct GitHub repository.

6. In the heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".

7. Set the following config vars:

| Key | Value |
--- | ---
AWS_ACCESS_KEY_ID | `<your secret key>`
AWS_S3_REGION_NAME | `<your region name>`
AWS_SECRET_ACCESS_KEY | `<your aws access key>`
AWS_STORAGE_BUCKET_NAME | `<your aws bucket name>`
DATABASE_URL | `<your postgres database url>`
HOSTNAME | `<your heroku app hostname>`
SECRET | `<your secret key>`
USE_AWS | `True`

8. From the command line of your local IDE:
- Enter the heroku postres shell 
- Migrate the database models 
- Create your superuser account in your new database

Instructions on how to do these steps can be found in the [heroku devcenter documentation](https://devcenter.heroku.com/articles/heroku-postgresql).

9. In your heroku dashboard, click "Deploy". Scroll down to "Manual Deploy", select the master branch then click "Deploy Branch".

10. Once the build is complete, click the "View app" button provided.

11. From the link provided add `/admin` to the end of the url. Here, log in with your superuser account and create instances of Course, PostCategory, SlackChannel, and Post.

- Instances of Course must include courses named `5P Course` and `4P Course` for the template logic of their post labels to work.

12. Once instances of these items exist in your database your heroku site will run as expected.
## Credits

### Code
- Code to animate notification bell in the navbar by [Fazlur Rahman](https://codepen.io/fazlurr/pen/xeXpqx)
- Code to handle pagination in function based views from [simpleisbetterthancomplex.com](https://simpleisbetterthancomplex.com/tutorial/2016/08/03/how-to-paginate-with-django.html)
- Code to create triangle in post card corners for course indication from [This stack overflow post](https://stackoverflow.com/questions/18531959/how-to-create-triangle-shape-in-the-top-right-angle-of-another-div-to-look-divid)
- Loading spinner code from [W3Schools](https://www.w3schools.com/howto/howto_css_loader.asp) 

### Images
- Library background image by [mentatdgt on Pexels.com](https://www.pexels.com/photo/library-photo-1319854/)

## Acknowledgements

Special thanks to [Chris Z.](https://github.com/ckz8780) for his help with a couple of sticky moments while working on this project.

## Contact
To contact me, feel free to email
`anna (at) codeinstitute (dot) net`