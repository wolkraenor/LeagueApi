from app.views import app
from app.settings import APP_PORT

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=APP_PORT)



