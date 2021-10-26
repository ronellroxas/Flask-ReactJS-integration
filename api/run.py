from app import create_app
from app.routes.query_routes import query_bp
from app.routes.datasource_routes import datasource_bp
import config

app = create_app(config)
app.register_blueprint(query_bp)
app.register_blueprint(datasource_bp)

if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)