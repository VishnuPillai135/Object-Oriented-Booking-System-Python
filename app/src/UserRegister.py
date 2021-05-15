from User import User
from flask import Flask, redirect, request, render_template, url_for
from flask_login import LoginManager,login_user, current_user, login_required, logout_user
from server import app,login_manager
class UserRegister:
    def __init__(self):
        self._users = []

    def add_user(self, email, password, name, phone, mobilePhone, medicare):
        user = User(email, password, name, phone, mobilePhone, medicare)
        self._user.append(user)
        return True

    def verify_email(self, name, password):
        for user in self._users:
            if user.name == email:
                return user

        return None
