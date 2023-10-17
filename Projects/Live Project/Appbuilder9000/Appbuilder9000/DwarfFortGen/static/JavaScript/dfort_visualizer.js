

/* Grabs the hidden h6 tag value from details page and changes color of visual based on selected material */
if (document.getElementById("skin") !== null) {
    var skin = String(document.getElementById("skin").innerHTML);

    if (String(skin) == 'meat') {
        document.getElementById("beast-visual").style.color = "red";
        document.getElementById("skin-display").style.color = "red";
        console.log(skin);

    } else if (String(skin) == 'metal') {
        document.getElementById("beast-visual").style.color = "silver";
        document.getElementById("skin-display").style.color = "silver";
        console.log(skin);

    } else if (String(skin) == 'fungus') {
        document.getElementById("beast-visual").style.color = "purple";
        document.getElementById("skin-display").style.color = "purple";
        console.log(skin);

    } else if (String(skin) == 'scale') {
        document.getElementById("beast-visual").style.color = "green";
        document.getElementById("skin-display").style.color = "green";
        console.log(skin);

    } else if (String(skin) == 'gem') {
        document.getElementById("beast-visual").style.color = "hotpink";
        document.getElementById("skin-display").style.color = "hotpink";
        console.log(skin);
    }
}
