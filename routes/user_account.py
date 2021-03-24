from flask import render_template, flash
from flask_login import login_required, current_user

from ..models.models import Issue
from ..utils.forms import AccountSettings
from ..extensions import bcrypt


def configure_account_routes(app):
    @app.route('/account')
    @login_required
    def account():
        user_issues = Issue.objects(author=current_user.id)
        return render_template('account.html', user=current_user, issues=user_issues)

    @app.route('/account/settings', methods=['GET', 'POST', 'DELETE'])
    @login_required
    def account_settings():
        form = AccountSettings()
        form.current_user = current_user
        if form.validate_on_submit() and bcrypt.check_password_hash(current_user.password, form.old_password.data):
            current_user.name = form.username.data
            current_user.email = form.user_email.data
            password = bcrypt.generate_password_hash(
                form.password.data).decode('utf-8')
            current_user.password = password
            current_user.save()
            
            flash(message='Account data has been successfully changed.', category='success')
        return render_template('account.html', user=current_user, form=form)
