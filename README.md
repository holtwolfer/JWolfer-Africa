# African Artifacts — GitHub Pages catalog

A static catalog generated from `Africa_Collection.pptx`. Original explicit catalog numbers are preserved. Unnumbered items remain unnumbered. Slides without photographs are included.

## Publish with GitHub Pages

1. Create a **public** GitHub repository (for example, `african-artifacts`).
2. Upload the **contents of this folder** to the repository root (not the ZIP file). For a large upload, use GitHub Desktop or Git instead of the browser.
3. In repository **Settings → Pages**, select **Deploy from a branch**, branch **main**, folder **/(root)**, then save.
4. Visit `https://YOUR-USERNAME.github.io/african-artifacts/`.

## Preview locally

Run `python -m http.server 8000` inside this folder and open `http://localhost:8000`.

## Edit an artifact

Edit the corresponding object in `catalog.json`. The `number` field is null for unnumbered items. To add photographs, put JPEG files in `images/` and add their relative paths to that artifact's `images` array. The first image is the main gallery photo. Do not change the stable `id` field.

## Review before publishing

Text parsing from slides is automated and may need corrections, especially ambiguous culture/country fields and provisional attributions. Images are resized for web use. Public GitHub Pages sites and their images are publicly accessible. Check ownership, privacy, and any sensitive cultural material before publishing.
