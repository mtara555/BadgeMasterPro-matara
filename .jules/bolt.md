## 2026-06-02 - Debouncing performance-heavy UI updates
**Learning:** Functions that perform expensive DOM updates or heavy logic (like QR code generation via QRCode.js) triggered by 'oninput' events cause measurable UI jank and redundant operations. Debouncing these events significantly improves performance without sacrificing user experience.
**Action:** Always identify and debounce 'oninput' or 'onscroll' handlers that trigger expensive rendering or global data re-fetching.
