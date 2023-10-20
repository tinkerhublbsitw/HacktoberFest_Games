const compChoiceDisplay = document.getElementById('computer-choice')
const userChoiceDisplay = document.getElementById('user-choice')
const resultDisplay = document.getElementById('result')
const userScoreDisplay= document.getElementById('user-score')
const computerScoreDisplay= document.getElementById('computer-score')
const possibleChoices = document.querySelectorAll('.choice-button')
let userChoice
let computerChoice
let result
let computerScore = 0
let userScore = 0
possibleChoices.forEach(possibleChoice => possibleChoice.addEventListener('click', (e) => {
    userChoice=e.target.id
    userChoiceDisplay.innerHTML= userChoice
    generateComputerChoice()
    getResult()
}))

function generateComputerChoice()
{
    const randomNumber=Math.floor(Math.random() * possibleChoices.length)
    if(randomNumber === 0)
    {
            computerChoice='Rock'
    }
    if(randomNumber === 1)
    {
            computerChoice='Scissors'
    }
    if(randomNumber === 2)
    {
            computerChoice='Paper'
    }
    compChoiceDisplay.innerHTML=computerChoice
}

function getResult() 
{
    if (computerChoice === userChoice) {
        result = "Tie!";
    } else if (computerChoice === 'Rock' && userChoice === 'Scissors') {
        result = "You lose!";
        computerScore++
    } else if (computerChoice === 'Scissors' && userChoice === 'Paper') {
        result = "You lose!";
        computerScore++
    } else if (computerChoice === 'Paper' && userChoice === 'Rock') {
        result = "You lose!";
        computerScore++
    } else {
        result = "You win!";
        userScore++
    }
    computerScoreDisplay.innerHTML=computerScore
    userScoreDisplay.innerHTML=userScore
    resultDisplay.innerHTML=result
}
