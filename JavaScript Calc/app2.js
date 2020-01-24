// 1. Get input values
const multiplier = document.querySelector("#multiplier");
const multiplicable = document.querySelector("#multiplicable");
const btn = document.querySelector("button");
const answer = document.querySelector("#answer");
// 2. Create calc function
function calc() {
    // 3. Display output to user
    answer.innerText = parseInt(multiplier.value) * parseInt(multiplicable.value);
}
// 4. Add Event listener to button
btn.addEventListener("click", calc);