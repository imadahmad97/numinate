document.addEventListener("DOMContentLoaded", function() {
  const startButton = document.getElementById('startButton');
  const q1 = document.getElementById('q1');
  const options = document.getElementById('options');
  const makeComparisonButton = document.querySelector('#options button:nth-child(2)');
  const dataFormQuestion = document.getElementById('dataFormQuestion');

  startButton.addEventListener('click', function() {
    startButton.classList.add('fade-out');
    setTimeout(() => {
      startButton.style.display = 'none';
      q1.style.display = 'block';
      options.style.display = 'block';
      q1.style.opacity = 0;
      options.style.opacity = 0;
      setTimeout(() => {
        q1.classList.add('fade-in');
        options.classList.add('fade-in');
      }, 10);
    }, 400);
  });

  makeComparisonButton.addEventListener('click', function() {
    options.classList.add('fade-out');
    q1.classList.add('fade-out');
    q1.classList.remove('fade-in');
    options.classList.remove('fade-in');
    q1.style.opacity = 0;
    options.style.opacity = 0;
    setTimeout(() => {
      q1.style.display = 'none';
      options.style.display = 'none';
      document.getElementById('dataFormQuestionText').style.display = 'block';  // Changed this line
      document.getElementById('dataFormButtons').style.display = 'block';  // Changed this line
      document.getElementById('dataFormQuestionText').style.opacity = 0;  // Changed this line
      document.getElementById('dataFormButtons').style.opacity = 0;  // Changed this line
      setTimeout(() => {
        document.getElementById('dataFormQuestionText').classList.add('fade-in');  // Changed this line
        document.getElementById('dataFormButtons').classList.add('fade-in');  // Changed this line
      }, 10);
    }, 400);
  });
  
});

