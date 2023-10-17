//----------ADD ITEM MODAL----------
//AddGame FORM VALIDATION
function validateForm() {
    let x = document.forms["GameForm"]["Name"].value;
    if (x == "") {
        alert("The name of the item must be filled out.");
        return false;
    }
}
//STICKY ADDGAME FORM
function openaddGame(){
    document.getElementById("add-item").style.display = "block";
}

function closeForm() {
    document.getElementById("add-item").style.display = "none";
}

//CLOSE FORM IF USER CLICKS OUTSIDE THE CONTACT-CONTAINER WINDOW
document.addEventListener("click",
    function(event){
        if (
          event.target.matches("#add-item")
          )
          {closeForm()}
        }
);

//SHOW GAME LIBRARY AS A TABLE
function showHideElement() {
    //document.getElementById("gameLibraryTable").style.width="100%";
    var peekaboo = document.getElementById("gameLibraryTable");
    if (peekaboo.style.display === "none") {
        peekaboo.style.display = "table";   //Ensure you choose the appropriate display option, i.e. block, inline, table, etc.
        var text = document.getElementById("showHideElement").innerHTML ="&nbsp;Hide List&nbsp;";
    }
    else {
        peekaboo.style.display = "none";
        var text = document.getElementById("showHideElement").innerHTML ="Show List";
    }
}
//----------ADD ITEM MODAL----------


//----------DELETE ITEM MODAL----------
//DELETE FORM modal
function opendeletemodal(){
    document.getElementById("delete-item").style.display = "block";
}

function closedeletemodal() {
    document.getElementById("delete-item").style.display = "none";
}

//CLOSE FORM IF USER CLICKS OUTSIDE THE CONTACT-CONTAINER WINDOW
document.addEventListener("click",
    function(event){
        if (
          event.target.matches("#delete-item")
          )
          {closedeletemodal()}
        }
);
//----------DELETE ITEM MODAL----------
