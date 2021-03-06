from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    title = 'Главная'
    user = {
        'name': 'Alex',
        'ago': 21
    }
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Ипполит'},
            'body': 'Какая гадость эта ваша заливная рыба!!'
        }
    ]
    return render_template(
        'index.html',
        title=title,
        user=user,
        posts=posts
    )