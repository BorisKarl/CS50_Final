from flask import Flask, request, render_template, redirect, url_for
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc, delete

app = Flask(__name__)

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop_db.sqlite3'
db = SQLAlchemy(app)

# Mail Configuration
app.config['MAIL_SERVER'] = 'smtp.strato.de'
app.config['MAIL_DEFAULT_SENDER'] = 'webmaster@borisnielsen.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'webmaster@borisnielsen.com'
app.config['MAIL_PASSWORD'] = 'monawebshop4321'
mail = Mail(app)


# Define classes for database
class Order(db.Model):
    __tablename__ = "order"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String[100])
    item_id = db.Column(db.Integer)
    price = db.Column(db.Numeric(10,2))
    user_id = db.Column(db.Integer)
    shipping = db.Column(db.Numeric(10, 2))
    total = db.Column(db.Numeric(10, 2))


class Customer(db.Model):
    __tablename__ = "customer"
    id = db.Column(db.Integer, primary_key=True)
    vorname = db.Column(db.String[100])
    nachname = db.Column(db.String[100])
    email = db.Column(db.String[100])
    strasse = db.Column(db.String[100])
    haus_no = db.Column(db.Integer)
    plz = db.Column(db.Integer)
    stadt = db.Column(db.String[100])


# store the products
products = [
    {"id": 1, "name": "Der schauende Hund", "price": 9.99, "src": "motiv_1.png"},
    {"id": 2, "name": "Der mutige Hund", "price": 29.99, "src": "motiv_2.png"},
    {"id": 3, "name": "Der fliegende Hund", "price": 39.99, "src": "motiv_3.png"},
    {"id": 4, "name": "Der Hund im Sommer", "price": 49.99, "src": "motiv_4.png"},
    {"id": 5, "name": "Der lachende Hund", "price": 59.99, "src": "motiv_5.png"},
    {"id": 6, "name": "Der Hund mit Punkten", "price": 69.99, "src": "motiv_6.png"},
    {"id": 7, "name": "Der Hund unter zwei Sonnen", "price": 44.99, "src": "motiv_7.png"},
    {"id": 8, "name": "Der bunte Hund", "price": 54.99, "src": "motiv_8.png"},
    {"id": 9, "name": "Der Hund mit Napf", "price": 64.99, "src": "motiv_9.png"},
]


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", products=products)


# Dynamic route
@app.route("/product/<int:product_id>", methods = ["GET", "POST"])
def product(product_id):
    product = None
    for p in products:
        if p["id"] == product_id:
            product = p

    if request.method == "GET":
        return render_template("product.html", product=product)


# Order site and db entries
@app.route("/order", methods = ["GET", "POST"])
def order():
    if request.method == "GET":
        return render_template("adress.html", product=product)

    elif request.method == "POST":
        id = request.form.get("item")

        int_id = int(id)
        item_id = products[int_id - 1]["id"]
        price = products[int_id - 1]["price"]
        name = products[int_id - 1]["name"]
        user_id = 1
        shipping = 4.99
        total = shipping + price
        ordering = Order(item_id=item_id,
                         name=name,
                         price=price,
                         user_id=user_id,
                         shipping=shipping,
                         total=total)
        db.create_all()
        db.session.add(ordering)
        db.session.commit()

        return render_template("order.html", product=products[int_id - 1])

# Customer info and mail handling
@app.route("/confirmation", methods= ["GET", "POST"])
def adress():
    if request.method == "POST":
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

        row = Customer.query.order_by(desc(Customer.id)).first()
        mailadress = row.email
        produkt = Order.query.order_by(desc(Order.id)).first()
        src_id = produkt.item_id
        src = products[src_id - 1]["src"]
        att = "static/imgs/" + src
        invoice = render_template("invoice_pdf.html", produkt=produkt, customer=row, att=att)

        invoice_pdf = pdfkit.from_string(invoice, False, options={"enable-local-file-access": ""})

        msg = Message('Dein Einkauf bei Mona ',
                      recipients=[mailadress])

        msg.body = 'Vielen Dank für Deinen Einkauf beim Monawebshop!'
        msg.html = invoice
        with app.open_resource(att) as fp:
            msg.attach("src", "image/png", fp.read())

        mail.send(msg)



        return render_template("confirmation.html", produkt=produkt, customer=row, att=att)

# Delete from basket/database
@app.route("/delete", methods=["POST"])
def delete():
    row = Order.query.order_by(desc(Order.id)).first()
    Order.query.filter(Order.id == row.id).delete()
    db.session.commit()

    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)
