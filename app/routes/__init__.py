from . import app

@app.route("/")
def index():
    return {
        "app": APP_NAME,
        "version": APP_VERSION
    }