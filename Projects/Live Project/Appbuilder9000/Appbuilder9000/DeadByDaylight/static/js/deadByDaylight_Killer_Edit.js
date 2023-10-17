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
    document.getElementById("Body_Image").src = K_Full_Body_Image
}

window.onload = PreviewCard2();