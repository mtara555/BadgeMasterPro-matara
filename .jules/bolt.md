## 2025-05-15 - [IndexedDB Object Bloat Bottleneck]
**Learning:** In applications storing large binary/base64 data (like photos) in IndexedDB, using `getAll()` causes severe performance degradation and memory pressure because the browser must deserialize the entire object body for every record, even if only a single property (like `eventId`) is needed.
**Action:** Use `openKeyCursor()` on indices to perform counts or key-only searches, or `openCursor()` to process records one-by-one, avoiding the allocation of a massive array of heavy objects.
