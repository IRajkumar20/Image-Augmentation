from flask import Flask
from models import db
from image import IMG_UPLOAD
from mosaic_or import MOSAIC
import os


app=Flask(__name__)


# database
basedir=os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///' + os.path.join(basedir,'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False



db.init_app(app)

with app.app_context():
    db.create_all()


# blueprint register
app.register_blueprint(IMG_UPLOAD)   
app.register_blueprint(MOSAIC)


if __name__ == "__main__":
    app.run()