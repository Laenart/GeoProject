from parks.park_view import parks_api

from app import app

app.register_blueprint(parks_api)

if __name__ == '__main__':
    app.run()
