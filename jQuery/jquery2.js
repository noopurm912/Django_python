$('h1').click(function(){
  $(this).text("i am changed")
})

//key press

$('input').eq(0).keypress(function(){
  // $('h3').toggleClass('turnBlue')
  // console.log(event)
  if (event.which === 13){
    $('h3').toggleClass('turnBlue')
  }
})

// on()

$('h1').on('dblclick',function(){
  $('this').toggleClass('turnBlue')
})
