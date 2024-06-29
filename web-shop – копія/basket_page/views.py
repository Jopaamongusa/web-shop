import flask
import os 
import json
from shop_page import Product
from flask_login import current_user
from project.main_config import mail
from flask_mail import Message
# from reg_page.models import Users
from basket_page.models import Delivery

def render_basket():
    global id_products 
    path_json = os.path.abspath(__file__ + "/../../static/basket_page/json/data.json")
    with open(path_json, "r", encoding="utf-8") as file:
        data_dict = json.load(file)

    if current_user.is_authenticated:
        is_authenticated = current_user.is_authenticated,
        user_name = current_user.name,
    else:
        is_authenticated = None
        user_name = None



    if flask.request.cookies.get('products') :
        products = flask.request.cookies.get('products')
        count = len(products)
        count = count // 2 + 1
        list_products = []
        repeate_id = []        
        for id_products in products:
            count_products = products.count(id_products)
            if id_products not in repeate_id:
                list_products.append(Product.query.get(id_products))
                print(list_products)
                repeate_id.append(id_products)
        if flask.request.method == 'POST':
            print(flask.request.form['email'])
            delivery = Delivery(         
                name = flask.request.form['username'],     
                forname = flask.request.form['forname'],
                email = flask.request.form['email'],
                phone_number = flask.request.form['phone-number'],
                city = flask.request.form['city'],
                post = flask.request.form['post'],
                more_info = flask.request.form['more_info'],
            ) 

            message_text = f'Order № {Delivery.product}: \n\n' + f"Ваше замовлення {Delivery.product} було надіслано в місто {delivery.city} та в віділ {delivery.post} "
            for product in list_products:
                message_text += f'{product.name}\n'
    
            message = Message(
                subject = f'Order № {list_products}',
                sender = 'arzon.art125@gmail.com',
                recipients = [delivery.email],
                body = message_text
            )    
            mail.send(message)
        try:
            return flask.render_template(template_name_or_list = 'basket.html', body = data_dict, products = list_products, count = count, is_authenticated= is_authenticated, user_name= user_name, is_admin = current_user.is_admin)
        except UnboundLocalError:
            count_products = 0
            return flask.render_template(template_name_or_list = 'basket.html', body = data_dict, products = list_products, count = count, is_authenticated= is_authenticated, user_name= user_name, is_admin = current_user.is_admin)
    else:
        print(data_dict)
        return flask.render_template(template_name_or_list= "basket.html", body = data_dict , is_authenticated= is_authenticated, user_name= user_name, is_admin = current_user.is_admin)

