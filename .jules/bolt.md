## 2026-04-30 - Debouncing high-frequency UI updates
**Learning:** In single-file HTML applications with complex UI interactions, rapid input events (oninput) can trigger expensive operations like QR code generation and list filtering, leading to UI stuttering.
**Action:** Use a `debounce` utility to limit the rate of these operations. Ensure that debounced functions exposed on `window` are initialized after the original functions are fully defined (e.g., using `setTimeout(..., 0)` inside an IIFE).
