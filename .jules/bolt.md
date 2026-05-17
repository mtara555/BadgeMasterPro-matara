## 2025-05-14 - Debouncing UI Updates in Single-File HTML App
**Learning:** High-frequency event handlers (oninput) for DOM-heavy operations (like QR code generation and live previews) can cause significant UI stuttering when not debounced. In a single-file application where functions are exposed on the `window` object, debouncing can be applied by overwriting these global references at the end of the script's initialization.
**Action:** Use a `debounce` utility to wrap `oninput` handlers that trigger expensive DOM updates or database queries. For text inputs, 250ms is a good balance; for sliders (sizing), 100ms provides better responsiveness.

## 2025-05-14 - Verification of Debounced Functions via DOM Observation
**Learning:** Directly wrapping a debounced function to count calls may erroneously report the frequency of calls to the *debouncer* rather than the *execution* of the original logic.
**Action:** Use a `MutationObserver` in Playwright tests to count actual DOM updates to verify that debouncing is effectively reducing the frequency of UI renders.
