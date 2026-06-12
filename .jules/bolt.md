## 2026-06-12 - [IndexedDB Query Optimization]
**Learning:** Using `getAll()` on a store that contains large binary/base64 data (like photos) causes a major performance bottleneck even if only metadata is needed. The browser must deserialize all objects, leading to high CPU and memory usage.
**Action:** Use `openKeyCursor()` or `getAllKeys()` on specific indexes to count or filter records without loading the entire object payload. This is critical for stores like 'badges' where each record can be several hundred KB.
