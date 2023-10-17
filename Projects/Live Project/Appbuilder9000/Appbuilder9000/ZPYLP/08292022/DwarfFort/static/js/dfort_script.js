

/*Delete Modal*/
var modal = document.getElementById("delete-modal");
var btn = document.getElementById("button-modal");
var close = document.getElementById("modal-close");


// listener for click on button to open the modal
if (document.getElementById("button-modal") !== null) {
    btn.onclick = function() {
        modal.style.display = "block";
    }
}

// listener for click on close button
if (document.getElementById("modal-close") !== null) {
    close.onclick = function() {
        modal.style.display = "none";
    }
}