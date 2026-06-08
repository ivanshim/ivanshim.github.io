(async function () {
  const app = document.getElementById("app");
  const appliances = await loadAppliances();

  window.addEventListener("hashchange", () => renderRoute(app, appliances));
  renderRoute(app, appliances);
})();

async function loadAppliances() {
  const response = await fetch("/appliances/appliances.csv", { cache: "no-store" });
  if (!response.ok) {
    throw new Error("Unable to load appliances.csv");
  }
  return parseCsv(await response.text());
}

function parseCsv(text) {
  const rows = [];
  let row = [];
  let value = "";
  let quoted = false;

  for (let i = 0; i < text.length; i += 1) {
    const char = text[i];
    const next = text[i + 1];

    if (quoted) {
      if (char === '"' && next === '"') {
        value += '"';
        i += 1;
      } else if (char === '"') {
        quoted = false;
      } else {
        value += char;
      }
    } else if (char === '"') {
      quoted = true;
    } else if (char === ",") {
      row.push(value);
      value = "";
    } else if (char === "\n") {
      row.push(value);
      rows.push(row);
      row = [];
      value = "";
    } else if (char !== "\r") {
      value += char;
    }
  }

  if (value || row.length) {
    row.push(value);
    rows.push(row);
  }

  const headers = rows.shift();
  return rows.filter(Boolean).map((values) =>
    Object.fromEntries(headers.map((header, index) => [header, values[index] || ""]))
  );
}

function renderRoute(app, appliances) {
  const slug = getDetailSlug();
  if (slug) {
    renderDetail(app, appliances, slug);
  } else {
    renderIndex(app, appliances);
  }
}

function getDetailSlug() {
  return decodeURIComponent(window.location.hash.replace(/^#\/?/, ""));
}

function renderIndex(app, appliances) {
  document.title = "Appliances";
  app.replaceChildren(element("h1", "Appliances"));

  const groups = new Map();
  appliances.forEach((appliance) => {
    const country = appliance.title.split(":")[0] || "Other";
    if (!groups.has(country)) {
      groups.set(country, []);
    }
    groups.get(country).push(appliance);
  });

  ["Japan", "Singapore", "Uganda"].forEach((country) => {
    const section = document.createDocumentFragment();
    section.append(element("h2", country));

    const list = element("ul");
    (groups.get(country) || []).forEach((appliance) => {
      const item = element("li");
      const link = element("a", appliance.title);
      link.href = `/appliances/#${encodeURIComponent(appliance.slug)}`;
      item.append(link);
      list.append(item);
    });
    section.append(list);
    app.append(section);
  });
}

function renderDetail(app, appliances, slug) {
  const appliance = appliances.find((item) => item.slug === slug);
  if (!appliance) {
    document.title = "Appliance not found";
    app.replaceChildren(element("h1", "Appliance not found"), element("p", slug));
    return;
  }

  document.title = appliance.title;
  const title = element("h1", appliance.title);
  const image = element("img");
  image.className = "appliance-image";
  image.src = appliance.image;
  image.alt = appliance.title;

  const description = element("p", appliance.description);
  const source = element("p");
  const sourceLink = element("a", "Source");
  sourceLink.href = appliance.source;
  sourceLink.rel = "noopener";
  source.append("Source: ", sourceLink);

  const back = element("a", "Back to appliances");
  back.className = "back-link";
  back.href = "/appliances/";

  app.replaceChildren(title, image, description, source, back);
}

function element(tag, text) {
  const node = document.createElement(tag);
  if (text !== undefined) {
    node.textContent = text;
  }
  return node;
}
