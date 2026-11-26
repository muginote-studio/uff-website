# Website editing rules

- These are unofficial cafe design proposals. Keep the disclosures and illustrative-photo labels.
- Decorative icons must use inline SVG with a viewBox, explicit dimensions, currentColor and CSS sizing, or a CSS shape. Do not use Unicode stars, dingbats, emoji, variation selectors or arrow characters as visual icons.
- Do not rely on a text-presentation variation selector or font choice to fix an emoji. Replace the icon with a vector shape.
- Decorative SVGs require aria-hidden="true" and focusable="false". Meaningful icons need an accessible name or adjacent text.
- Keep body text readable and layouts responsive. Long names and addresses must not overflow.
- Before publishing, run python3 scripts/check_presentation.py and check any changed JavaScript syntax.
- Check desktop and narrow layouts. When available, inspect Safari/WebKit as well as Chromium, especially icons, fonts, forms and image cropping. If a browser is unavailable, state that visual/browser verification is incomplete.
- Preserve existing content and URLs unless the user asks to change them.
- Never invent store facts, contact details, prices, testimonials, bookings or sales activity.

