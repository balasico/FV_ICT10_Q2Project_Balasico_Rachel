from pyscript import document, display

#SEATWORK 1
club_members = ["Rachel Balasico","Adrianna Averilla","Ciara De Guzman","Zyrene Nieto"]

def check_member(e):
    #gets the info from index.html
    first_name = Element("firstName").element.value
    last_name = Element("lastName").element.value

    #for the message
    full_name = first_name + " " + last_name

    #checks if what is inputed part for the list
    is_member = full_name in club_members

    messages = {True: f"Congratulations {full_name}! You are now part of the ICT club.", False: f"Sorry {full_name}, your name is not on the list.}

    #displays the message
    display(messages[is_member], target="result")

#SKILLS TEST
def check_details (e):
    #list of all non-metals
    non_metals = {
        "H": ("Hydrogen", 1, 1.008),
        "He": ("Helium", 2, 4.003),
        "C": ("Carbon", 6, 12.011),
        "N": ("Nitrogen", 7, 14.007),
        "O": ("Oxygen", 8, 15.999),
        "F": ("Flourine", 9, 18.998),
        "Ne": ("Neon", 10, 20.180),
        "P": ("Phosphorus", 15, 30.974),
        "S": ("Sulfur", 16, 32.065),
        "Cl": ("Clorine", 17, 35.453),
        "Ar": ("Argon", 18, 39.948),
        "Se": ("Selenium", 34, 78.960),
        "Br": ("Bromine", 35, 79.904),
        "Kr": ("Krypton", 36, 83.798),
        "I": ("Iodine", 54, 126.905),
        "Xe": ("Xenon", 54, 131.293),
        "Rn": ("Radon", 86, 222.018),
    }

    #gets the info from index.html
    element_input = document.getElementById("element").value

    element_display = non_metals.get(element_input, ("Element not found", "-", "-"))

    #from ma'am
    result = f"""
    <div>
    <b> Symbol: </b> {element_input} <br>
    <b> Element: </b> {element_display[0]} <br>
    <b> Atomic Number: </b> {element_display[1]} <br>
    <b> Atomic Mass: </b> {element_display[2]}
    </div>
    """

    #displays the result
    display(result, target = "result")

#DRILL 2
def new_member(e):

    grade_8 = {'Jayana Tremor'}
    grade_9 = {'Fairy Admat','Kyrie Funtanilla'}
    grade_10 = {'Rachel Balasico','Caitlyn Tano','Hope Benitez','Sammantha Lacuesta','Rocky Saludes'}
    grade_11 = {'Lorenzo Calida','Queeny Ramos'}
    grade_12 = {'Anna Avestruz','Lloyd Gonzales','Elisha Padre'}

    #gets the info from index.html
    first_name = document.getElementById("firstname").value
    last_name = document.getElementById("lastname").value

    new_fellow = first_name + " " + last_name
    new_fellow_again = {new_fellow}

    #combines all the sets
    all_members = grade_8 | grade_9 | grade_10 | grade_11 | grade_12 | new_fellow_again

    #sorts the names alphabetically
    all_members = sorted(all_members)

    #displays the heading
    display("ALL MEMBERS", target="result")

    for member in all_members: display(member, target="result")

    #displays the total number of members
    display("Total Members: " + str(len(all_members)), target="result")