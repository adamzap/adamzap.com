title: Landslide
date: 2015-04-11
index_meta: Python

Landslide is a Python program that generates HTML5 slideshows from Markdown,
Restructured Text, or Textile files. It's first release was in 2010.

- [PyPi]
- [Code]

### Skills

- Python programming
- Managing an open-source project
- Python packaging and distribution with PyPi

### Inspiration

Sometime in 2010, some of my coworkers and I started doing [Lightning Talks].
These short presentations were great for our morale, camaraderie, and public
speaking skills. I wanted a quick way to generate slides for them, so I wrote
Landslide.

Landslide came together with the help of two high-quality components that were
already done for me: the [Markdown] markup language and Google's [html5slides]
project.

Google created html5slides to show off the HTML5 features adding to Google
Chrome. It was an open-source slideshow that looked amazing at the time. I've
never been the best designer, so it was great to have the looks of the
slideshow done for me.

How hard would it be to pull the structure out of this slideshow and put my own
HTML in the slides? Better yet, what if I could write my content in Markdown
and run a script to generate the slideshow? In a fit of inspiration and
excitement, I ripped the slides apart and wrote this Python script:

    :::python
    import jinja2
    import markdown

    with open('presentation.html', 'w') as outfile:
        slides_src = markdown.markdown(open('slides.md').read()).split('<hr />\n')

        slides = []

        for slide_src in slides_src:
            header, content = slide_src.split('\n', 1)
            slides.append({'header': header, 'content': content})

        template = jinja2.Template(open('base.html').read())

        outfile.write(template.render({'slides': slides}))

I've always had a fascination with terse code. How few lines can I complete
a task in while maintaining clarity? That question that has guided my
programming for years. I think it's a worthwhile one. The above script is
a direct result of this goal. I was overjoyed that all my Python code for this
project could fit in a single slide.

Then I put the code on GitHub.

### Open-Source Success

I'm not sure how or why it happened, but Landslide started to gain traction a
few months after I open-sourced it.

As of this writing, I've accepted contributions from [33 people] who live all
over the world. 1,226 people have starred the project on GitHub, and it's been
installed over 23,000 times. I cannot overstate my appreciation for [GitHub]
and [PyPi]. These are some of the incredible tools that have made all of this
possible.

Looking back, I could have managed some aspects of Landslide better. I accepted
patches too quickly and let the code quality drop below my personal standards.
After a while, it didn't feel like my code anymore. Also, I let the
project languish for long periods of time.

I'm thankful for Landslide and all that it has taught me.

[PyPi]: https://pypi.python.org/pypi/landslide/
[Code]: https://github.com/adamzap/landslide
[Louisiana State University]: http://www.lsu.edu/
[Lightning Talks]: http://en.wikipedia.org/wiki/Lightning_talk
[Markdown]: http://daringfireball.net/projects/markdown/syntax
[html5slides]: https://code.google.com/p/html5slides/
[GitHub]: https://github.com/
[PyPi]: https://pypi.python.org/pypi
[33 people]: https://github.com/adamzap/landslide/graphs/contributors
