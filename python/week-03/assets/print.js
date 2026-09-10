// Expand answers for paper without saving or changing learner progress.
let printOpened = [];
let printActive = false;
window.addEventListener('beforeprint', () => {
  if (printActive) return;
  printActive = true;
  printOpened = [...document.querySelectorAll('details:not([open])')];
  printOpened.forEach((section) => { section.open = true; });
});
window.addEventListener('afterprint', () => {
  if (!printActive) return;
  printOpened.forEach((section) => { section.open = false; });
  printOpened = [];
  printActive = false;
});
