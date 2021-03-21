from flask import render_template
from flask_login import login_required, current_user

from ..models.models import Issue


def configure_account_routes(app):
    @app.route('/account')
    @login_required
    def account():
        user_issues = Issue.objects(author=current_user.id)
        return render_template('account.html', user=current_user, issues=user_issues)