const next = document.getElementById('next');
const prev = document.getElementById('prev');
const text = document.getElementById('text');
let x = JSON.parse(document.getElementById('data').textContent); // x was string so converting it again
let quotes = JSON.parse(x);
let list = [];
let size = Object.keys(quotes).length;

for(let i = 0; i < size ; i++){
    list.push(quotes[i].fields.text);
}
list.sort();

let index = Math.floor(Math.random() * size);
text.innerText= list[index];

next.addEventListener('click', () => {
    if(index == size - 1)
        index = 0;
    else
        index++;

    text.innerHTML = list[index];
});

prev.addEventListener('click', () => {
    if(index == 0)
        index = size - 1;
    else
        index--;
    
    text.innerHTML = list[index];
})