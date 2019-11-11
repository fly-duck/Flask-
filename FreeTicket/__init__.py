SQLALCHEMY_TRACK_MODIFICATIONS=True 
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager,current_user,UserMixin
from flask import url_for,redirect,render_template,flash
from flask_admin.contrib.sqla import ModelView 



app = Flask(__name__)
app.config['SECRET_KEY'] = 'notsecretanymore'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


@login_manager.user_loader
def load_user(user_id):
    

    # print(User.get(user_id))
    return User.get(user_id)

from flask_admin import Admin 
from FreeTicket.models import User, Post 
admin=Admin(app)

class UserView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and not current_user.is_anonymous
    can_delete=False
 
class PostView(ModelView):
    page_size=50
    column_searchable_list = ['catagories']

    def is_accessible(self):
        print(current_user.username)
        if not current_user.is_admin:
            flash("you are not a admin!")
        return current_user.is_authenticated and not current_user.is_anonymous and current_user.is_admin




admin.add_view(UserView(User,db.session))
admin.add_view(PostView(Post,db.session))



# admin.add_view(ModelView(Post,name='cpp', endpoint='test1',db.session))
# admin.add_view(ModelView(Post,name='python', endpoint='test1',db.session))
# admin.add_view(ModelView(Post,name='others', endpoint='test1',db.session))


from FreeTicket import routes
