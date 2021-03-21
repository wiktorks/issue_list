from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user

from ..utils.forms import CreateIssue
from ..models.models import Issue

def configure_issue_routes(app):
    @app.route('/account/create_issue', methods=['GET', 'POST'])
    @login_required
    def create_issue():
        form = CreateIssue()
        if form.validate_on_submit():
            user_issues = Issue.objects(
                author=current_user.id, title=form.title.data)
            if not user_issues:
                new_issue = Issue(title=form.title.data)
                new_issue.author = current_user.id
                new_issue.save()
                flash(
                    f'Issue "{form.title.data}" has been created successfully.', category='success')
                return redirect(url_for('account'))
            else:
                flash(
                    f'Issue with title {form.title.data} already exists. Please choose a different title.', category='danger')

        return render_template('createIssue.html', form=form)