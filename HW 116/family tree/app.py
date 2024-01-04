# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Vraj" # write your name
    age = "14" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def father():

    name = "Yogesh" # write your name
    age = "44" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to mother webpage
@app.route("/mother")
def mother():

    name = "Rakshita" # write your name
    age = "44" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to friends webpage
@app.route("/friend")
def friends():

    name = "Bob" # write your name
    age = "14" # write your age

    return render_template('index.html' , name = name , age = age)


# add other routes, if you want
@app.route("/sister")
def sister():

    name = "Shivanshi" # write your name
    age = "11" # write your age

    return render_template('index.html' , name = name , age = age)




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
