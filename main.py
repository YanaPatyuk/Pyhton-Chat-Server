from flask import Blueprint, render_template

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return 'im the main'


@main.route('/profile')
def profile():
    return 'im your profile'

