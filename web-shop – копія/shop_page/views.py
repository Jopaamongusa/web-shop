import flask, os, json, pandas
from project.settings import DATABASE
from .models import Product
from flask_login import current_user 

def render_shop():
    if len(Product.query.all()) == 0:
        path = os.path.abspath(__file__+'/../Product.xlsx')
        


    path_json = os.path.abspath(__file__ + "/../../static/shop_page/json/data.json")
    with open(path_json, "r", encoding="utf-8") as file:
        data_dict = json.load(file)

    
    path_xlsx = os.path.abspath(__file__+"/../Product.xlsx")

    read_xl = pandas.read_excel(io= path_xlsx,header=None, names=["name", "description", "price"])
    
    list_products = []

    repeate_id = []

    print(Product.query.all())

    # for row in read_xl.iterrows():
    #     row_data = row[1]
    #     product = Product(
    #         name = row_data["name"],
    #         description = row_data["description"],
    #         price = row_data["price"],
    #         count = 1
    # #     )

    #     DATABASE.session.add(product)
    #     DATABASE.session.commit()
        
    if current_user.is_authenticated:
        is_authenticated = current_user.is_authenticated,
        user_name = current_user.name,
    else:
        is_authenticated = None
        user_name = None
    cookie = flask.request.cookies.get("products")
    if cookie != None and cookie != 0:
        for id in cookie:
            count = cookie.count(id)

        try:
            return flask.render_template(template_name_or_list= "shop.html", body = data_dict,products = Product.query.all(), count = count, is_authenticated= is_authenticated, user_name= user_name, is_admin = current_user.is_admin)
        except UnboundLocalError:
            count = 0
            return flask.render_template(template_name_or_list= "shop.html", body = data_dict,products = Product.query.all(), count = count, is_authenticated= is_authenticated, user_name= user_name, is_admin = current_user.is_admin)
    else:
        return flask.render_template(template_name_or_list= "shop.html", body = data_dict,products = Product.query.all(), is_authenticated= is_authenticated, user_name= user_name, is_admin = current_user.is_admin)

