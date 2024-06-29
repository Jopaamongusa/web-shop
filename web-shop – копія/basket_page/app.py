import flask 

basket  = flask.Blueprint(
    name = "basket",
    import_name = "basket_app",
    template_folder = "basket_page/templates",
    static_folder = "static/basket_page",
    static_url_path = "/basket/"
)