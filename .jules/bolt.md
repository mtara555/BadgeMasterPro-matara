## 2024-05-21 - Debouncing IIFE-wrapped functions
**Learning:** In a single-file application where functions are defined inside an IIFE and then exposed to the `window` object, debouncing must be applied to the local variable before (or during) assignment to `window` to ensure both internal calls and HTML event handlers (`oninput`) benefit from the optimization.
**Action:** Always wrap the local function reference with `debounce()` and then update both the local reference and the `window` property to maintain consistency.
