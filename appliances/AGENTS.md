# AGENTS.md

Rules for future agents editing `appliances/`.

## Pages

- Store appliance pages directly in this directory as lowercase hyphenated Markdown files, usually `<country>-<brand>-<model>.md`.
- Use matching slugs and permalinks: `jp-daikin-an22zss-f.md` -> `/appliance/jp-daikin-an22zss-f/`.
- Front matter must include:
  - `title: "Country: Brand Model Type"`
  - `permalink: /appliance/<slug>/`
- The H1 must exactly match the title.
- Include a short description, exact model number, meaningful variant notes, and a source link.
- For split air conditioners, treat indoor and outdoor units as separate appliance pages when both model numbers matter. Example: `AN...` indoor unit and `AR...` outdoor unit.

## Index

- Keep `index.md` grouped under `## Japan`, `## Singapore`, and `## Uganda`.
- Add each new appliance link under the matching country.
- Link labels must match page titles.
- Use root-relative permalink links, for example `/appliance/jp-sharp-re-tm18-w/`.

## Images

- Store product images beside the Markdown page in this directory.
- Reference images with absolute site paths such as `/appliances/<image-file>`.
- Prefer official manufacturer images; use a variant-matching image when the requested model has a specific color, hinge, size, or indoor/outdoor unit.
- When replacing a cached image, use a new descriptive filename and update the Markdown reference.
