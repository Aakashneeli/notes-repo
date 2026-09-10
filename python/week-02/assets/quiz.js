// Deliberately no persistence: demonstrated learning belongs in learning records.
document.querySelectorAll('[data-quiz]').forEach((quiz) => {
 const button = quiz.querySelector('button');
 button.addEventListener('click', () => {
  const picked = quiz.querySelector('input:checked');
  const output = quiz.querySelector('[role=status]');
  output.textContent = !picked ? 'Choose an answer first.' : picked.value === quiz.dataset.answer ? 'Correct. ' + quiz.dataset.explanation : 'Try again. ' + quiz.dataset.hint;
 });
});
