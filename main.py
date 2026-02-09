from pyscript import document

def intrcheck(e):
    document.getElementById('output').innerHTML = ' '
    document.getElementById('image').innerHTML = ' '
    
    registration = document.querySelector('input[name="registration"]:checked').value
    clearance = document.querySelector('input[name="clear"]:checked').value
    grade_level = int(document.getElementById('level').value)
    section = document.getElementById('section').value

    if registration != 'registered':
        display(f'Not eligible: student is not registered for Intrams. Please ask your PE teacher about the online registraton.', target='output')
    elif clearance != 'cleared':
        display(f'Not eligible: medical clearance required. Get your clearance at the clinic.', target='output')
    elif section == 'emerald' and grade_level == 8 or 9:
        display(f'Congratulations! You are part of the RedBulldogs', target='output')
        document.getElementById("image").innerHTML = "Place the image tag here"
    elif section == 'ruby' and grade_level == 8 or 9:
        display(f'Congratulations! You are part of the Bluebears', target='output')
        document.getElementById("image").innerHTML = "Place the image tag here"
    elif section == 'ruby' and grade_level == 7 or 10:
        display(f'Congratulations! You are part of the YellowTigerss', target='output')
        document.getElementById("image").innerHTML = "Place the image tag here"
    else: 
        display(f'Congratulations! You are part of the GreenHornets', target='output')
        document.getElementById("image").innerHTML = "Place the image tag here"
   