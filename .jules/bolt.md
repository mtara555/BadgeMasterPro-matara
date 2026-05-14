## 2026-05-14 - Debouncing Global UI Handlers
**Learning:** In this single-file IIFE architecture, debouncing functions by overwriting their `window` assignments at the end of the script effectively targets event handlers in the HTML (which look up global scope) without breaking synchronous internal calls to the same functions.
**Action:** Use this pattern for future UI optimizations to maintain internal consistency while improving event-driven performance.
