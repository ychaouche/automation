from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
import sys

ff = Firefox(capabilities={"marionette":True})
ff.get("xxx")

def login():
    ff.find_element_by_name("_pass").send_keys("xxx")
    ff.find_element_by_name("_user").send_keys("xxx")
    ff.find_element_by_name("form").submit()

def contact():
    click_on(id="rcmbtn108")

def cdm():
    click_on(id="rcmliR2dsb2JhbDQzMQ")

def cdm_kouba():
    click_on(id="rcmliR2dsb2JhbDQzMg")

def drh():
    click_on(id="rcmliR2dsb2JhbDQyOA")

def click_on(id):
    WebDriverWait(ff,10).until(lambda x:ff.find_element_by_id(id))
    ff.find_element_by_id(id).click()
    


def do_add_contact(name,surname,email):
    WebDriverWait(ff,10).until(lambda x:ff.find_element_by_name("_firstname"))
    ff.find_element_by_name("_firstname").send_keys(name)
    ff.find_element_by_name("_surname").send_keys(surname)
    ff.find_element_by_name("_email[]").send_keys(email)


def add_contact(name,surname,email):
    contact_id="rcmbtn123"
    save_id="rcmbtn101"
    print name,surname,email
    # Ajout contact
    click_on(contact_id)
    # Changer de frame
    ff.switch_to.frame(ff.find_element_by_id('contact-frame'))
    do_add_contact(name,surname,email)
    # Sauvegarder
    click_on(save_id)
    # Retourner au cadre parent
    ff.switch_to.parent_frame()
    return name,surname,email

def add_contacts(datafile):
    csvreader = open(datafile)
    while True:
        try:
            name,surname,email = csvreader.next().split(",")
        except:
            return False
        add_contact(name,surname,email)
        print "Press Enter to continue"
        raw_input(str((name,surname,email)))
    
login()
raw_input("Press Enter to continue")
contact()
raw_input("Press Enter to continue")
drh()
raw_input("Press Enter to continue")
add_contacts("datadrh.csv")

