title: Bare Bible
date: 2015-04-10
index_date: 2010-2012

Bare Bible is a website that displays complete books of the Bible without any
features like verse numbers, headings, or cross references. It was released
sometime in 2010 or 2011.

- [Website]

### Inspiration

Measurement alters experience. I believe this idea applies to Bible text. The
chapter and verse boundaries we find in most Bibles today affect our view of
it. The same is true for the tiny letters and numbers interleaved throughout.
These things make Scripture seem more like a technical document than
a narrative. There is a place for both of these views, but I wanted to further
explore the latter.

Could I better understand the intent of Paul's letter to the Colossians if
I read it in this way? What would it be like to read the gospel of John in one
sitting without knowing exactly how much I have left? What if I didn't have
subheadings and chapter numbers to control the flow of the story? I was able to
investigate these scenarios and more with Bare Bible.

Crossway, my employer, has since released the [ESV Reader's Bible]. It's
a beautiful approach to the same concept. I had nothing to do with that, but
we do have a Reader's Mode in ESVBible.org and our mobile apps. [Bibliotheca]
is another exciting stab at it. I'm glad the same idea is showing up in
different places.

### Technical Details

The code that generates Bare Bible and the text on its pages is simple.

The text comes from an [old ESV API] for JavaScript that is no longer
documented but [still works]. If you look at the source of any book page on
Bare Bible, you will see that all I'm doing is stacking queries to this API.
Add a nice-looking stylesheet, and you get what I think is an enjoyable
Bible-reading experience.

A Python script feeds passage data to the excellent [Jinja2] template
engine to build the individual pages. Jinja2 has powered many of my side
projects over the years. It's a great tool!

[Website]: http://barebible.com
[ESV Reader's Bible]: https://www.crossway.org/bibles/esv-readers-bible-none-tru/
[Bibliotheca]: http://www.bibliotheca.co/
[old ESV API]: http://www.esvapi.org/
[still works]: http://www.gnpcb.org/esv/share/js/?action=doPassageQuery&passage=Genesis+1:1
[Jinja2]: http://jinja.pocoo.org/
