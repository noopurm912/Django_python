// Restart game button
var restart = document.querySelector("#b")

// Grabs all the squares
var squares = document.querySelectorAll("td")

// clear all the squares
function clearBoard(){
  for (var i = 0; i < squares.length; i++)
  {
    squares[i].textContent = ''
  }
}
// restart button

restart.addEventListener('click',clearBoard)

// check the square marker

function changeMarker(){
  if(this.textContent === ''){
    this.textContent = 'X'}

else if (this.textContent = 'X'){
  this.textContent = 'O'}
}


for (var i = 0; i <squares.length; i++)
{
  squares[i].addEventListener('click',changeMarker)
}

// for loop to add event listener to all the square
