from flask import render_template, flash, request
from . import auth
from .forms import RegistrationForm


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        print(form.email.data)
        print(form.preferred_time.data)
        print(form.politics.data, form.finance.data, form.sports.data, form.lifestyle.data)
    return render_template('auth/register.html', form=form)
