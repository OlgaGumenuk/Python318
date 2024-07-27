from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'klk4566jkdhdss4877eoldmc78955fkcmn14788'

menu = [
    {'name': 'Главная', 'url': 'index'},
    {'name': 'О нас', 'url': 'about'},
    {'name': 'Обратная связь', 'url': 'contact'},
]


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="Главная", menu=menu)


@app.route('/about')
def about():
    return render_template('about.html', title="О нас", menu=menu)

# @app.route("/profile/<int:username>")
# @app.route("/profile/<float:username>")
# @app.route("/profile/<path:username>")- любые допуст.символы url и слэш# @app.route("/profile/<path:

def profile(username):
    return f"Пользователь: {username}"


@app.route('/contact', methods=["POST", "GET"])
def contact():
    if request.method == 'POST':
        print(request.form)
        if len(request.form['username']) > 2:
            flash("Сообщение отправлено успешно!", category="success")
        else:
            flash("Ошибка отправки", category="error")

        # context = {
        #     'username': request.form['username'],
        #     'email': request.form['email'],
        #     'message': request.form['message']
        # }
        # return render_template('contact.html', **context, title="Обратная связь", menu=menu)

    return render_template('contact.html', title="Обратная связь", menu=menu)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html', title='Страница не нашлась', menu=menu)

if __name__ == '__main__':
    app.run(debug=True)
