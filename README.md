# The Library

A hobby project to create a library of community generated resources. Built with Django.

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

- Code to animate notification bell in the navbar by [Fazlur Rahman](https://codepen.io/fazlurr/pen/xeXpqx)
