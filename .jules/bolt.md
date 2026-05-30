## 2026-05-30 - Optimize IndexedDB queries in loadEvents and selectAllBadges
**Learning:** Using `getAll()` on stores containing large base64 data (like photos) causes significant memory and CPU overhead. `openKeyCursor()` on indexes and `getAllKeys()` are much more efficient for counting and ID retrieval.
**Action:** Always prefer `openKeyCursor()` or `getAllKeys()` when full object data is not required, especially in stores with potential large blobs or base64 strings.
