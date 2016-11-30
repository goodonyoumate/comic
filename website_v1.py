from bottle import run
from bottle import route
from bottle import view
from itertools import count

#Classes ------------------
#Classes start with capitals

class Ticket:
    _ids = count(0)
    
    def __init__(self, name, email):
        #these properties are passwed on from the user
        self.name = name
        self.email = email

        #these are properties are set manually
        self.id = next(self._ids)
        self.checked_in = False
        
    
    def sell_ticket(self):
        self.total =- 1
        print(self.total)
        

tickets =  [
    Ticket("Tanya", "Tanya@hi.com"),
    Ticket("Fred", "Fred@flintstone.com"),
    Ticket("Superman", "supermand@gmail.com")
    ]

#print(first_ticket.name)
#print(second_ticket.name)

#Pages --------------------------------

#from bottle impor run,route,view
#index page / here is default

@route('/')
@view('index')
def index():
    pass

'''
make changes to the check-in page

@route grabs the value after / and pulls the value in
'''

@route('/check-in-success/<ticket_id>')
@view('check-in-success')

def check_in_success(ticket_id):

    found_ticket = None
    
    
    for ticket in tickets:
        
        if ticket.id == int(ticket_id):
            found_ticket = ticket
            found_ticket.checked_in = True
        
            
    data = dict(
                ticket = found_ticket
                )
    return data


@route('/check-in')
@view('check-in')

def check_in():
    data = dict(
                test = "hello", 
                ticket_list = tickets
                )
    return data

                
@route('/sell-ticket')
@view('sell-ticket')

def sell_ticket():
    pass


run(host='0.0.0.0',port=8080,reloader=True, debug=True)

#boolean's will need to be Capitals
#route

#http://0.0.0.0:8080

