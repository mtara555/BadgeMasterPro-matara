## 2026-07-08 - [Optimized loadEvents with openKeyCursor]
**Learning:** Using `getAll()` on IndexedDB stores with large payloads (like base64 photos) causes significant memory pressure and slows down rendering, even if only counts are needed. Using `openKeyCursor` on an index is much more efficient as it only loads the keys.
**Action:** Always prefer `openKeyCursor` or `getAllKeys` when full object payloads are not required, especially on stores known to contain large blobs or base64 strings.
