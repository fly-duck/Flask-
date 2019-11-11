SQLALCHEMY_TRACK_MODIFICATIONS=False
from FreeTicket import app 


if __name__ == '__main__':
    app.run(debug=True)