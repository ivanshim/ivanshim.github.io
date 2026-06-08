# AGENTS.md

Rules for future agents editing appliance data and pages.

## Data

- Store appliance data in `appliances.csv`.
- Keep the CSV headers exactly: `slug,image,title,description,source`.
- `slug` is the stable URL id and must match `/appliance/<slug>/`.
- `image` should be an absolute site path such as `/appliances/<image-file>`.
- `title` should follow `Country: Brand Model Type`.
- `description` should include the exact model number and meaningful variant notes.
- `source` should be the source URL.
- For split air conditioners, treat indoor and outdoor units as separate appliance pages when both model numbers matter. Example: `AN...` indoor unit and `AR...` outdoor unit.

## Pages

- `appliances/index.html` loads `appliances.csv` through `app.js` and renders the index.
- `/appliance/<slug>/index.html` files are lightweight JS shells. Do not duplicate appliance data in them.
- When adding a new CSV row, add the matching `/appliance/<slug>/index.html` shell so direct static URLs work.

## Images

- Store product images in `appliances/`.
- Prefer official manufacturer images; use a variant-matching image when the requested model has a specific color, hinge, size, or indoor/outdoor unit.
- When replacing a cached image, use a new descriptive filename and update `appliances.csv`.
