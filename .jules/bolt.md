## 2026-05-20 - Prevent Redundant Asynchronous Renders via Debouncing
**Learning:** In this application, `updateBadgePreview` uses an internal 20ms `setTimeout` for QR code generation. Rapid, non-debounced calls to this function caused multiple QR codes to be instantiated and appended/rendered before previous ones finished, leading to UI flicker and excessive resource consumption.
**Action:** Always debounce functions that trigger asynchronous DOM updates or external library calls (like QRCode.js) in high-frequency events (`oninput`, `onscroll`, etc.) to ensure a single, stable render cycle.
