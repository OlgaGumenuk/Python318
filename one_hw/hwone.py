from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'edlskso5846cmvnb47123slkfjd5666dddl'

menu = [
    {'name': 'Главная', 'url': 'index'},
    {'name': 'Обо всем', 'url': 'about'},
    {'name': 'Что-то ещё', 'url': 'contact'},
]


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="Главная", menu=menu)


@app.route('/about')
def about():
    return render_template('about.html', title="Обо всем", menu=menu)


@app.route("/profile/<username>")
def profile(username):
    return f"Пользователь: {username}"


@app.route('/contact', methods=["POST", "GET"])
def contact():
    if request.method == 'POST':
        if len(request.form['username']) > 2:
            flash("Информация заполнена успешно", category="success")
        else:
            flash("Ошибка отправки", category="error")
        # print(request.form)
        # context = {
        #     'username': request.form['username'],
        #     'email': request.form['email'],
        #     'message': request.form['message']
        # }
        # print(request.form['username'])
        # return render_template('contact.html', **context, title="Заполни новое", menu=menu)

    return render_template('contact.html', title="Заполни новое", menu=menu)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html', title="Страница не нашлась", menu=menu)

if __name__ == '__main__':
    app.run(debug=True)
