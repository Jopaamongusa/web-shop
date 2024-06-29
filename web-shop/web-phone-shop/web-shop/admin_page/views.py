import flask, os
import json
from shop_page.models import Product
from project.settings import DATABASE
from flask_login import current_user


def render_admin():

    path_json = os.path.abspath(__file__ + "/../../static/admin_page/json/data.json")
    print(path_json)
    with open(path_json, "r", encoding='utf-8') as file:
        data_dict = json.load(file)

    if flask.request.method == 'POST':
        try:

            if flask.request.form.get('new-product'):
                product = Product(
                    name = flask.request.form['name-add'],
                    description = flask.request.form['description-add'],
                    price = flask.request.form['price-add'],
                    count = flask.request.form['count-add'],
                    discount = flask.request.form['discount-add']
                )
                DATABASE.session.add(product)
                DATABASE.session.commit()
                image_file = flask.request.files['image-add']
                image_file.save(os.path.abspath(__file__ + f'/../../../reg_projec/static/shop_page/images/{product.name}.png'))
            
            elif flask.request.form.get('del'):
                product_id = int(flask.request.form['del'])
                print(product_id)
                product_del = Product.query.get(product_id)
                print(product_del)
                if Product.query.get(product_id):
                    DATABASE.session.delete(product_del)
                    DATABASE.session.commit()
                    os.remove(os.path.abspath(__file__ + f"/../../../reg_projec/static/shop_page/images/{product_del.name}.png"))

            elif flask.request.form.get('set-changes'):
                product_data = flask.request.form.get("set-changes").split('-') # із form отримали "image-1" => product_data = ['image', '1'] 
                print(product_data)
                product_id = int(product_data[-1]) # product_id = 1
                get_product = Product.query.get(product_id)
                abspath = os.path.abspath(__file__ + "/../../../reg_projec/static/shop_page/images")
                if "0" == product_data[0]:
                    os.remove(abspath + f'/{get_product.name}.png')
                    new_image = flask.request.files['image']
                    new_image.save(abspath + f'/{get_product.name}.png')
                elif '1' == product_data[0]:
                    if product_data[1] == '1':
                        print(100)
                        new_product_name = flask.request.form['name']
                        os.rename(src= abspath + f'\{get_product.name}.png', dst= abspath + f'\{new_product_name}.png')
                        get_product.name = new_product_name
                        DATABASE.session.commit()
                    elif '2' == product_data[1]:
                        print(200)
                        new_product_name = flask.request.form["price"]
                        get_product.price = new_product_name
                        DATABASE.session.commit()
                    elif '3' == product_data[1]:
                        new_product_name = flask.request.form["description"]
                        get_product.description = new_product_name
                        DATABASE.session.commit()
                    elif '4' == product_data[1]:
                        new_product_name = flask.request.form["count"]
                        get_product.count = new_product_name
                        DATABASE.session.commit()
                
        except Exception as e:
            print(e)

    if current_user.is_authenticated and current_user.is_admin:
        return flask.render_template(
            body = data_dict,
            template_name_or_list = 'admin.html', 
            products = Product.query.all(),
            is_authenticated = current_user.is_authenticated,
            user_name = current_user.name,
            is_admin = current_user.is_admin
        )
    
    return flask.redirect('/')

# reg_projec\static\admin_page\json\data.json
# reg_projec\\static\\admin_page\\json\\data.json
# reg_projec\static\admin_page\json\data.json