from app import create_app

from app.config import ProductionConfig

app = create_app(config_class=ProductionConfig)

print('app.config["HOST"] = ', app.config['HOST'])
print('app.config["SQLALCHEMY_DATABASE_URI"] = ', app.config['SQLALCHEMY_DATABASE_URI'])