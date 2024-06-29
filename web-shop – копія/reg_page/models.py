from project.settings import DATABASE

class Users(DATABASE.Model):
    id = DATABASE.Column(DATABASE.Integer, primary_key = True)
    name = DATABASE.Column(DATABASE.String(50))
    email = DATABASE.Column(DATABASE.String(50))
    password = DATABASE.Column(DATABASE.String(50))
    is_admin = DATABASE.Column(DATABASE.Boolean)
    
    def __repr__(self):
        return f'Користувач {self.name}'
    
    def is_active(self):
        return True
    
    def get_id(self):
        return str(self.id)
    
    def is_authenticated(self):
        return True
    
    def is_anonymous(self):
        return False