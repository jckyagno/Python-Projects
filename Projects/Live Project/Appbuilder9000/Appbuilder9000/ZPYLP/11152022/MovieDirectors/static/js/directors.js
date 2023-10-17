var modal = document.getElementById("myModal");

var btn = document.getElementById("modalButton");

var cancel = document.getElementById("cancelButton");

if (modal && btn && cancel) {
    btn.onclick = function() {
        modal.style.display = "block";
    }

    cancel.onclick = function() {
        modal.style.display = "none";
    }

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }
}
