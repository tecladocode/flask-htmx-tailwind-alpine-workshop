

import feedparser
import jinja_partials
from flask import Flask, render_template

feeds = {
    "https://blog.teclado.com/rss/": {"title": "The Teclado Blog", "href": "https://blog.teclado.com/rss/", "show_images": True, "entries": {}},
    "https://www.joshwcomeau.com/rss.xml": {"title": "Josh W. Comeau", "href": "https://www.joshwcomeau.com/rss.xml", "show_images": False, "entries": {}},
}

def create_app():
    app = Flask(__name__)
    jinja_partials.register_extensions(app)


    @app.route("/feed/")
    @app.route("/feed/<path:feed_url>")
    def render_feed(feed_url: str = None):
        for url, feed_ in feeds.items():
            parsed_feed = feedparser.parse(url)
            for entry in parsed_feed.entries:
                if entry.link not in feed_["entries"]:
                    feed_["entries"][entry.link] = entry

        if feed_url is None:
            feed = list(feeds.values())[0]
        else:
            feed = feeds[feed_url]
        return render_template("feed.html", feed=feed, feeds=feeds)


    return app