# AGENTS.md

Rules for future agents editing appliance data and pages.

## Data

- Store appliance data in `appliances.csv`.
- Keep the CSV headers exactly: `slug,image,title,description,source`.
- `slug` is the stable URL id and must match `/appliances/#<slug>`.
- `image` should be the image filename only, for example `<image-file>`.
- `title` should follow `Country: Brand Model Type`.
- `description` should include the exact model number and meaningful variant notes.
- `source` should be the source URL.
- For split air conditioners, treat indoor and outdoor units as separate appliance pages when both model numbers matter. Example: `AN...` indoor unit and `AR...` outdoor unit.

## Pages

- `appliances/index.html` loads `appliances.csv` through `app-router-20260608.js` and renders both the index and hash-routed detail views.
- Detail URLs use `/appliances/#<slug>`.
- Do not add per-appliance HTML or Markdown pages; the CSV is the appliance data source.

## Images

- Store product images in `appliances/`.
- Prefer official manufacturer images; use a variant-matching image when the requested model has a specific color, hinge, size, or indoor/outdoor unit.
- When replacing a cached image, use a new descriptive filename and update `appliances.csv`.
