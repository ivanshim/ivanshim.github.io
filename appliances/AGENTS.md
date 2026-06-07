# AGENTS.md

Instructions for future agents editing files in `appliances/`.

## Appliance Page Pattern

- Store individual appliance pages directly in this directory as `<country>-<brand>-<model>.md`.
- Use lowercase hyphenated slugs for filenames and permalinks.
- Each appliance page must use front matter with:
  - `title: "Country: Brand Model Type"`
  - `permalink: /appliance/<slug>/`
- The page H1 must match the title.
- Store the product image in this directory beside the Markdown file.
- Reference local images with absolute site paths such as `/appliances/<image-file>`.
- Include a short product description, model number, any important variant notes, and a source link.

## Naming And Labels

- Link labels and page titles should follow `Country: Brand Model Type`.
- Suffix the model number with the appliance type, for example `Microwave`, `Refrigerator`, `Washing Machine`, `Dehumidifier`, or `TV`.
- Keep country names in human-readable form in labels, even if filenames use country prefixes such as `jp-`.

## Index

- Keep `appliances/index.md` grouped by country under `## Japan`, `## Singapore`, and `## Uganda`.
- Add new appliance links under the matching country subheader.
- Keep links as root-relative permalinks, for example `/appliance/jp-sharp-re-tm18-w/`.

## Images

- Prefer official manufacturer product images when available.
- If a specific variant is requested, use an image matching that variant.
- When replacing an image that may be cached, use a new descriptive filename and update the Markdown image reference.
