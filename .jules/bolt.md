## 2025-06-01 - [IndexedDB Payload Bottleneck]
**Learning:** Using `getAll()` on object stores containing large blobs or base64 strings (like badge photos) causes massive memory spikes and slow execution, as the entire dataset is loaded into the main thread.
**Action:** Use `openCursor()` for filtered counting or `openKeyCursor()` on indexes when only metadata/keys are needed to avoid loading the full object payloads.
