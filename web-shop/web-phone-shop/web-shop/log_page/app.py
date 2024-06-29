import flask

log = flask.Blueprint(
    name = "login_page",
    import_name= "app",
    template_folder = "log_page/templates",
    static_folder= "static",
    static_url_path= "/log",
)