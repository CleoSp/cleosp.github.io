# Cleo Spiers

Personal website for [cleospiers.com](https://cleospiers.com), built with plain
HTML and CSS. No JavaScript, framework, package installation, or build step.

## Content

- `index.html`: biography, employment, document links, writing, and photo previews.
- `photography.html`: photography gallery.
- `style.css`: shared typography and layout.
- `assets/`: PDFs and web-sized photographs.

Navigation is repeated in both HTML pages. Update both when adding a page.
Keep links relative so the site also works when opened locally.

## Local preview

Open `index.html` directly, or run:

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

Then visit http://127.0.0.1:8000.

## Publishing

GitHub Pages serves the root of the `main` branch. Push changes to `main` to
publish them. `CNAME` contains the custom domain, and `.nojekyll` keeps the
site entirely static.

Images have small and large JPEG versions, responsive dimensions, and sRGB
color profiles. Preserve their aspect ratios when adding or replacing photos.
The upright final portrait uses JPEG orientation metadata.

The writing and photographs remain the work of Cleo Spiers; no reuse license
is granted by the public availability of this repository.
