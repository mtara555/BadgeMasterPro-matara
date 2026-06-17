## 2025-05-14 - [Debounce for High-Frequency Events]
**Learning:** In a single-file application where the logic is wrapped in an IIFE, functions used in HTML `oninput` or `onclick` attributes must be explicitly exposed to the `window` object. High-frequency events like `oninput` on text fields and range sliders were causing excessive executions of expensive operations (QR code generation, DOM filtering), leading to UI lag.
**Action:** Implement a `debounce` utility and apply it to all `oninput` handlers that trigger expensive operations. Ensure the debounced wrappers are exposed on `window`.
