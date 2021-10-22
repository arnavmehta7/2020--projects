function ageInDays() {
    let birthyear = (prompt("Enter Your Date Of Birth: "));
    let days = (2021 - (birthyear)) * 365;
    console.log(`${days} is the current Days`);
    var h = document.createElement('h1');
    let text = document.createTextNode((`You are ${days} days old`));
    console.log(typeof (text));
    h.setAttribute("id", "ageInDays");
    console.log(h);
    h.appendChild(text);
    document.getElementById('flex-box-days-result').appendChild(h);



    let years = (2021 - (birthyear));
    let heading2 = document.createElement('h1');
    let text2 = document.createTextNode(`You are ${years} years Old!.`);
    heading2.setAttribute('id', 'ageInyears');
    heading2.appendChild(text2);
    document.getElementById('flex-box-years').appendChild(heading2);
}

function reset() {
    document.getElementById('ageInDays').remove();
    document.getElementById('ageInyears').remove();

}

function generateCat() {
    let image = document.createElement('img');
    let div = document.getElementById('flexcat');
    image.src = 'https://thecatapi.com/api/images/get?format=src&type=gif&size=small';
    div.appendChild(image);
}

function rpsGame(choice) {
    console.log(choice);
    let humanChoice, botChoice;
    humanChoice = choice.id;
    botChoice = NumberToChoice();
    console.log('Computer Choice:', botChoice);
    results = decideWinner(humanChoice, botChoice);
    console.log('Result:',results);
    message = finalMessage(results); // return a dictionary
    console.log('Message: ',message);
    rpsFrontend(choice.id,botChoice,message);


}

function NumberToChoice() {
    let num = (Math.floor(Math.random() * 3));
    return ['Rock', 'Paper', 'Scissors'][num];
}

function decideWinner(choice, botChoice) {
    let rpsData = {
        'Rock': {
            'Scissors': 1,
            'Rock': 0.5,
            'Paper': 0
        }, // someone picks paper u lose, rock then tie
        'Paper': {
            'Scissors': 0,
            'Rock': 1,
            'Paper': 0.5
        },
        'Scissors': {
            'Scissors': 0.5,
            'Rock': 0,
            'Paper': 1
        }
    }
    let yourScore = rpsData[choice][botChoice];
    let botScore = rpsData[botChoice][choice];
    return [yourScore, botScore];
}

function finalMessage([yourScore, botScore]) {
    if (yourScore === 0) {
        return {'message': 'You Lost','color': 'red'};
    }
    else if (yourScore === 0.5) {
        return {'message': 'Tie','color': 'yellow'};
    }
    else{
        return {'message': 'You Won! Wooo!','color': 'green'};
    }
} 

function rpsFrontend(humanImageChoice,botImageChoice,finalMessage){
    let imagesData = {
        'Rock':document.getElementById('Rock').src,
        'Paper':document.getElementById('Paper').src,
        'Scissors':document.getElementById('Scissors').src
    };
     
    //Remove ALl the images
    document.getElementById('Rock').remove();
    document.getElementById('Paper').remove();
    document.getElementById('Scissors').remove();
    
    
    let humanDiv = document.createElement('div');
    let botDiv = document.createElement('div');
    let messageDiv = document.createElement('div');
    humanDiv.innerHTML = "<img src='"+imagesData[humanImageChoice]+"'"+"height=200px style='box-shadow:10px 10px 30px blue;"+"'>";
    botDiv.innerHTML = "<img src='"+imagesData[botImageChoice]+"'"+"height=200px style='box-shadow:10px 10px 30px red;"+"'>";
//    humanDiv.innerHTML = `<img src='${imagesData[humanImageChoice]}'> style='box-shadow: 10px 5px 20px red;';
    
    console.log(humanDiv);
    document.getElementById('flexbox-rps-div').appendChild(humanDiv);
    document.getElementById('flexbox-rps-div').appendChild(botDiv);
    

}







