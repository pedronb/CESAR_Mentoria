from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
# app.config['SECRET_KEY'] = "1234"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:mysqladmin@localhost/crud_projeto"

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from Routes.Projetos_Routes import *

if __name__ == '__main__':
    app.run(debug=True)