## 2026-04-25 - [Debounced expensive input handlers]
**Learning:** High-frequency 'oninput' events in this single-file app were triggering expensive DOM rebuilds and QR code generations, causing lag during typing.
**Action:** Use a 'debounce' utility and expose debounced wrappers on the 'window' object to remain accessible from HTML attributes when the script is wrapped in an IIFE.
