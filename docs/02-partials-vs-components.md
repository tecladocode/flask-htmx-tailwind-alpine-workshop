# Partials vs. Components?

Jinja has the concept of "macro" and "include". Both of these can be used to bring in another template or part of a template into the current template.

However, macros can't be rendered using render_template, and includes can't take arbitrary arguments.

Jinja partials solves this by allowing us to define renderable templates (so they can be rendered and returned by a Flask endpoint), but also we can render them within other templates and pass arbitrary arguments, like so:

``` jinja2
{{ render_partial("partials/entry.html", title=item.title) }}
```
