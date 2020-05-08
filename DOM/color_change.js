// generate random color hex code
var header = document.querySelector("h1")
header.style.color = "red"

function getRandomColor(){
  var letters = "0123456789ABCDEF"
  var color = "#"
  for(var i = 0; i < 6; i++){
    color += letters[Math.floor(Math.random()*16)]
  }
  return color
}
// assign the color

function changeHeaderColor(){
  colorInput = getRandomColor()
  header.style.color = colorInput
}

// #set interval
setInterval("changeHeaderColor()",500)
