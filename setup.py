from waitress import serve
from flask_app import create_app 

app=create_app()

if __name__ == '__main__':
    app.run()         
    serve(app)
