from pyscript import display, document

def intrcheck(e):
    document.getElementById('output').innerHTML = ' '
    document.getElementById('image').innerHTML = ' '
    
    registration = document.querySelector('input[name="registration"]:checked').value
    clearance = document.querySelector('input[name="clear"]:checked').value
    grade_level = document.getElementById('level').value
    

    if registration != 'regis':
        display(f'Not eligible: student is not registered for Intrams. Please ask your PE teacher about the online registraton.', target='output')
    elif clearance != 'yesclear':
        display(f'Not eligible: medical clearance required. Get your clearance at the clinic.', target='output')
    elif grade_level == 'b':
        display(f'Congratulations! You are part of the RedBulldogs', target='output')
        document.getElementById("image").innerHTML = "<img src='red bulldogs.jpg' height='300' width='300'>"
    elif grade_level == 'f':
        display(f'Congratulations! You are part of the BlueBears', target='output')
        document.getElementById("image").innerHTML = "<img src='blue bears.jpg' height='300' width='300'>"
    elif grade_level == 'e':
        display(f'Congratulations! You are part of the YellowTigers', target='output')
        document.getElementById("image").innerHTML = "<img src='yellow tigers.jpg' height='300' width='300'>"
    elif grade_level == 'c':
        display(f'Congratulations! You are part of the RedBulldogs', target='output')
        document.getElementById("image").innerHTML = "<img src='red bulldogs.jpg' height='300' width='300'>"
    elif grade_level == 'g':
        display(f'Congratulations! You are part of the BlueBears', target='output')
        document.getElementById("image").innerHTML = "<img src='blue bears.jpg' height='300' width='300'>"
    elif grade_level == 'h':
        display(f'Congratulations! You are part of the YellowTigers', target='output')
        document.getElementById("image").innerHTML = "<img src='yellow tigers.jpg' height='300' width='300'>"
    else: 
        display(f'Congratulations! You are part of the GreenHornets', target='output')
        document.getElementById("image").innerHTML = "<img src='green hornets.jpg' height='300' width='300'>"
   
   
