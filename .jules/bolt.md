## 2025-05-18 - [IndexedDB Memory Bottleneck in updateStats]
**Learning:** The `updateStats` function uses `tx.objectStore('badges').getAll().onsuccess` to count badges with photos (`e.target.result.filter(b=>b.photo).length`). Since badges often contain high-resolution base64 photo data, loading ALL badge objects into memory just to count them is a major performance and memory bottleneck as the database grows.
**Action:** In future optimizations, replace `getAll()` with a `count()` on a dedicated index (e.g., a 'hasPhoto' index) or use a cursor that only fetches the necessary property, avoiding the loading of large blobs into memory.

## 2025-05-18 - [Debouncing Global Functions in IIFEs]
**Learning:** When debouncing functions that are both used internally and exposed on the `window` object within an IIFE, the debounced version must be assigned back to the same variable name and the `window` property to ensure consistency across both internal script calls (like `refreshAll`) and HTML event handlers.
**Action:** Use the pattern `var func = debounce(function(){...}, wait); window.func = func;` inside the IIFE scope.
