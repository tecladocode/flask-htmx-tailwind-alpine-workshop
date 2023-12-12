# A Website without Reloading

One of the first things you can add with HTMX is boosted links. These links fetch the target link, and swap the returned HTML by the current page HTML.

With these, the page content changes without a page reload, which can make the page seem a bit snappier since there is no blank page in between link clicks.

First, let's create our Flask app. Since we don't have a database at the moment, we'll use a dictionary of feed URLs to feeds. Each feed has some attributes, as well as a dictionary of entries (mapping entry URL to entry body).

When we load the page, we'll go through our feeds and parse their RSS. This is very inefficient. You'd normally want a database, and parse the RSS periodically. It'll do the job for showing you how this all works.

```py title="__init__.py"
--8<-- "steps/01-website-without-reloading/app/__init__.py"
```

!!! note
    The way of updating the entries of a feed is over-complicated, but we need this logic for later on. At the moment, you could just do this:

    ```py
    for url in feeds:
        parsed_feed = feedparser.parse(url)
        feeds[url] = parsed_feed
    ```

    But we'll be adding some custom data to entries later, so we don't want to overwrite all the entries each time. That's why we're only adding new entries, and not those that already exist.

## Setting up the base template

In the base template we'll want to include our dependencies: TailwindCSS and HTMX.

We'll also set up the `content` block where other templates can put their content.

```html title="templates/base.html"
--8<-- "steps/01-website-without-reloading/app/templates/base.html"
```

## Our partials for entry and entry page

One entry will represent one article in the RSS feed we're reading:

```html title="templates/partials/entry.html"
--8<-- "steps/01-website-without-reloading/app/templates/partials/entry.html"
```

Entries can have images, and they expect a few properties which are named after the `feedparser` properties for an entry. That way when we parse a feed, we can just pass the entries directly to this template.

An entry page is a collection of entries. We don't need to have this as its own partial yet, but it will come in handy when we add pagination.

```html title="templates/partials/entry_page.html"
--8<-- "steps/01-website-without-reloading/app/templates/partials/entry_page.html"
```

## The main page

Now that we've got our partials and base template, we can put them together in the main feed page.

This has a list of feeds on the left, and the list of entries on the right.

```html title="templates/feed.html"
--8<-- "steps/01-website-without-reloading/app/templates/feed.html"
```

With this, we're ready to launch of site and test it out!

```
flask run
```