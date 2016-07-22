""" 
    Model File
    Users - Quotes
"""
from system.core.model import Model
import re


class User(Model):
    def __init__(self):
        super(User, self).__init__()

    """  User - Quotes  """
    
    # info about user by id
    def get_user_by_id(self, id):
        query_user = "SELECT * FROM users WHERE id = :id"
        data_user = {
            'id': id
        }
        return self.db.query_db(query_user, data_user)

    # info about user by email
    def get_user_by_email(self, email):
        query_user = "SELECT * FROM users WHERE email = :email"
        data_user = {
            'email': email
        }
        return self.db.query_db(query_user, data_user)
   