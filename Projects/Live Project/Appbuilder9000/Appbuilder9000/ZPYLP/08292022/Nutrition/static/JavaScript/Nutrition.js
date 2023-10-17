// $(document).ready(function() {
//     $("#cf_onclick").click(function() {
//         $("#cdf2 img.top").toggleClass("transparent");
//     });
// });


function swole() {
    var weak = document.getElementById("top");
    var strong = document.getElementById("bottom");
    if (weak.style.display == "block") {
        weak.style.display = "none";
        strong.style.display = "block";
    }
    else {
        weak.style.display = "block";
        strong.style.display = "none";
    }
}