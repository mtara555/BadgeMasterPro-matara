## 2026-05-01 - [Debounce Optimization for High-Frequency Inputs]
**Learning:** In a single-file PWA like BadgeMaster Pro, high-frequency events like `oninput` for live previews and search can cause noticeable UI lag due to frequent DOM manipulations and IndexedDB queries. Debouncing these handlers is a high-impact, low-complexity optimization.
**Action:** Always check for `oninput` or `onmousemove` handlers in legacy/single-file JS projects and apply debouncing to those that trigger re-renders or data fetching.
