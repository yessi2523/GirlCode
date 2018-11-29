# from flask import Flask
# app = Flask(__name__)
#
# @app.route("/")
# def index():
#     return "Index!"
#
# @app.route("/hello")
# def hello():
#     return "Hello World!"
#
# @app.route("/members")
# def members():
#     return "Members"
#
# @app.route("/members/<string:name>/")
# def getMember(name):
#     return name
#
# if __name__ == "__main__":
#     app.run()

import datetime

def number_of_stars(s):
    return

shermanReviews=[]
shermanComments=[]
meal="dinner"

def getShermanReview():
    print("What is your rating of the food in general from 1-5 stars in Sherman?")
    s=input("Enter number of stars from 1-5: ")
    critique=input("Critique or comments on the food: ")
    print("Your rating is " + str(s) + " stars and " + str(critique))

    shermanReviews.append(int(s))
    shermanComments.append(critique)

def printShermanReviews():
    print("reviews are :"+str(shermanReviews))
    total = sum(shermanReviews)
    n = len(shermanReviews)
    avg = total/n
    print("The average is " + str(avg) )
    print(shermanComments)

def checktime():
    global meal
    global shermanReviews
    global shermanComments
    t=datetime.datetime.now()
    if t.hour>16 and meal=="lunch":
        meal="dinner"
        shermanReviews=[]
        shermanComments=[]
        print("It's dinner time! ")
    elif t.hour<=16 and meal=="dinner":
        meal="lunch"
        shermanReviews=[]
        shermanComments=[]
        print("It's lunch time! ")


def getReviews():
    checktime()
    print(meal)
    getShermanReview()
    printShermanReviews()


while (True):
    getReviews()
