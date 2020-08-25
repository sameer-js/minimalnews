import os
from datetime import datetime

from app import create_app, db
from app.models import News, User, categories
from app.engine import news_spider
from app.email import distribute_news

app = create_app(os.environ.get('FLASK_CONFIG', 'default'))


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, News=News, User=User, categories=categories)


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


@app.cli.command()
def distribute():
    """ Distribute the newsletter """
    batch = {0: 'morning', 6: 'noon', 12: 'evening'}
    users = User.query.filter_by(confirmed=True,
                                preferred_time=batch.get(datetime.utcnow().hour))
    news_obj = News.query.limit(12)
    distribute_news(users, 'newsletter', news_obj=news_obj)

