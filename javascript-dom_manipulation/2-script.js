/*eslint-disable*/
document.addEventListener('DOMContentLoaded', () => {
  const elementRed = document.getElementById('red_header');
  const header = document.querySelector('header');

  elementRed.addEventListener('click', () => {
    header.classList.add('red');
  })
})