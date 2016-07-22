"""
    Controller File
    Quotes 
"""
from system.core.controller import *

class Quotes(Controller):
    def __init__(self, action):
        super(Quotes, self).__init__(action)
        
        self.load_model('User')
        self.load_model('Quote')
        self.db = self._app.db

   
    def index(self):
        
        quotes = self.models['Quote'].get_latest_quotes(session['id'])
        favorites = self.models['Quote'].get_user_fav_quotes(session['id'])
        return self.load_view('quotes.html', quotes = quotes, favorites=favorites)

    def add_quote(self):
        print 'added =)'
        validate = self.models['Quote'].add_quote(request.form, session['id'])
        if validate['status'] == True:
            for message in validate['errors']:
                flash(message, 'valid')
            return redirect('/quotes')
        else:
            for message in validate['errors']:
                flash(message, 'error')
            return redirect('/quotes')
    
    def addfavorite(self, id):
        self.models['Quote'].addfavoritequote(id, session['id'])
        return redirect('/quotes')

    def removefavorite(self,id):
        self.models['Quote'].removefavoritequote(id, session['id'])
        return redirect('/quotes')