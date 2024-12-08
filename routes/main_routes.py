
def register_routes(app):
    "register all blueprints here"
    from src.routes_rout.restourent_routes import restaurent_bp
    app.register_blueprint(restaurent_bp,url_prefix="/api")