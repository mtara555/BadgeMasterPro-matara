## 2025-05-14 - [IndexedDB Payload Bottleneck]
**Learning:** Using `getAll()` on IndexedDB stores where records contain large payloads (e.g., base64 photos) causes significant memory pressure and slows down UI updates, even for simple operations like counting.
**Action:** Use `openKeyCursor()` on indexes when only the key is needed, or `openCursor()` to process records iteratively without loading the entire dataset into memory.
