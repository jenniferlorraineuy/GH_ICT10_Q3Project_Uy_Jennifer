from pyscript import display, document

def intrams_signup(e):
    document.getElementById('output').innerHTML = ' '

    reg = document.querySelector('input[name="reg"]:checked')
    medcert = document.querySelector('input[name="medcert"]:checked')
    grade = int(document.getElementById('grade').value)
    section = document.getElementById('section').value

    if reg is None or medcert is None or section == "":
        display("Kindly accomplish all fields", target='output')

    elif reg.value !="yes":
        display("Please do the online registration", target='output')
    
    elif medcert.value !="yes":
        display("Please get medical clearance from the clinic", target='output')
    
    elif grade < 7 or grade > 10:
        display("Only for grades 7-10", target='output')

    elif grade == 7 and section == "Emerald":
        display("Congratulations! Welcome to Yellow Tigers", target='output')
    elif grade == 7 and section == "Ruby":
        display("Congratulations! Welcome to Blue Bears", target='output')
    elif grade == 7 and section == "Sapphire":
        display("Congratulations! Welcome to Red Bulldogs", target='output')
    elif grade == 7 and section == "Topaz":
        display("Congratulations! Welcome to Green Hornets", target='output')

    elif grade == 8 and section == "Emerald":
        display("Congratulations! Welcome to Yellow Tigers", target='output')
    elif grade == 8 and section == "Ruby":
        display("Congratulations! Welcome to Blue Bears", target='output')
    elif grade == 8 and section == "Sapphire":
        display("Congratulations! Welcome to Red Bulldogs", target='output')
    elif grade == 8 and section == "Topaz":
        display("Congratulations! Welcome to Green Hornets", target='output')

    elif grade == 9 and section == "Emerald":
        display("Congratulations! Welcome to Yellow Tigers", target='output')
    elif grade == 9 and section == "Ruby":
        display("Congratulations! Welcome to Blue Bears", target='output')
    elif grade == 9 and section == "Sapphire":
        display("Congratulations! Welcome to Red Bulldogs", target='output')
    elif grade == 9 and section == "Topaz":
        display("Congratulations! Welcome to Green Hornets", target='output')

    elif grade == 10 and section == "Emerald":
        display("Congratulations! Welcome to Yellow Tigers", target='output')
    elif grade == 10 and section == "Ruby":
        display("Congratulations! Welcome to Blue Bears", target='output')
    elif grade == 10 and section == "Sapphire":
        display("Congratulations! Welcome to Red Bulldogs", target='output')
    elif grade == 10 and section == "Topaz":
        display("Congratulations! Welcome to Green Hornets", target='output')

    else:
        display("Invalid Input", target='output')