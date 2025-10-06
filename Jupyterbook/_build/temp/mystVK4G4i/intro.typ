// Created with jtex v.1.0.20
#import "lapreprint.typ": *
#show: template.with(
  title: "Introduction",
  abstract: (
    (
      title: "Abstract",
      content: [
This is my abstract!
      ]
    ),
  ),
  date: datetime(
    year: 2025,
    month: 10,
    day: 2,
  ),
  keywords: ("jupyter-book","something-else",),
  authors: (
    (
      name: "captain jupyter",
    ),
  ),
  affiliations: (
  ),
  margin: (
  ),
)

#import "myst-imports.typ": *

/* Written by MyST v1.6.0 */

I am a book about ... something! Wikipedia has #link("https://en.wikipedia.org/wiki/book")[information about books]: hover over the link for more information.

// An admonition containing a note

#noteBlock[
Books are usually written on paper ... But Jupyter Book can create _websites_!
]

If you sold 100 books at \$10 per book, you'd have \$1000 dollars according to #link(<eq:book>)[(1)]. If instead you publish your Jupyter Book to the web for free, you'd have \$0 dollars!

// An arbitrary math equation

$ x times y = z $ <eq:book>
Sometimes when reading it is helpful to foster a _tranquil_ environment. The image in #link(<fig:mountains>)[Figure~1] would be a perfect spot!

// A figure of a photograph of some mountains, followed by a caption

#show figure: set block(breakable: breakableDefault)
#figure(
  image("files/e18f93c1a505d76c1d42cf6b874a6a0d.png", width: 90%),
  caption: [
A photograph of some beautiful mountains to look at whilst reading.
],
  kind: "figure",
  supplement: [Figure],
) <fig:mountains>
