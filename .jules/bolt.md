## 2025-05-14 - IndexedDB Cursor vs getAll
**Learning:** Using `getAll()` on stores with large objects (e.g., base64 photos) causes significant performance degradation and memory pressure.
**Action:** Use `openKeyCursor()` on indexes for counting or `openCursor()` to iterate without loading all objects into memory at once.
