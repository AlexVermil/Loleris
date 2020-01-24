// 1. Get input values
const first = document.querySelector("#first");
const second = document.querySelector("#second");
const btn = document.querySelector("button");
const answer = document.querySelector("#answer");
// 2. Create calc function
function calc() {
    // 4. Display output to user
    answer.innerText = parseInt(first.value) + parseInt(second.value);
}
// 3. Add Event listener to button
btn.addEventListener("click", calc);