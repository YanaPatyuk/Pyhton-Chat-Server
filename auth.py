from flask import Blueprint, render_template, redirect, url_for

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return 'you login'

# @auth.route('login', methods=['POST'])
# def login_post():

@auth.route('/signup')
def signup():
    return 'you signup'

# @auth.route('signup', methods=['POST'])
# def signup_post():

@auth.route('/logut')
def logout():
    return 'you logout'
