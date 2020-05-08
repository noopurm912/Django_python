

var f_name =prompt("Enter your First Name: ")
var l_name =prompt("Enter your Last Name: ")
var age=prompt("Enter your age: ")
var height=prompt("Enter your height in cm: ")
var pet_name=prompt("Enter your pet Name: ")
alert("Thank you so much information")

//Logic

if((f_name[0]==l_name[0])&&(age>20 && age<30)&&(height>=170)&&(pet_name[pet_name.length-1]=="y"))
{
  console.log("you are a spy")
}
else {
  console.log("nothing for you")
}
