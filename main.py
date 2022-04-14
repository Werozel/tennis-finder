import config
from modules.core.app import app

if __name__ == "__main__":
    app.run(port=config.PORT)
