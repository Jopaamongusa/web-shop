from project.settings import DATABASE

class Product(DATABASE.Model):
    id = DATABASE.Column(DATABASE.Integer, primary_key= True)
    name = DATABASE.Column(DATABASE.String(100), nullable= True)
    description = DATABASE.Column(DATABASE.Text, nullable= True)
    price = DATABASE.Column(DATABASE.Integer, nullable= True)
    count = DATABASE.Column(DATABASE.Integer, nullable= True)
    discount = DATABASE.Column(DATABASE.Integer, nullable= True)

    def __repr__(self):
        return f"{self.name} Номер в базі - {self.id}"