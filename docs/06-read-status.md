# Entry read status indicator

Let's add some custom data to our entries, akin to what we'd do if we were storing them in a database. Let's add a `read` status.

We'll also add an endpoint for making an entry as read, which then redirects us to the actual entry post.

```py title="__init__.py" linenums="1" hl_lines="22 58-65"
--8<-- "steps/04-read-status/app/__init__.py"
```

Then we'll need to add some stuff to our entry partial as well, to show when an entry has been read or not.

We'll start with an icon that denotes the read status. It's just a green circle:

```html
<svg viewBox="0 0 16 16"
xmlns="http://www.w3.org/2000/svg"
class="fill-emerald-500 h-3 w-3 inline-block mb-1">
    <circle cx="8" cy="8" r="8" />
</svg>
```

Now we need to make it so the SVG only shows up if the entry is not read. We can do that with Jinja. Pass the entry's `read` status to the partial and then just do this:

```html
{% if not read %}
<!-- draw the svg -->
{% endif %}
```

But this will have one problem: when we click on an entry and read it, the app will show it as "unread" until we refresh the page. We need a solution that can update the app immediately, as well as update the backend state for when we refresh the page.

We can do this with HTMX! But it's one of these things that will be much simpler with JavaScript. So, we go back to AlpineJS.

We can add state to the entry `div`, which is populated from the Jinja value:

```
x-data="{ read: {{ read | lower }} }"
```

The `{{ read | lower }}` portion is a Jinja interpolation. The `read` value is a Python `True` or `False`. We turn it to lowercase so that the final result reads:

```
x-data="{ read: true }
```

This is valid JavaScript, so with this Alpine stores the boolean value `read` in the element.

Then we can change the link at the bottom to set the Alpine `read` value to `true` when we click the link. Here's the complete code, with the elements modified highlighted:

```html title="templates/partials/entry.html" linenums="1" hl_lines="9 10 18-25 33 34"
--8<-- "steps/04-read-status/app/templates/partials/entry.html"
```