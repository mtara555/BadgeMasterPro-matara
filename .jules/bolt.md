## 2025-05-14 - Scoping debounced functions in IIFE
**Learning:** Functions defined in an IIFE must be explicitly attached to `window` if they are to be used in HTML event attributes like `oninput`.
**Action:** Always expose debounced versions of internal functions on the `window` object when the application uses inline HTML handlers.
