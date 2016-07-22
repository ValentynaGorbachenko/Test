"""
    Controller File
    Users - Quotes
"""
from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        
        self.load_model('User')
        self.load_model('Quote')
        self.db = self._app.db

   
    def index(self):
        print "redirected"
        return redirect('/main')


    def show_user(self, id):
        user = self.models['User'].get_user_by_id(id)
        quotes = self.models['Quote'].get_quote_by_user_id(id)
        return self.load_view('show_user.html', user = user[0], quotes = quotes)


