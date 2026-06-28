## 2025-05-15 - IndexedDB Cursor Optimization
**Learning:** Loading large objects (e.g., base64 photos) from IndexedDB via `getAll()` significantly blocks the main thread and consumes excessive memory, even if only one field is needed. Using `openKeyCursor` on an index allows iterating over just the required keys/values without fetching the full record payload.
**Action:** Prefer `openKeyCursor` or `getAllKeys` on indexes when only counts or specific IDs are needed from stores containing large data blobs.
