## 2025-07-02 - [Optimized IndexedDB badge counting]
**Learning:** Using `getAll()` on a store where objects contain large base64 photos is a major performance bottleneck in IndexedDB, as it forces the browser to load and deserialize the entire payload even when only a count or a specific property is needed.
**Action:** Use `openKeyCursor()` on a relevant index to perform counts or groupings without fetching full object payloads. Always include a fallback to `getAll()` or similar if the index is missing to ensure robustness across different database versions.
