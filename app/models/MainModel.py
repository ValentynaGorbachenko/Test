""" 
    Model File
    Users - Quotes
"""
from system.core.model import Model
import re

class MainModel(Model):
    def __init__(self):
        super(MainModel, self).__init__()

    """  Log In - Registration  """
   
    # validation check and inserting new user into database
    def validate_add_user(self, data):
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        errors = []
        # name validation
        if not data['name']:
            errors.append('Name cannot be empty!')
        elif len(data['name'])<2:
            errors.append('Name should be at least 2 characters long')
        # elif not data['name'].isalpha():
        #     errors.append('Name can contain only characters!')
        # alias validation
        if not data['alias']:
            errors.append('Alias cannot be empty!')
        elif len(data['alias'])<2:
            errors.append('Alias should be at least 2 characters long')
        elif not data['alias'].isalpha():
            errors.append('Alias can contain only characters!')
        # email validation
        if not data['email']:
            errors.append('Email cannot be empty!')
        elif not EMAIL_REGEX.match(data['email']):
            errors.append('Email format must be valid!')
        # password validation
        if not data['password']:
            errors.append('Password cannot be empty!')
        elif len(data['password'])<8:
            errors.append('Password must be at least 8 characters long!')
        elif data['password'] != data['conf_password']:
            errors.append('Password and confirmation must match!')
        # birthdate validation
        if not data['birthdate']:
            errors.append('Birthday cannot be empty!')
        elif len(data['birthdate'])<8:
            errors.append('Birthday should be have 8 numbers')
        # elif not data['alias'].isdigit():
        #     errors.append('Birthday can contain only numbers!')


        if errors:
            return {'status': False, 'errors': errors}
        else:
            # validation passed, inserting the info
            query_email = "SELECT * FROM users WHERE email = :user_email LIMIT 1"
            data_email = {
                'user_email': data['email']
            }
            email_check = self.db.query_db(query_email, data_email)
            if len(email_check)==0:
                hashed_pass = self.bcrypt.generate_password_hash(data['password'])
                query_user = "INSERT INTO users (name, alias, email, password, birthdate, created_at, updated_at) VALUES(:name, :alias, :email, :hashed_pass, :birthdate, NOW(), NOW())"
                data_user = {
                    'name': data['name'],
                    'alias': data['alias'],
                    'email': data['email'],
                    'hashed_pass': hashed_pass,
                    'birthdate': data['birthdate']
                }
                self.db.query_db(query_user, data_user)
                # retrieve the last inserted user by email
                users = self.db.query_db(query_email, data_email)
                return {'status': True, 'user': users[0]}
            else:
                errors.append('This email in use already!')
                return {'status': False, 'errors': errors}
            
    def validate_log_user(self, data):
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        errors = []
        # email validation
        if not data['email']:
            errors.append('Email cannot be empty!')
        
        # password validation
        if not data['password']:
            errors.append('Password cannot be empty!')
        
        if errors:
            return {'status': False, 'errors': errors}
        else:
            query_email = "SELECT * FROM users WHERE email = :user_email LIMIT 1"
            data_email = {
                'user_email': data['email']
            }
            user_curr = self.db.query_db(query_email, data_email)
            
            if len(user_curr)==1:
                if self.bcrypt.check_password_hash(user_curr[0]['password'], data['password']):
                    return {'status': True, 'user': user_curr[0]}
                else:
                    errors.append('Password is not matching!')
                    return {'status': False, 'errors': errors}
            else:
                errors.append('Email is not matching!')
                return {'status': False, 'errors': errors}
