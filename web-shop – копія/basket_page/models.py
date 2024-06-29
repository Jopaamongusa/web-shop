from project.settings import DATABASE

class Delivery(DATABASE.Model):
    id =            DATABASE.Column(DATABASE.Integer, primary_key = True)
    name =          DATABASE.Column(DATABASE.String(50))
    forname =       DATABASE.Column(DATABASE.String(100))
    email =         DATABASE.Column(DATABASE.String(50))
    phone_number =  DATABASE.Column(DATABASE.String(50))
    city =          DATABASE.Column(DATABASE.Text())
    post =          DATABASE.Column(DATABASE.Text())
    more_info =     DATABASE.Column(DATABASE.Text())
    product =       DATABASE.Column(DATABASE.String(50))

    def __reor__(self):
        return f'Користувач {self.email}'
        