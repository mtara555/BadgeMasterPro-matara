## 2025-05-22 - Real-time UI Debouncing
**Learning:** Frequent `oninput` events for badge previews and search fields were triggering expensive operations (QR code generation, IndexedDB lookups, bulk DOM re-renders) on every keystroke. This congested the main thread and caused UI lag, especially on mobile or lower-end devices.
**Action:** Implement a `debounce` utility and wrap performance-heavy functions. Use 250ms for text inputs and search filters, and 100ms for layout/sizing sliders to maintain a balance between responsiveness and efficiency.
