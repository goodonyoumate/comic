from bottle import run
from bottle import route
from bottle import view, request
from itertools import count

#Classes ------------------
#Classes start with capitals

class Comic:
    _ids = count(0)
    
    def __init__(self, name,quantity,url,description):
        #these properties are passwed on from the user
        self.name = name
        self.quantity = quantity
        self.description = description
        self.url = url
        self.id = next(self._ids)


comics =  [
    Comic("superdude", 9, "https://s-media-cache-ak0.pinimg.com/564x/c8/9b/de/c89bde62a4254b45baf5a4ab289b194d.jpg", "5star"),
    Comic("the other book", 8, "http://static1.gamespot.com/uploads/original/1562/15626911/2991050-4996630-04-variant.jpg", "4star"),
    Comic("the last book", 9, "https://s-media-cache-ak0.pinimg.com/236x/cb/6b/ac/cb6bac6ffae8f510202f3c5e37b621aa.jpg", "3star")
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

@route('/sell-comic-success/<comic_id>')
@view('sell-comic-success')

def sell_comic_success(comic_id):
    
    for comic in comics:
        
        if comic.id == int(comic_id):
            found_comic = comic
            found_comic.quantity -= 1
        
    data = dict (
            comic = found_comic
        )
    return data

@route('/sell')
@view('sell')

def sell():
    data = dict(
                
                comic_list = comics
                )
    return data



               
@route('/restock-comic')
@view('restock-comic')

def restock_comic():
    pass



@route('/restock-success', method='POST')
@view('restock-success')

def restock_success():
    name = request.forms.get('name')
    quantity = request.forms.get('quantity')

    for comic in comics:
        if comic.name == name:
            comic.quantity = int(quantity)
        


run(host='0.0.0.0',port=8080,reloader=True, debug=True)


'''
allow the website to load CSS files
'''

@route('/css/:filename#.*#')
def send_static(filename):
       file = static_file(filename, root='./css/')
       return file
       
'''
allow the website to load image files
'''

@route('/images/:filename#.*#')
def load_images(filename):
       file = static_file(filename, root='./images/')
       return file


'''
more comments
'''
