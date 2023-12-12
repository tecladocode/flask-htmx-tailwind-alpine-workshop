# Simple, dynamic pagination with HTMX

In our earlier application, we rendered the entries directly in the `feed.html`. Now let's create an endpoint that will render one page of entries using our partial.

!!! warning

    When we get an RSS feed and parse it using feedparser, that gives us _all_ the entries that are present in the feed. In some cases, it could be dozens or even hundreds of entries.
    
    For pagination to be most effective, you'd only load (from your database) the entries for the current page. Since we don't have a database and we're parsing the feeds every time, we don't have the ability to do this. We're "faking" the need for pagination at the moment, but it'll show you how it works.

This is what the new endpoint looks like:

```py title="__init__.py" linenums="1" hl_lines="31-48"
--8<-- "steps/02-dynamic-pagination/app/__init__.py"
```

We'll modify the entry page partial to include a button to load the next page of entries. Having the button as part of the page may seem weird, but it's a nice way to ensure that all the data a page needs is colocated. Since a page knows its own page number, it's easy to make a button to get the next page (just add 1).

If we stored state outside of the page, then when we render the page, we'd have to keep track of the state elsewhere.

```html title="templates/partials/entry_page.html" linenums="1" hl_lines="5-9"
--8<-- "steps/02-dynamic-pagination/app/templates/partials/entry_page.html"
```

Finally, we can call our new endpoint from `feed.html` instead of rendering the partial there. Using HTMX, it can call the endpoint and replace the endpoint's response into the element that makes the request:

```html title="templates/feed.html" linenums="1" hl_lines="22-27"
--8<-- "steps/02-dynamic-pagination/app/templates/feed.html"
```