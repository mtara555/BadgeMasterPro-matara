## 2025-05-08 - Debouncing Global Event Handlers
**Learning:** In a single-file application where event handlers are defined in HTML (e.g., `oninput="updateBadgePreview()"`), debouncing can be achieved by overwriting the function on the `window` object at the end of the script's IIFE. This ensures the UI remains responsive without breaking internal synchronous logic that relies on the local function definitions.
**Action:** Always verify if functions are called via HTML attributes or programmatically before deciding where to apply debouncing or throttling.
