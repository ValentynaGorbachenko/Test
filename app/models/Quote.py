""" 
    Model File
    Quotes
"""
from system.core.model import Model
import re


class Quote(Model):
    def __init__(self):
        super(Quote, self).__init__()

    def get_latest_quotes(self, id):
        query_quotes = "SELECT quotes.id as quote_id,quotes.author, quotes.quote, users.alias, users.id as user_id_who_wrote FROM quotes LEFT JOIN users ON users.id = quotes.user_id WHERE users.id NOT IN (SELECT favorites.quote_id FROM favorites WHERE favorites.user_id =:id);"
        data_user = {
            'id' : id
        }
        return self.db.query_db(query_quotes, data_user)

    def get_user_fav_quotes(self,id):
        query_fav_quotes = "SELECT quotes.id as quote_id,quotes.author, quotes.quote, users.alias, users.id as user_id_who_wrote FROM quotes LEFT JOIN users ON users.id = quotes.user_id WHERE quotes.id IN (SELECT favorites.quote_id FROM favorites WHERE favorites.user_id =:id);"
        data_user = {
            'id' : id
        }
        return self.db.query_db(query_fav_quotes, data_user)

    def add_quote(self, data, id):
        errors=[]
        if not data['author']:
            errors.append('Author name cannot be empty!')
        elif len(data['author'])>3:
            errors.append('Author cannot be less than 3 characters!')
        
        if not data['quote']:
            errors.append('Quote cannot be empty!')
        elif len(data['quote'])>10:
            errors.append('Quote cannot be less than 10 characters!')
        
        if errors:
            return {'status': False, 'errors': errors}
        else:
            query_quote = "INSERT INTO quotes (author, quote, user_id, created_at, updated_at) VALUES (:author, :quote, :id,  NOW(), NOW());"
            data_quote = {
                'author': data['author'],
                'quote': data['quote'],
                'id' :id
            }
            self.db.query_db(query_quote, data_quote)
            errors.append('You have successfully added a product!')
            return {'status': True, 'errors': errors}
    
    def get_quote_by_user_id(self, id):
        query = "SELECT quotes.author, quotes.id, quotes.quote FROM quotes LEFT JOIN users ON users.id = quotes.user_id WHERE users.id= :id;"        
        data = {
            'id' :id
        }
        return self.db.query_db(query, data)
    
    def addfavoritequote(self,quote_id, user_id):
        query = "INSERT INTO favorites (user_id, quote_id, created_at, updated_at) VALUES (:user_id, :quote_id, NOW(), NOW());"
        data = {
            'user_id': user_id,
            'quote_id': quote_id
        }
        return self.db.query_db(query, data)

    def removefavoritequote(self,quote_id, user_id ):
        query = "DELETE FROM favorites WHERE quote_id=: quote_id AND user_id = :user_id"
        data = {
            'user_id': user_id,
            'quote_id': quote_id
        }
        return self.db.query_db(query, data)