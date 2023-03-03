from flask import Flask, flash, redirect, render_template, request, session, g
from flask_sqlalchemy import SQLAlchemy
#from sqlalchemy.orm import sessionmaker

from sqlalchemy import type_coerce, create_engine, ForeignKey, Column, String, Integer, CHAR, Numeric, desc
#from flask_session import Session
#from tempfile import mkdtemp
#from werkzeug.security import check_password_hash, generate_password_hash

# Configure application
app = Flask(__name__)

# Configure app for sqlAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///namo.sqlite3'
db = SQLAlchemy(app)

#engine = create_engine('sqlite:////instance/bestello.sqlite3')
#Session = sessionmaker(bind=engine)
#session = Session

# db.Model.metadata.reflect(db.engine)


# Define model
class Bestello(db.Model):
    __tablename__ = 'bestello'
    #__table_args__ = {'extend_existing': True}
    # LOC_CODE = db.Column(db.Text, primary_key=True)
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer)
    price = db.Column(db.Numeric)
    user_id = db.Column(db.Integer)
    size = db.Column(db.String[100])
    shipping = db.Column(db.Numeric)
    total = db.Column(db.Numeric)
    number = db.Column(db.Integer)

class Customer(db.Model):
    __tablename__ = "customer"
    id = db.Column(db.Integer, primary_key = True)
    vorname = db.Column(db.String[100])
    nachname = db.Column(db.String[100])
    email = db.Column(db.String[100])
    strasse = db.Column(db.String[100])
    haus_no = db.Column(db.Integer)
    plz = db.Column(db.Integer)
    stadt = db.Column(db.String[100])


# Configure session to use filesystem (instead of signed cookies)
#app.config["SESSION_PERMANENT"] = False
#app.config["SESSION_TYPE"] = "filesystem"
#Session(app)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/index", methods=["GET", "POST"])
def buy():
    if request.method == "GET":
        return render_template("index.html")

    if request.method == "POST":
        # id = session["user_id"]

        user_id = 1

        if request.form.get("eins"):
            item = "Shirt Motiv 1"
            item_id = 1
        else:
            item = "Shirt Motiv 2"
            item_id = 2



        number = request.form.get("number")
        number = int(number)
        if (number < 0):
            return redirect("index.html")

        price = 24.99
        shipping = 5.99
        total = (price * number) + shipping
        size = "m"

        bestell = Bestello(item_id=item_id,price=price, user_id=user_id, size=size,
                           shipping=shipping, total=total, number=number)

        db.create_all()
        db.session.add(bestell)
        db.session.commit()
        bestellungen = Bestello.query.all()
        # data = (item_id, price, number, size, shipping, total)

        # (item_id, price, number, size, shipping, total) "number": number,

        return render_template("/order.html", item=item, number=number, bestellungen=bestellungen)


@app.route("/order", methods=["GET", "POST"])
def order():
    if request.method == "GET":
        return render_template("order.html")

    else:
        vorname = request.form.get("firstname")
        nachname = request.form.get("lastname")
        email = request.form.get("email")
        strasse = request.form.get("street")
        haus_no = request.form.get("hausnummer")
        plz = request.form.get("plz")
        stadt = request.form.get("city")

        customer = Customer(vorname=vorname, 
                            nachname=nachname,
                            email=email,
                            strasse=strasse,
                            haus_no=haus_no,
                            plz=plz,
                            stadt=stadt)
        db.create_all()
        db.session.add(customer)
        db.session.commit()
        return render_template("after_order.html", customer=customer)



@app.route("/after_order", methods=["GET", "POST"])
def after_order():
        if request.method == "POST":
            if 'confirmation' in request.form:        
                row = Bestello.query.order_by(desc(Bestello.item_id)).first()
                item_id = row.item_id

                print(item_id)

                if item_id == 1:
                    motiv = "Motiv 1"
                elif item_id == 2:
                    motiv = "Motiv 2"
                else:
                    return ("/")

                total = row.total
                total = round(total, 2)

                return render_template("order_confirmation.html", motiv=motiv, total=total)
            else:
                last_row = Customer.query.order_by(Customer.id.desc()).first()

                if last_row:
                    db.session.delete(last_row)
                    db.session.commit()

                return render_template("order.html")
        

@app.route("/home", methods=["GET", "POST"])
def home():
    return redirect("/")

if __name__ == '__main__':
    app.run()
