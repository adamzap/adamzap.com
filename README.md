# adamzap.com

A simple static site generator that uses `build_and_serve.py` to combine
`theme` and `content` into what you see on [adamzap.com].

`build_and_serve.py` builds on the more general use case of [mend].

### Goal

To build a personal website that I can look back on in ten, five, or even two
years from now and not cringe. Is it even possible?

### Shouts Out to These Awesome Modules

- `os` because is it possible to write a script without it?
- `codecs` because why didn't I write this in Python 3?
- `jinja2` for templating
- `shutil` for simplifying directory operations
- `datetime` see `os`
- `markdown` for HTML generation
- `functools` because writing `codecs.open(f, encoding='utf-8')` a lot is no
  fun
- `livereload` because I had a feeling that I shouldn't try to combine
  `SimpleHTTPServer` and `watchdog`
- `collections` for `OrderedDict`
- `feedgenerator` for generating feeds

Modules, I couldn't have done it without you! #thankful #blessed

[adamzap.com]: http://adamzap.com/
[mend]: https://github.com/adamzap/mend/
