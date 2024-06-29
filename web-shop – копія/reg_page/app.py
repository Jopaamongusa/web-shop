import flask

reg = flask.Blueprint(
    name = 'registration',
    import_name = "app",
    template_folder = "reg_page/templates",
    static_folder = "static",
    static_url_path = "/reg"
)