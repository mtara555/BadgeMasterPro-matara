## 2025-06-25 - [IndexedDB Memory & Search Optimization]
**Learning:** In applications using IndexedDB with large record values (e.g., base64 photos), `getAll()` on a store causes severe performance degradation and potential OOM crashes. Using `openKeyCursor` on an index is significantly faster for counting or grouping as it avoids loading the record value into memory.
**Action:** Always prefer `openKeyCursor` or `openCursor` over `getAll()` for large datasets. Use debouncing on text inputs that trigger database-heavy operations.
