# Updating far away elements

Let's add an unread count to each feed in the sidebar!

Adding the unread count initially is relatively straightforward. When we load the page, count how many unread entries there are, and put them on the sidebar beside each feed:

```html title="templates/feed.html"
<span>{{ feed_['entries'].values() | rejectattr("read") | list | length }}</span>
```

This is not the simplest bit of code! Using Jinja filters we build an expression that:

- Gets the current feed's entries.
- Rejects those that have `read=True`.
- Turns it into a list.
- Gets the length.

We can put that in a span, and we could style it however we want.

## Updating without reloading

The main difficulty with this is that when we mark an entry as read, the sidebar won't reload. We also can't use HTMX out-of-band swaps easily, because the endpoint that marks an entry as read redirects the user to a different site.

So we go back to AlpineJS, where we'll use event-driven development to achieve this.

When we mark an entry as read we're already using AlpineJS to change the state locally:

```
x-on:click="read = true"
```

AlpineJS also has event handling, so we can dispatch an event here that can then be caught by the span that contains the number of unread entries.

To dispatch an event, we do:

```
x-on:click="$dispatch('read'); read = true;"
```

We can include extra data, and we should! A user might click an entry multiple times, so let's include whether the entry has an unread state or not:

```
x-on:click="$dispatch('read' { read: read }); read = true;
```

There's a lot of `read` there! In order:

- `'read'` is the event name.
- In `{ read: read }`, the first `read` is the name of the key in the object that we are passing.
    - The second `read` is the current value of the AlpineJS attribute we're using to store whether an entry has been read or not.
- After the semicolon, we change the aforementioned status to `true`. Nothing to do with the event dispatch.

You could probably write this line of code better than me!

Here's the full `entry.html` code with the changed line highlighted:

```html title="templates/partials/entry.html" linenums="1" hl_lines="33"
--8<-- "steps/05-unread-numbers/app/templates/partials/entry.html"
```

### Catching the event

AlpineJS will bubble up the event upwards through any HTML container _that is itself also an AlpineJS component_.

At the moment, there are no common ancestors of the entry and the sidebar which are AlpineJS components. So there is no way for this event to be caught by the sidebar `span`.

Let's find a common ancestor of entries and the sidebar: the `body`.

We could structure our HTML page a bit better, put everything inside a `div` and use that. But we've got what we've got, and the `body` is a fine element.

Let's make the `body` an AlpineJS component so that the event can bubble up to it and be caught by any of its children.

```
<body x-data>
```

We don't need to put anything in `x-data`, just doing this does what we need.

Now we can go to the event and add some logic there to catch the event. If the current status of the entry is unread, then we can decrease the number in the badge by 1:

```html
<span @read.window="{{ '$el.innerHTML -= $event.detail.read ? 0 : 1' if feed.href == feed_['href'] else '' }}">{{ feed_['entries'].values() | rejectattr("read") | list | length }}</span>
```

We also need to make sure that we're only decreasing the number in the _currently active feed_, as that's the only feed in which we could be clicking an article. Otherwise, all feeds would see their unread article count lower.

Here's the final code for the feed with changed lines highlighted:

```html title="templates/feed.html" linenums="1" hl_lines="13"
--8<-- "steps/05-unread-numbers/app/templates/feed.html"
```

!!! note
    `@read` is the event name, and `@read.window` makes it so the `span` can catch the event even if it wasn't emitted by a child component.

With this, we're done! We've rapidly built a simple app that is just interactive enough, simple to understand, and very fast to incrementally update.

Thank you for reading, and I hope you've enjoyed this session!
