## 2026-05-26 - [Debouncing Frequent UI and DB Updates]
**Learning:** In a single-file application with many inline HTML event handlers (oninput, onchange), updating the global (window) function references with debounced versions is an effective way to optimize performance across the entire UI without refactoring the HTML.
**Action:** When optimizing performance in legacy-style or single-file JS applications, use a debounce wrapper and re-assign to the window object to ensure both programmatic and user-triggered events are optimized.
