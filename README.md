# CS50_Final
Hi there 👋, this is my final project for the Harvard CS50 course 2022/23.

#Technologies used
* Flask
* Python
* Html
* Javascript
* CSS

#Eplanation
Our daughter really likes ti draw. Sometimes she draws cats, sometimes kings, and sometime dogs. Many dogs.
As most parents, we are certain that our daughter is a fantastic artis gifted with a unbelivable amount of talent.
Therefore we wanted to show the world the vide range of her dog paintings.

It is a small flask webapp, a webshop where you can "buy" one of nine dog-paintings of my daughter.
I used dynamic paths, so flask renders the same product-layout-page for every of the nine items accordingly with the help of a python loop
and the flask url_for method. I store the data of the product and customer in a sql database with the help of sqlalchemy.
And as a last step I render a special invoice-page as an email and send it to the customer via flask-mail.
Unfortunatly pythonanywhere, where the live demo is hosted is not allowing a email api in the free mode, so I had to
waive on that option.
No real payment is involved. This is a mock-up shop.
Fell free to try it out!

