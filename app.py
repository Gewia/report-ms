from report import create_app
from report import db

app = create_app()

if __name__ == '__main__': #? debugging only
    app.run(host='0.0.0.0', port=5000)