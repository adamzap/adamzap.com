title: Chords
date: 2015-04-01
index_meta: iOS / Python

![Chords](/media/chords.jpg)

Chords is a free guitar chord reference app for the iPhone. It's initial
release was in 2008. Since then it has been downloaded millions of times.

- [App Store]

### Backstory

I remember looking for guitar chord apps on the iOS App Store when it launched
in July of 2008. They were all charging a dollar or two for information that
was free online. This frustrated me. Features like progression composition and
listening to chord sounds are worth charging for, but I thought a simple
reference should be free. So I set out to create a free guitar chords app.

I was excited to use Xcode and any other Apple tool I could get my hands on.
I had dabbled in Mac development before by creating a guitar tab management app
using [Core Data].

Objective-C was equal parts scary and exciting, but I was able to get
everything working like I wanted. Of course, Python was part of my toolchain
as well. Read on for more about how I used it.

I released Chords v1.0 in the App Store in October of 2008.

### iOS 7

The release of iOS 7 in September of 2013 broke Chords, and I had no idea.
I hadn't touched the code in almost five years, so I rewrote it from scratch.
iOS programming had changed a lot since 2008, but it was a positive experience.
I also used this opportunity to fix a few erroneous chord diagrams and improve
the aesthetics of the images I was generating.

I released Chords v2.0 on November 20, 2013.

### Technical Details

Chords is almost as simple as an iOS app can be: a PickerView and an image. The
app is merely a shell though. The real value is in the chord diagrams.

I got the chord data online and put in an easily-parsable format. The 336
images were then stitched together with a Python script that makes heavy use of
the [Python Imaging Library] (now deprecated in favor of [Pillow]). That script
is only 70 lines long.

[Core Data]: http://en.wikipedia.org/wiki/Core_Data
[App Store]: https://itunes.apple.com/us/app/chords/id295004203
[Python Imaging Library]: http://www.pythonware.com/products/pil/
[Pillow]: https://pillow.readthedocs.org/
