## 2026-05-06 - [IndexedDB Memory Management]
**Learning:** Using `getAll()` on stores containing large base64 strings (like photos) causes high memory pressure and risk of crashes in single-file PWA applications.
**Action:** Always prefer `openCursor()` for iterations or `openKeyCursor()` on indexes for counting to keep the memory footprint constant regardless of dataset size.
