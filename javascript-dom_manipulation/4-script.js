const element = document.getElementById("add_item");
// const addElement = document.querySelector("my_list");
const ul = document.querySelector("ul");

function createItem() {
    let newItem = document.createElement("li");
    newItem.textContent = "Item";
    ul.appendChild(newItem);
}

element.addEventListener("click", createItem);