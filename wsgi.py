from app import create_app

from app.config import ProductionConfig

app = create_app(config_class=ProductionConfig)

print('app.config["HOST"] = ', app.config['HOST'])