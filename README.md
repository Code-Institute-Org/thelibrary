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

### images
- Library background image by [mentatdgt on Pexels.com](https://www.pexels.com/photo/library-photo-1319854/)

## Testing

### solved bugs
1. z-index was not working on absolute positioned elements, causing user avatars on list view cards to overlap the menu dropdown options. 
- Issue was solved by adding position: relative; to the navbar and then adding a z-index of 99.
- Solution found in this post on [Stack Overflow](https://stackoverflow.com/questions/16315125/position-absolute-has-greater-z-index-than-position-fixed)

2. Adding the `selected` attribute to the category `<option>` elements, conditional on which value was in the kwargs was not working.

```html
{% if category.pk == category_pk %}selected{% endif %}
```
- When printing `{{ category.pk }}` and `{{ category_pk }}` to the template, they were printing as the same. However the comparison of the two with `==` was not evaluating to True. 
- After some digging I realized that one was a string and the other was an int. Using the `stringformat` filter fixed the problem:
```html
{% if category.pk|stringformat:"i" == category_pk %}selected{% endif %}
```