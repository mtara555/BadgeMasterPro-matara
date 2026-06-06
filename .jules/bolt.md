## 2025-05-15 - Debouncing frequent event handlers
**Learning:** Profiling confirmed that `loadAllBadges` and `updateBadgePreview` were triggered on every keystroke (e.g., 9 times for a 9-character input), causing redundant DOM updates and IndexedDB queries.
**Action:** Implement a `debounce` utility and wrap performance-heavy global event handlers. Verified that this reduces executions to 1-2 per rapid input sequence.
