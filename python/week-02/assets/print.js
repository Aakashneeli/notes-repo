// Expand answers for paper without saving or changing learner progress.
let printOpened = [];
window.addEventListener('beforeprint', () => {
  printOpened = [...document.querySelectorAll('details:not([open])')];
  printOpened.forEach((section) => { section.open = true; });
});
window.addEventListener('afterprint', () => {
  printOpened.forEach((section) => { section.open = false; });
  printOpened = [];
});
