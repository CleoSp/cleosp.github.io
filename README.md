# Cleo Spiers

Personal website for [cleospiers.com](https://cleospiers.com)

## Content

- `index.html`: biography, employment, document links, writing, and photo previews.
- `photography.html`: photography gallery.
- `style.css`: shared typography and layout.
- `assets/`: PDFs and web-sized photographs.

Navigation is repeated in all three HTML pages. Update each when adding a page.
Keep content-page links relative so the site also works when opened locally.
The 404 page uses root-relative links so it works at any missing URL depth.

## Search, sharing, and accessibility

Pages contain their full content in HTML, including with JavaScript disabled or
in View Source. Each page has a unique title, description, canonical URL,
English language attribute, and one H1. Photographs have descriptive alt text.
Public content pages also include Open Graph and Twitter metadata and JSON-LD
structured data. The opening skateboard photograph is the social preview image.

`favicon.svg` and `favicon.ico` provide the CS monogram. `robots.txt` advertises
`sitemap.xml`; add new canonical content pages to the sitemap and `llms.txt`.
`404.html` is the GitHub Pages error document and is marked noindex.

CSS is served directly without minification. Its line-level source map embeds
the original stylesheet for developer tools. After editing `style.css`, run
`python scripts/update-source-map.py` and commit the refreshed `style.css.map`.
There is no executable JavaScript requiring a JavaScript source map.

## Local preview

Open `index.html` directly

## Publishing

GitHub Pages serves the root of the `main` branch. Push changes to `main` to
publish them. `CNAME` contains the custom domain, and `.nojekyll` keeps the
site entirely static.

Images have small and large JPEG versions, responsive dimensions, and sRGB
color profiles. Preserve their aspect ratios when adding or replacing photos.
The upright final portrait uses JPEG orientation metadata.

The writing and photographs remain the work of Cleo Spiers; no reuse license
is granted by the public availability of this repository.
