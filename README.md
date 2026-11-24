# Marginalia

A PDF library and annotator that runs entirely in your browser.

**Open it:** https://yosoybikash.github.io/marginalia/

- Keep PDFs in a library, sorted into categories
- Highlight, underline and strike through text, line by line, like a normal reader
- Margin notes, text boxes, pen, marker, shapes, stamps and a drawn signature
- Search inside a PDF, page thumbnails, and a list of all your marks
- Export the annotated PDF, or a Markdown / CSV summary of your notes
- Warm colour themes, including a dark one

## Privacy

Nothing is uploaded anywhere. Your PDFs and notes are stored in your own browser
(IndexedDB and localStorage) on your own computer. Everyone who opens the link gets
their own separate, private library. The site counts page visits with
[GoatCounter](https://www.goatcounter.com/), which uses no cookies and never sees your files. Use **Back up** to save your library to a file,
and **Restore** to bring it back or move it to another browser or computer.

## Offline use

`index.html` is a single self-contained file. You can download it and open it
directly, with no internet connection needed.

## Development

The readable source is `src/app.html`. `build.py` inlines PDF.js and pdf-lib into it
to produce `index.html`.

Built with [PDF.js](https://mozilla.github.io/pdf.js/) (Apache-2.0) and
[pdf-lib](https://pdf-lib.js.org/) (MIT).
