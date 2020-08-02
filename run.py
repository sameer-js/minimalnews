import os

from app import create_app, db
from app.models import User, categories

app = create_app(os.environ.get('FLASK_CONFIG', 'default'))


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, categories=categories)
