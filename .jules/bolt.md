## 2025-05-24 - [IndexedDB Schema and Performance]
**Learning:** Performance optimizations relying on IndexedDB indices will crash the application if the indices aren't present in the schema. Simply adding index creation to the `v0->v1` migration path is insufficient for existing users who already have the database at `v1` or `v2`.
**Action:** Always increment the database version and add explicit migration logic in `onupgradeneeded` to create missing indices for existing stores. Additionally, implement defensive checks using `store.indexNames.contains('indexName')` and provide fallbacks to ensure the app remains functional even if migrations fail or indices are missing.

## 2025-05-24 - [Memory Pressure from Large Payloads]
**Learning:** Using `getAll()` on object stores containing large base64-encoded photos causes significant memory pressure and slows down UI updates, even when just counting records.
**Action:** Use `openCursor()` or `openKeyCursor()` (on an index if possible) to iterate over records without loading the full object payloads into memory when full data isn't needed (e.g., for statistics or filtered counts).
