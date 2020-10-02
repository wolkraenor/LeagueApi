from app.__init__ import app
from app.settings import APP_NAME, APP_VERSION


@app.route("/")
def index():
    return {
        "app": APP_NAME,
        "version": APP_VERSION
    }
