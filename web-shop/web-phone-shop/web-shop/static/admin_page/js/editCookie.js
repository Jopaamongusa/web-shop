
let listButtonImage = document.querySelectorAll(".edit-img")

console.log(listButtonImage)
for (let count = 0; count < listButtonImage.length; count++) {
    let button = listButtonImage[count]
    button.addEventListener(
        type = "click",
        listener = (event) => {
            console.log('img')
            event.preventDefault();
            document.querySelector(".modal-window").style.display = "flex"
            let inputData = document.querySelector(".input-data")
            inputData.type = "file" 
            inputData.accept = "image/*"
            inputData.name = "image"
            document.querySelector(".modal-label").textContent= "Оберіть нове зоображення:"
            document.querySelector('.change-submit').value = `0-${button.id}`
        }
    )
}

let listButtonName = document.querySelectorAll(".edit-text")
console.log(listButtonName)
for (let count = 0; count < listButtonName.length; count++) {
    let button = listButtonName[count]
    button.addEventListener(
        type = "click",
        listener = (event) => {
            console.log('text')
            event.preventDefault();
            document.querySelector(".modal-window").style.display = "flex"
            let inputData = document.querySelector(".input-data")
            inputData.type = "text"
            inputData.placeholder = "Введіть нову назву продукту"
            if(button.name === "name"){
                document.querySelector(".modal-label").textContent= "Задайте нову назву продукту:"
                document.querySelector('.change-submit').value = `1-1-${button.id}`
                inputData.name = "name"
            }
            if(button.name === "price"){
                document.querySelector(".modal-label").textContent= "Задайте нову ціну продукту:"
                document.querySelector('.change-submit').value = `1-2-${button.id}`
                inputData.name = "price"
            }
            if(button.name === "description"){
                document.querySelector(".modal-label").textContent= "Задайте нову опис продукту:"
                document.querySelector('.change-submit').value = `1-3-${button.id}`
                inputData.name = "description"
            }
            if(button.name === "count"){
                document.querySelector(".modal-label").textContent= "Задайте нову кількість товару:"
                document.querySelector('.change-submit').value = `1-4-${button.id}`
                inputData.name = "count"
            }ю 
        }
    )
}

let listButton = document.querySelectorAll('.modal-window-add-button')
console.log(listButton)
console.log(200)
for (let count = 0; count < listButton.length; count++) {
    let button = listButton[count]
    console.log(200)
    button.addEventListener(
        type = "click",
        listener = (event) => {
            event.preventDefault();
            document.querySelector(".modal-window-add").style.display = "flex"
            console.log(200)
            
        }
    )
}