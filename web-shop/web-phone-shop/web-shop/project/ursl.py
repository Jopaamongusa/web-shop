import home_page
from .settings import project
import log_page
import reg_page
import shop_page
import basket_page
import admin_page

home_page.home.add_url_rule(rule="/", view_func= home_page.render_home)
shop_page.shop.add_url_rule(rule="/shop/", view_func= shop_page.render_shop, methods = ['GET', 'POST'])
reg_page.reg.add_url_rule(rule='/reg/', view_func= reg_page.render_reg, methods = ['GET','POST'])
log_page.log.add_url_rule(rule='/log/', view_func= log_page.show_authorization, methods = ['GET','POST'])
basket_page.basket.add_url_rule(rule='/cart/', view_func= basket_page.render_basket, methods = ['GET','POST'])
admin_page.admin.add_url_rule(rule= '/admin/', view_func= admin_page.render_admin, methods= ["GET","POST"])

project.register_blueprint(blueprint= basket_page.basket)
project.register_blueprint(blueprint= home_page.home)
project.register_blueprint(blueprint= shop_page.shop)
project.register_blueprint(blueprint= reg_page.reg)
project.register_blueprint(blueprint= log_page.log)
project.register_blueprint(blueprint= admin_page.admin)