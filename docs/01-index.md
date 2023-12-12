# Rapid Project Setup

This idea of rapid development isn't necessarily the "best" way to do anything. But it is definitely a rapid way of doing things.

What I'll show you is how you can very quickly develop a server-side application that is dynamic, usable, simple, and (in my opinion) joyful to work with.

As your application grows and becomes more complex, this way of developing, and indeed the whole application you've already developed using this method, may need re-written.

This is ideal for prototypes, side projects that you want to get out there quickly, internal tools, etc. If you're not careful, the code ends up becoming a bit messy. But at that point, your idea will be validated. You'll have customers or users, and you can spend time finessing your approach and your code.

By doing things this way I've implemented relatively complex interfaces in minutes or hours, instead of days.

## Rapid project set-up

Python packaging! We love it dearly. To get started quickly, I recommend using [Rye](https://rye-up.com/guide/installation/):

```
rye init flask-htmx-tailwind
cd flask-htmx-tailwind
rye pin 3.12
```

With these three commands you create your project folder, set up your virtual environment, set your Python version (and install it if you don't have it already).

To install requirements, either add them to `pyproject.toml`, or use `rye add`:

```
rye add "flask[dotenv]" jinja-partials feedparser
rye sync
```

Then to run your Flask app you just do:

```
rye run flask run
```

You can also activate the `.venv` and run `flask run` as usual.

It's worth learning about Docker and docker-compose so you can run your app with that (and run a database alongside it), but for now this is good enough!

## Adding dependencies

### Adding TailwindCSS

There are many ways to run TailwindCSS when you run your Flask app, but for the speediest workflow, let's just use the CDN version of TailwindCSS. This means that we don't have to worry about compiling our CSS, and we can just use TailwindCSS classes in our HTML.

Add the TailwindCSS CDN to the `<head>` of your `base.html` template:

```html
<script src="https://cdn.tailwindcss.com"></script>
```

The CDN version of TailwindCSS contains all of the classes, so it isn't recommended for production applications. Instead, you should install `tailwindcss` with npm, and run it on your HTML files with `--minify` to create a smaller CSS file.

#### Using TailwindCSS with npm

See [https://tailwindcss.com/docs/installation](https://tailwindcss.com/docs/installation).

### Adding HTMX

Add the HTMX CDN to the `<head>` of your `base.html` template:

```html
<script src="https://unpkg.com/htmx.org@1.9.9"></script>
```

### Adding AlpineJS

HTMX is fantastic because it allows you to perform server requests, receive responses, and replace parts of your HTML, without reloading the page.

However, sometimes we just need to add some in-page interactivity.

AlpineJS is perfect for the job. It pairs very well with HTMX and is very lightweight.

```html
<script src="https://unpkg.com/alpinejs" defer></script>
```