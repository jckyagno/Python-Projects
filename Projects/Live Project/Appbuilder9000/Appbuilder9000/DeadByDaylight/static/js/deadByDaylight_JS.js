var slideIndex = 1;
showSlides(slideIndex);
var slideIndex2 = 1;
showSlides2(slideIndex2);

//Next/previous controls
function plusSlides(n) {
    showSlides(slideIndex += n);
}

//Thumbnail image control
function currentSlide(n) {
    showSlides(slideIndex = n);
}
function showSlides(n) {
    var i;
    var slides = document.getElementsByClassName("mySlides");
    if (n > slides.length) {slideIndex = 1}
    if (n < 1) {slideIndex = slides.length}
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    slides[slideIndex-1].style.display = "block";
}


//Next/previous controls
function plusSlides2(n2) {
    showSlides2(slideIndex2 += n2);
}

//Thumbnail image control
function currentSlide2(n2) {
    showSlides2(slideIndex2 = n2);
}
function showSlides2(n2) {
    var i2;
    var slides2 = document.getElementsByClassName("mySlides2");
    if (n2 > slides2.length) {slideIndex2 = 1}
    if (n2 < 1) {slideIndex2 = slides2.length}
    for (i2 = 0; i2 < slides2.length; i2++) {
        slides2[i2].style.display = "none";
    }
    slides2[slideIndex2-1].style.display = "block";
}
function PreviewCard() {

    /* Gets current Name */
    var name = document.getElementById("id_full_Name").value;
    document.getElementById("Full_Name_Test").innerHTML = name;

    /* Gets current Portrait */
    var title = document.getElementById("id_portrait_of_Survivor").value;
    document.getElementById("profile").src = title;

    /* Gets Perks Images */
    var perk_One = document.getElementById("id_image_Of_Perk_One").value;
    document.getElementById("Perk1").src = perk_One;

    var perk_Two = document.getElementById("id_image_Of_Perk_Two").value;
    document.getElementById("Perk2").src = perk_Two;

    var perk_Three = document.getElementById("id_image_Of_Perk_Three").value;
    document.getElementById("Perk3").src = perk_Three;

    /*Gets Perk Names */
    var name = document.getElementById("id_perk_One").value;
    document.getElementById("Perk_One_Test").innerHTML = name;
    console.log(name);

    var name = document.getElementById("id_perk_Two").value;
    document.getElementById("Perk_Two_Test").innerHTML = name;

    var name = document.getElementById("id_perk_Three").value;
    document.getElementById("Perk_Three_Test").innerHTML = name;

    /*Gets Full Body Image */
    var Full_Body_Image = document.getElementById("id_image_Of_Survivor").value;
    document.getElementById("Body_Image").src = Full_Body_Image
}
function openDelete() {
    document.getElementById("confirmDelete").style.display = "block";
}

function closeDelete() {
    document.getElementById("confirmDelete").style.display = "none";
}

function PreviewCard2() {

    /* Gets current Name */
    var name = document.getElementById("id_full_Name").value;
    document.getElementById("Full_Name_Test").innerHTML = name;


    var Killertitle = document.getElementById("id_portrait_of_Killer").value;
    document.getElementById("profile").src = Killertitle;

    /* Gets Perks Images */
    var perk_One = document.getElementById("id_image_Of_Perk_One").value;
    document.getElementById("Perk1").src = perk_One;

    var perk_Two = document.getElementById("id_image_Of_Perk_Two").value;
    document.getElementById("Perk2").src = perk_Two;

    var perk_Three = document.getElementById("id_image_Of_Perk_Three").value;
    document.getElementById("Perk3").src = perk_Three;

    /*Gets Perk Names */
    var name = document.getElementById("id_perk_One").value;
    document.getElementById("Perk_One_Test").innerHTML = name;
    console.log(name);

    var name = document.getElementById("id_perk_Two").value;
    document.getElementById("Perk_Two_Test").innerHTML = name;

    var name = document.getElementById("id_perk_Three").value;
    document.getElementById("Perk_Three_Test").innerHTML = name;


    var K_Full_Body_Image = document.getElementById("id_image_Of_Killer").value;
    document.getElementById("Body_Image").src = K_Full_Body_Image;

}