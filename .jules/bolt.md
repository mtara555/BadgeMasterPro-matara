## 2024-04-28 - Debouncing heavy UI updates in IIFE-wrapped single-file app

**Learning:** In a single-file application where the main logic is wrapped in an IIFE, functions called from HTML `oninput` or `onchange` attributes must be explicitly attached to the `window` object. Performance-heavy operations like DOM rendering and IndexedDB queries triggered by search inputs or slider movements can cause UI lag if not debounced.

**Action:** Always implement a `debounce` utility and expose debounced versions of search, filter, and size-adjustment functions on the `window` object when they are called from HTML event attributes.
