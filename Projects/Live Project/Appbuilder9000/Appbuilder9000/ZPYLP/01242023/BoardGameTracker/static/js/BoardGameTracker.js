// assign modal variable
var modal = document.getElementById("bgtModal");

// assign button to open modal
var btn = document.getElementById("modalBtn");

// create close button for modal
var span = document.getElementsByClassName("modalClose")[0];


// click button to open modal
btn.onclick = function() {
    modal.style.display = "block";
}

// close modal when user clicks close button
span.onclick = function() {
    modal.style.display = "none";
}



// close modal when user clicks outside modal
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

