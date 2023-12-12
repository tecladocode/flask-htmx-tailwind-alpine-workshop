# Adding new RSS feeds

To add new RSS feeds, we need a form!

Let's start by creating a partial for it:

```html title="templates/partials/add_feed.html"
--8<-- "steps/03-01-adding-feeds-htmx/app/templates/partials/add_feed.html"
```

Then we can either:

- Show the form by calling an endpoint that returns its HTML; or
- Show the form using JavaScript 😱 (don't worry, AlpineJS is very minimal)

## Adding feeds using HTMX

We'll begin by adding two endpoints to our Flask app: one for rendering the form, and one for dealing with the form submission:

```py title="__init__.py" linenums="1" hl_lines="50-60"
--8<-- "steps/03-01-adding-feeds-htmx/app/__init__.py"
```

Then we'll add a button in our `feed.html` template that, when clicked, calls the `/render_add_feed` endpoint and replaces the HTML returned into the current page:

```html title="templates/feed.html" linenums="1" hl_lines="18-22"
--8<-- "steps/03-01-adding-feeds-htmx/app/templates/feed.html"
```

That's it! Doesn't get much easier than that!

## Adding feeds with AlpineJS

If you want to be able to _hide_ the form once you've shown it, then you start needing JavaScript. AlpineJS offers a very minimalistic API that complements HTMX very well.

Let's bring it into our base template:

```html title="templates/base.html" linenums="1" hl_lines="9"
--8<-- "steps/03-01-adding-feeds-htmx/app/templates/base.html"
```

Then let's change our `feed.html` so it uses AlpineJS:

```html title="templates/feed.html" linenums="1" hl_lines="18-25"
--8<-- "steps/03-02-adding-feeds-alpine/app/templates/feed.html"
```

Here we have the following:

- `x-data="{show: false}"` on the button parent.
- The first child `div` contains our form, but it's hidden to begin with because `x-show="show"` will hide it (since `show: false`).
- Then there's a button that toggles `show` with `x-on:click="show = !show`.
    - The button text changes depending on the `show` variable, and lets us hide or show the form.

If we use Alpine, we can get rid of the `/render_add_feed` template, so that's a small bonus:

```diff title="__init__.py"
-     
-     @app.route("/render_add_feed")
-     def render_add_feed():
-         return render_template("partials/add_feed.html")
```

We could also move `add_feed.html` outside of `partials` (since we're no longer rendering it on its own). We could make it a macro. Or we could put the HTML directly in the page. But keeping it as a partial is fine too!