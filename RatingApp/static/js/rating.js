
const firstStar = document.getElementById('star1')
const secondStar = document.getElementById('star2')
const thirdStar = document.getElementById('star3')
const fourthStar = document.getElementById('star4')
const fifthStar = document.getElementById('star5')



const selectionHandler = (selection) => {
    switch (selection) {
        case 'star1':{
            firstStar.classList.add('colored')
            secondStar.classList.remove('colored')
            thirdStar.classList.remove('colored')
            fourthStar.classList.remove('colored')
            fifthStar.classList.remove('colored')
            return
        }
        case 'star2':{
            firstStar.classList.add('colored')
            secondStar.classList.add('colored')
            thirdStar.classList.remove('colored')
            fourthStar.classList.remove('colored')
            fifthStar.classList.remove('colored')
            return
        }
        case 'star3':{
            firstStar.classList.add('colored')
            secondStar.classList.add('colored')
            thirdStar.classList.add('colored')
            fourthStar.classList.remove('colored')
            fifthStar.classList.remove('colored')
            return
        }
        case 'star4':{
            firstStar.classList.add('colored')
            secondStar.classList.add('colored')
            thirdStar.classList.add('colored')
            fourthStar.classList.add('colored')
            fifthStar.classList.remove('colored')
            return
        }
        case 'star5':{
            firstStar.classList.add('colored')
            secondStar.classList.add('colored')
            thirdStar.classList.add('colored')
            fourthStar.classList.add('colored')
            fifthStar.classList.add('colored')
            return
        }
    }

}

const arr = [firstStar, secondStar, thirdStar, fourthStar, fifthStar]

arr.forEach(item => item.addEventListener('mouseover', (event) =>{
    selectionHandler(event.target.id)
}))