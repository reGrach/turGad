from tg_back import tur_app


@tur_app.route('/registration')
def registration():
    return 'упсешная геристраияц'

@tur_app.route('/helo')
def login():
    from flask import request

    with app.test_request_context('/hello', method='POST'):
        # теперь, и до конца блока with, вы можете что-либо делать
        # с контекстом, например, вызывать простые assert-ы:
        assert request.path == '/hello'
        assert request.method == 'POST'