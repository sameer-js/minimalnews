from flask import flash, redirect, render_template, url_for

from ..models import User
from . import auth
from .forms import RegistrationForm
from .. import db


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # print(form.categories.data)
        user = User(email=form.email.data,
                    preferred_time=form.preferred_time.data)
        for category in form.categories.data:
            user.add_subscription(category)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('auth/register.html', form=form)
