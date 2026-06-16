## 2026-06-16 - [Initial Journal]
**Learning:** The application uses IndexedDB's `getAll()` extensively, even when only a subset of data or just counts are needed. This is particularly problematic for the 'badges' store because records contain large base64-encoded photos.
**Action:** Identify and replace high-impact `getAll()` calls with cursors or key cursors, and implement debouncing for search inputs.
