import datetime
def number_of_stars(s):
    return

usdanReviews=[]
usdanComments=[]
meal="dinner"

def getusdanReview():
    print("What is your rating of the food in general from 1-5 stars in Usdan?")
    s=input("Enter number of stars from 1-5: ")
    critique=input("Critique or comments on the food: ")
    print("Your rating is " + str(s) + " stars: " + str(critique))

    usdanReviews.append(int(s))
    usdanComments.append(critique)

def printusdanReviews():
    print("reviews are :"+str(usdanReviews))
    total = sum(usdanReviews)
    n = len(usdanReviews)
    if n==0:
        print("There are no reviews yet ")
        return
    avg = total/n
    print("The average is " + str(avg) )
    print(usdanComments)


def checktime():
    global meal
    global usdanReviews
    global usdanComments
    t=datetime.datetime.now()
    if t.hour>16 and meal=="lunch":
        meal="dinner"
        usdanReviews=[]
        usdanComments=[]
        print("It's dinner time! ")
    elif t.hour<=16 and meal=="dinner":
        meal="lunch"
        usdanReviews=[]
        usdanComments=[]
        print("It's lunch time! ")



def getReviews2():
    checktime()
    print(meal)
    printusdanReviews()
    getusdanReview()


while (True):
    getReviews2()
