from tg_back import tur_app


@tur_app.route('/registration')
def registration():
    return 'Успешная регистрация'