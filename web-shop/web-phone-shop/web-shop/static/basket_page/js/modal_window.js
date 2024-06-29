let modal_window = document.querySelectorAll(".confirm")

for  (let count = 0; count < modal_window.length; count++ ){
    let window = modal_window[count]
    window.addEventListener(
        type = 'click',
        listener = (event) => {
            event.preventDefault();
            document.querySelector(".modal-window-div").style.display = "flex"
        }
    )
}

