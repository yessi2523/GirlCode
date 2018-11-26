def number_of_stars(s):
    return

usdanReviews=[]
usdanComments=[]
def getusdanReview():
    print("What is your rating of the food in general from 1-5 stars in Sherman?")
    s=input("Enter number of stars from 1-5: ")
    critique=input("Critique or comments on the food: ")
    print("Your rating is " + str(s) + " stars" + str(critique))

    usdanReviews.append(int(s))
    usdanComments.append(critique  )

def printusdanReviews():
    print("reviews are :"+str(usdanReviews))
    total = sum(usdanReviews)
    n = len(usdanReviews)
    avg = total/n
    print("The average is " + str(avg) )
    print(usdanComments)

def getReviews2():
    getusdanReview()
    printusdanReviews()

while (True):
    getReviews2()
