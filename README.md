# Mode-dependent buffer scrolling for Kitty

[Kitty][kitty] is a fast GPU-based terminal emulator.

[kitty]: https://sw.kovidgoyal.net/kitty


Kitty lets you configure keys to scroll the buffer;
by default, it uses `Ctrl+Shift+Page Up`, `Ctrl+Shift+Page Down`,
`Ctrl+Shift+↑`, `Ctrl+Shift+↓`, `Ctrl+Shift+Home`, and `Ctrl+Shift+End`.

When you run a fullscreen application
such as an editor, file manager, or terminal multiplexer,
they switch Kitty into the so-called *application screen*.
This is an alternate buffer that is not scrollable,
thus, scrolling keys do nothing.

With this kitten, you can configure keys
so that they scroll the normal buffer when it is the active one,
but when the application screen is active,
they send a keystroke to the running application.

## Why would you want that?

* Many terminal emulators scroll the buffer on `Shift+Page Up/Down`.
  So, muscle memory says you’d want to configure Kitty the same way.

* Midnight Commander uses shifted navigation keys
  to select blocks in the internal editor
  and files in the panels.

* Emacs (with `cua-mode`) also uses shifted navigation keys
  to mark a region.

* If you decide to run tmux within Kitty,
  it can also be configured to scroll its windows
  with shifted navigation keys.
  This way, you use the same keystrokes to scroll in Kitty and tmux.

      bind-key -n           S-PageUp   copy-mode -eu
      bind-key -T copy-mode S-PageUp   send-keys -X page-up
      bind-key -T copy-mode S-PageDown send-keys -X page-down


# Minimum requirements

Kitty 0.13.0 or higher.


# Installation

* Copy or symlink `smart_scroll.py`
  into your Kitty configuration directory
  (`~/.config/kitty`).

* Edit your `kitty.conf` to add some key shortcuts.

* Restart Kitty.


# Configuration example

The following snippet will set `Shift+↑`, `Shift+↓`,
`Shift+Page Up`, and `Shift+Page Down`
to scroll the normal screen by line or page,
and `Ctrl+Shift+Home` and `Ctrl+Shift+End`
to scroll to the top and bottom of the scrollback buffer,
but send these same keys to the running application if any.

```
map shift+up        kitten smart_scroll.py scroll_line_up   shift+up
map shift+down      kitten smart_scroll.py scroll_line_down shift+down
map shift+page_up   kitten smart_scroll.py scroll_page_up   shift+page_up
map shift+page_down kitten smart_scroll.py scroll_page_down shift+page_down
map ctrl+shift+home kitten smart_scroll.py scroll_home      ctrl+shift+home
map ctrl+shift+end  kitten smart_scroll.py scroll_end       ctrl+shift+end
```

The first argument (after `smart_scroll.py`)
can technically be any Kitty action that does not require arguments.
That action will be invoked without arguments
when the key is pressed while the normal screen is active.

The second argument specifies a key.
This key will be sent when the mapped key is pressed
while the application screen is active.
It may be the same key that is used to activate the mapping,
or a different one if you so desire.


# License

GNU General Public License version 3 or later.
