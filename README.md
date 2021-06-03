# The Library

A hobby project to create a library of community generated resources. Built with Django.

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

### Getting set up
1. Open new empty project folder in vscode
2. Set terminal to cmd in vscode:
```
Press Ctrl + Shift + P to open the command palette.
Type 'shell' in the searcher.
Select 'Terminal: Select Default Shell'.
Select 'Command Prompt'
```
3. Update pip
```
pip install --upgrade pip.
```
4. Set up virtual environment:
```
python -m venv venv
```
5. Activate virtual environment
```
venv\Scripts\activate 
```
6. Install Django
```
python -m pip install Django
```
7. Start django project files
```
django-admin startproject thelibrary .
```
8. Install django all-auth
```
pip install django-allauth
```

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