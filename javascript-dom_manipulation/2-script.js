const element = document.getElementById("red_header");
  element.addEventListener("click", function() {
    const addElement = document.querySelector("header");
      addElement.classList.add("red");
});