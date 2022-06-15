from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('likes'))


@app.route('/likes')
def likes():
    feedback = None

    get_request = request.args.get('names')
    split_request = str(get_request).split(",")
    names = list(split_request)

    if get_request is None:
        return render_template('likes.html', error=True, feedback=None, error_message=None)

    for name in names:
        if not name.isalpha():
            error_message = "Имя может содержать только символы алфавита."
            return render_template('likes.html', error=True, feedback=None, error_message=error_message)
        elif len(name) > 10:
            error_message = "Имя не может содержать больше 10 символов."
            return render_template('likes.html', error=True, feedback=None, error_message=error_message)

    if len(names) == 0:
        feedback = 'Это никому не нравится.'
    elif len(names) == 1:
        feedback = f'{names[0]} лайкнул это.'
    elif len(names) == 2:
        feedback = f'{names[0]} и {names[1]} лайкнули это.'
    elif len(names) == 3:
        feedback = f'{names[0]}, {names[1]} и {names[2]} лайкнули это.'
    elif len(names) > 3:
        feedback = f'{names[0]}, {names[1]} и ещё {len(names) - 2} человека лайкнули это.'

    return render_template('likes.html', error=None, feedback=feedback, error_message=None)


if __name__ == "__main__":
    app.run(debug=True, port=8000)
