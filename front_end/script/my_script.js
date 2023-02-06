console.log('inside my script js')

function showAlert(){
    window.alert('loaded')
}

// window.addEventListener("load", showAlert)

function changeHeaderToRed(){
    elem = document.getElementById('header_1')
    elem.style.color = 'red'
}

function swichColor(className){
    const elements = document.getElementsByClassName(className)

    for(let index = 0; index < elements.length; index++){
        const element = elements[index]
        let currClass = null
        newClass = null
        if (element.classList.contains('btn-outline-secondary')){
            currClass = 'btn-outline-secondary'
            newClass = 'btn-danger'
        } else {
            currClass = 'btn-danger'
            newClass = 'btn-outline-secondary'
        }
        element.classList.replace(currClass, newClass)
    }
}





