from celery import Celery
from flask import Flask

from app.celery_tasks import process_article
from app.feed_parser import parse_feeds

app = Flask(__name__)


def make_celery(app):
    celery = Celery(
        app.import_name, backend="redis://localhost", broker="redis://localhost"
    )
    celery.conf.update(app.config)
    return celery


celery = make_celery(app)


@app.route("/parse_feeds", methods=["GET"])
def trigger_feed_parsing():
    parse_feeds.delay()
    return "Feed parsing started", 202


if __name__ == "__main__":
    app.run(debug=True)
