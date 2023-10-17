function PreviewBeast() {

    /* Gets current Name */
    var name = document.getElementById("id_name").value;
    document.getElementById("newName").innerHTML = name;

    /* Gets current Title */
    var title = document.getElementById("id_title").value;
    document.getElementById("newTitle").innerHTML = title;

    /* Gets current Skin Selection */
    var skin = document.getElementById("id_skin").value;

    /* Skin Color */
    if (String(skin) == 'meat') {
        document.getElementById("beast-visual").style.color = "red";
        document.getElementById("id_skin").style.color = "red";

    } else if (String(skin) == 'metal') {
        document.getElementById("beast-visual").style.color = "silver";
        document.getElementById("id_skin").style.color = "silver";

    } else if (String(skin) == 'fungus') {
        document.getElementById("beast-visual").style.color = "purple";
        document.getElementById("id_skin").style.color = "purple";

    } else if (String(skin) == 'scale') {
        document.getElementById("beast-visual").style.color = "green";
        document.getElementById("id_skin").style.color = "green";

    } else if (String(skin) == 'gem') {
        document.getElementById("beast-visual").style.color = "hotpink";
        document.getElementById("id_skin").style.color = "hotpink";
    }

    /* Gets current Species selection */
    var species = document.getElementById("id_species").value;

    /* Gets area to paint Beast Image */
    var top1 = document.getElementById("top1")
    var top2 = document.getElementById("top2")
    var mid = document.getElementById("mid")
    var bot1 = document.getElementById("bot1")
    var bot2 = document.getElementById("bot2")

    /* Species Type */
    if (String(species) == 'canine') {
        top1.innerHTML = '  [:P  ';
        top2.innerHTML = ' <-|-> ';
        mid.innerHTML =  '|| # ||';
        bot1.innerHTML = 'V \\#/ V';
        bot2.innerHTML = ' _| |_ ';
    }
    else if (String(species) == 'avian') {
        top1.innerHTML = '  }B>  ';
        top2.innerHTML = ' o-^-o ';
        mid.innerHTML = '[|   |]';
        bot1.innerHTML = '[ \\_/ ]';
        bot2.innerHTML = '  | |  ';
    }
    else if (String(species) == 'feline') {
        top1.innerHTML = '  =:3  ';
        top2.innerHTML = ' <-|-> ';
        mid.innerHTML =  '|| # ||';
        bot1.innerHTML = 'V \\#/ V';
        bot2.innerHTML = ' _| |_ ';
    }
    else if (String(species) == 'unknown') {
        top1.innerHTML = '  ___  ';
        top2.innerHTML = ' ( ~ ) ';
        mid.innerHTML = '(  0  )';
        bot1.innerHTML = '(_____)';
        bot2.innerHTML = ' |   | ';
    }
    else if (String(species) == 'amphibian') {
        top1.innerHTML = '  ,_,  ';
        top2.innerHTML = ' (00) ';
        mid.innerHTML = 'T( ~ )T';
        bot1.innerHTML = '" \\_/ "';
        bot2.innerHTML = '  ( )  ';
    }
    else if (String(species) == 'reptilian') {
        top1.innerHTML = ' {(")} ';
        top2.innerHTML = '_--+--_';
        mid.innerHTML = ' / |   | \\ ';
        bot1.innerHTML = '[  |__|  ]';
        bot2.innerHTML =' _/  \\_ ';
    }

    }
