var roster = []


function addName(){
  var newName = prompt("please enter the name")
  roster.push(newName)
}

function remove(){
  var remName = prompt("please enter the name u wanna remove")
  var index = roster.indexOf(remName)
  roster.splice(index,1)
}

function display(){
  console.log(roster);
}

var x = prompt("would you like to start the roster? y or n")
//var request = "empty"
if(x === 'y'){
  while (response !== "quit") {
    var response = prompt("please enter the operation: add , remove, display, quit")
    if(response === "add"){
      addName();
    }
    else if (response === "remove") {
      remove();
    }
    else if (response === "display") {
      display();
    }

      //request = "quit"
    }
  }

  alert("thank yoy for using the app! please refresh to start over")
