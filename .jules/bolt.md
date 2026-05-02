## 2025-05-15 - Debouncing for Performance
**Learning:** Overwriting window-exposed functions with debounced versions at the end of an IIFE allows HTML event handlers (oninput) to benefit from reduced execution frequency while maintaining synchronous internal logic for script-based calls. This prevents race conditions in sequences like `refreshAll()`.
**Action:** Always apply debouncing at the end of the script, targeting the `window` object properties rather than local function declarations to preserve internal consistency and avoid race conditions.
