# CS50_Final

Hi there 👋, this is my final project for the Harvard CS50 course 2022/23.

# Technologies used
* Flask
* Python
* Html
* Javascript
* CSS

# Motivation

Our daughter really likes ti draw. Sometimes she draws cats, sometimes kings, and sometime dogs. Many dogs.
As most parents, we are certain that our daughter is a fantastic artist gifted with a unbelievable amount of talent.
Therefore we wanted to show the world the wide range of her dog paintings.

# Explanation

In CS50 we did the project finance, where we had to build a web app for buying and selling stocks. I was fascinated as the **html/css/javascript** aka ***The Frontend*** worked together with **sql and flask** aka ***The Backend***.
So I wanted to build a small shop on my own. I had some ideas and finally the idea of a small art gallery came to my mind.

## Gallery Wow Wow
At the start it was quite challenging to build an app on my own. The production code in the former CS50 lessons was prewritten in some parts, so it was a
lot going back and forth looking at these older lessons and rewriting to get the app running. Finally I used a fairly simple approach to make it work.

### How it works
I wrote a list of dictionaries including information for the corresponding product like *name, images source, id and price*.
Then I wrote a loop to display these images on the index page and used **dynamic urls** to render a product page with the corresponding
information of the product. This was I only had to write one product page which was very convenient.
If you press on the "Kaufen" - buy - button the product gets inserted in an order table with sqlalchemy and the next page gets rendered for inputting the user information. Here it is possible to delete the product from the sql database or input the information for the user.
The last page shows a confirmation page where the user can see what he has ordered and whereto it is going. An email is send as well via flask mail.

### Live demo
Unfortunately pythonanywhere, where the live demo is hosted is not allowing a email api in the free mode, so I had to
waive on that option. You can find the live demo on
http://karlgerd.pythonanywhere.com/
No real payment is involved. This is a mock-up shop.
Fell free to try it out!

## This was CS50!
