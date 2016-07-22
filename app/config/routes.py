"""
    Routes Configuration File
    Quotes
"""
from system.core.router import routes

"""
    Routes for Log In - Registration
"""

routes['default_controller'] = 'Users'
routes['POST']['/register'] = 'Main#register'
routes['/logout'] = 'Main#logout'
routes['POST']['/login'] = 'Main#login'
routes['/users/<int:id>'] = 'Users#show_user'

"""
Routes for Quotes
"""
routes['POST']['/quotes/add'] = 'Quotes#add_quote'
routes['/add_fav/<int:id>'] = 'Quotes#addfavorite'
routes['/remove/<int:id>'] = 'Quotes#removefavorite'