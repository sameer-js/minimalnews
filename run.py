import os

from app import create_app, db
from app.models import News, User, categories
from app.engine import news_spider

app = create_app(os.environ.get('FLASK_CONFIG', 'default'))


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, categories=categories)


@app.cli.command()
def test():
    """ Run the unit tests """
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
   

@app.cli.command()
def scrape():
    """ Run the scraper """
    news_spider.run_spider()

