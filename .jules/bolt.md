## 2025-05-15 - IndexedDB memory bottleneck with large base64 photos

**Learning:** Using `getAll()` on an IndexedDB object store that contains large base64-encoded strings (like photos) causes significant memory pressure and latency because the browser must deserialize and allocate memory for every single object in the store. This is especially problematic on mobile devices.

**Action:** When counting or filtering based on a specific field, use `openKeyCursor()` on an index to only load keys, or `openCursor()` to iterate and process one object at a time without loading the entire collection into memory at once.
