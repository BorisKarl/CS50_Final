# CS50_Final
Hi there 👋, this is my final project for the Harvard CS50 course 2022/23. 
It is a small flask webapp, a webshop where you can "buy" one of nine dog-paintings of my daughter.
I used dynamic paths, so flask renders the same product-layout-page for every of the nine items accordingly with the help of a python loop
and the flask url_for method. I store the data of the product and customer in a sql database with the help of sqlalchemy.
And as a last step I render a special invoice-page as an email and send it to the customer via flask-mail.
No real payment is involved.
Fell free to try it out!

