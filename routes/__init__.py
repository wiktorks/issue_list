from .login import configure_login
from .main import configure_main
from .issue import configure_issue_routes
from .user_account import configure_account_routes

def configure_routes(app):
    configure_main(app)
    configure_login(app)
    configure_issue_routes(app)
    configure_account_routes(app)