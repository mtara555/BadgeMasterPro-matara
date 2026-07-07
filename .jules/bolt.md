## 2025-05-14 - Optimized IndexedDB Badge Access
**Learning:** Using `getAll()` on the 'badges' store was a critical bottleneck because records contain large base64-encoded photos. This caused massive memory pressure and slow UI updates even for simple tasks like counting or filtering.
**Action:** Always prefer `openKeyCursor()` or `getAllKeys()` when full object data is not required. Use IndexedDB indices (`eventId`) for filtering to reduce the dataset before it reaches JavaScript.
