"""
    Controller File
    Users - Quotes
"""
from system.core.controller import *

class Main(Controller):
    def __init__(self, action):
        super(Main, self).__init__(action)
        
        self.load_model('MainModel')
        self.db = self._app.db
   
    def index(self):
        return self.load_view('index.html')

    def register(self):
        validate = self.models['MainModel'].validate_add_user(request.form)
        if validate['status'] == True:
            session['id'] = validate['user']['id']
            session['alias'] = validate['user']['alias']
            # change to /quotes
            return redirect('/quotes')
        else:
            for message in validate['errors']:
                flash(message, 'error reg')
            return redirect('/')

    def login(self):
        validate = self.models['MainModel'].validate_log_user(request.form)
        if validate['status'] == True:
            session['id'] = validate['user']['id']
            # change to /quotes
            return redirect('/quotes')
        else:
            for message in validate['errors']:
                flash(message, 'error log')
            return redirect('/')

    def logout(self):
        session.clear()
        return redirect('/')