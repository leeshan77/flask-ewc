from flask import Blueprint, url_for, request, render_template
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/hello')
def hello_pybo():
    return 'Hello, Esther!'


@bp.route('/')
def index():
    return redirect(url_for('question._list'))