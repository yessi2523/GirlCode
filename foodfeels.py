def number_of_stars(s):
    return

shermanReviews=[]
shermanComments=[]
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


def getReviews():
    getShermanReview()
    printShermanReviews()


while (True):
    getReviews()
