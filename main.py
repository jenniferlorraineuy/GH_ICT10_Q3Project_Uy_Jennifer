# listing the players
from pyscript import display, document


def intrams_players(e):
    players = ["Aseo, Tessa",
    "Batac, Anakin",
    "Calanglang, Neriza",
    "De Guzman, Vito",
    "Dee, Aaron",
    "Dolor, Harvey",
    "Galvez, Selena",
    "Garces, Adrianna",
    "Grospe, Jillian",
    "Hizon, Eduardo",
    "Intalan, Margo",
    "Ko, Atasha",
    "Lagman, Alijah",
    "Law, Marcus",
    "Macabago, Sittie",
    "Martinez, Euan",
    "Medina, Kelsey",
    "Mendoza, Michaela",
    "Mergal, Manuel",
    "Ngo, Seth",
    "Padojinog, Sofia",
    "Rivera, Benigno",
    "Shrestha, Ishan",
    "Uy, Jennifer",
    "Yao, Francesca"]

    output = document.getElementById("output")
    output.innerHTML = ""

    for player in players:
        output.innerHTML += player + "<br>"