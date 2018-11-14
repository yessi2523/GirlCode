def number_of_stars(s):
    return

shermanReviews=[]
def getShermanReview():
    print("What is your rating of the food in general from 1-5 stars in Sherman?")
    s=input("Enter number of stars from 1-5: ")
    print("Your rating is " + str(s) + " stars")

    shermanReviews.append(int(s))

def printShermanReviews():
    print("reviews are :"+str(shermanReviews))
    total = sum(shermanReviews)
    n = len(shermanReviews)
    avg = total/n
    print("The average is " + str(avg) )

def getReviews():
    getShermanReview()
    printShermanReviews()

while (True):
    getReviews()
