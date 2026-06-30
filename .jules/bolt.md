## 2025-05-15 - IndexedDB Performance with Large Blobs
**Learning:** Using `getAll()` on an IndexedDB store where records contain large base64-encoded images (0.1MB+) causes significant UI jank and memory pressure, as the browser must deserialize and load every object into memory even for simple count or filter operations.
**Action:** Always use `openKeyCursor()` or `getAllKeys()` on an index when only counts or specific IDs are needed. Use `openCursor()` to process records iteratively when searching through large objects without loading them all at once.
