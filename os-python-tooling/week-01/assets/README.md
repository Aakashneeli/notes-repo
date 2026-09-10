# Shared teaching components

`course.css` supplies typography, responsive layout, print layout and accessible focus states.
`quiz.js` gives immediate feedback for one equal-word-count multiple-choice question per lesson.
Native `<details>` elements contain expected results and hint ladders.

Quiz attempts are deliberately not persisted as mastery. Progress lives in Markdown and demonstrated learning records. Each lesson is its own HTML page with shared local assets; no build step or CDN is needed. Print styling expands answer content where supported.
