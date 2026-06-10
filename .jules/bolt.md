## 2025-05-22 - IndexedDB getAll() Bottleneck
**Learning:** IndexedDB `getAll()` on stores with large objects (base64 photos) loads everything into a single JS array, causing memory pressure and blocking the main thread.
**Action:** Use `openKeyCursor` on indexes for counts and filtered `getAll` on indexes to minimize data transfer.
