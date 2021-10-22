console.log("Testing");
screen = document.getElementById('screen');
buttons = document.querySelectorAll('button');
let screenValue='';
console.log(buttons);

for(item in buttons){
    buttons[item].addEventListener('click',(e)=>{
                                   buttonText = e.target.innerText;
                                   console.log('Button TExt is ',buttonText)
        
        if(buttonText=='X'){
            buttonText = '*';
            screenValue += buttonText;
            screen.value=screenValue;
                                }
        
        else if(buttonText=='C'){
            screenValue = '';// this handles displaying;
            screen.value=screenValue; // stored values;
        }
        
        else if(buttonText=='='){
            screen.value = eval(screenValue);
        
        }
        
        else{
            screenValue += buttonText;
            screen.value=screenValue;
        }
                                   })
    console.log(buttons[item]);
}