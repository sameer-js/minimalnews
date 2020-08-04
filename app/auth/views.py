from flask import flash, redirect, render_template, url_for

from .. import db
from ..email import send_email
from ..main import main
from ..models import User
from . import auth
from .forms import RegistrationForm


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.email.data.split('@')[0]
        user = User(email=form.email.data,
                    preferred_time=form.preferred_time.data)
        for category in form.categories.data:
            user.add_subscription(category)
        db.session.add(user)
        db.session.commit()
        token = user.generate_confirmation_token()
        send_email(user.email, 'Confirm your subscription',
                   '/auth/email/confirm', username=username, token=token)
        flash('A confirmation link has been sent to you via email.')
    return render_template('auth/register.html', form=form)


@auth.route('/confirm/<token>')
def confirm(token):
    if User.confirm(token):
        db.session.commit()
        return redirect(url_for('auth.success'))
    else:
        flash('The confirmation link is invalid or has expired!')
    return redirect('auth.register')


@auth.route('/success')
def success():
    return render_template('auth/success.html')
