const header = document.querySelector('header');
const eleHeader = document.getElementById('toggle_header');

eleHeader.addEventListener("click", function() {
  const currentClass = header.classList.value;

  let newClass;
  if (currentClass === "red") {
    newClass = "green";
  } else {
    newClass = "red";
  }

  header.classList.remove(currentClass);
  header.classList.toggle(newClass);
});
