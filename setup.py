from waitress import serve
from flask_app import create_app 
import os
port_= int(os.environ.get("PORT", 5000))
app=create_app()

if __name__ == '__main__':
	
    app.run()         
    serve(app,port=port_)
