

function togglenav() {
    var x = document.getElementById("nav"); 
    //selecting our contact form+
      if (x.style.transform == "translateY(-60px)") { //transition for navbar
        x.style.transform = "translateY(0px)"
        x.style.transition = ".5s ease-in-out"
      }
      else {
        x.style.transform = "translateY(-60px)"
        x.style.transition = ".5s ease-in"
      }

    }
  


var btnContainer = document.getElementById("nav");
var button = btnContainer.getElementsByClassName("button");



for (var i = 0; i <button.length; i++) {
    button[i].addEventListener("click", function() {
        var current = document.getElementsByClassName("active");
        current[0].className = current[0].className.replace(" active", "")
        this.className += " active";
    })   
}

var pageindex = 1;
homepages(pageindex);

function nextpage(n) {
    homepages(pageindex=n);
}

function homepages(n) {
    var pages = document.getElementsByClassName("container");
    if (n > pages.length) {pageindex = 1};
    if (n < 1) {pageindex = pages.length};
    for (i = 0; i <pages.length; i++) {
        pages[i].style.display = "none";
    }
    pages[pageindex - 1].style.display = "block";
}

var formbox = document.getElementById("formcontainer")
var formbtn = document.getElementsByClassName("formopen")

var contactme = document.getElementById("formpopup")


function formdisplay() {
  if (formbox.style.transform == "translateY(100vh)") {
    formbox.style.transform = "translateY(0vh)";
    formbox.style.transition = ".5s ease-in"
  } else {
    formbox.style.transform = "translateY(100vh)"
    formbox.style.transition = ".5s ease-out"
  }

}

for (i=0; i < formbtn.length; i++) {
  formbtn[i].addEventListener("click", formdisplay)
}

