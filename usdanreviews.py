def number_of_stars(s):
    return

usdanReviews=[]
def getusdanReview():
    print("What is your rating of the food in general from 1-5 stars in Sherman?")
    s=input("Enter number of stars from 1-5: ")
    print("Your rating is " + str(s) + " stars")

    usdanReviews.append(int(s))

def printusdanReviews():
    print("reviews are :"+str(usdanReviews))
    total = sum(usdanReviews)
    n = len(usdanReviews)
    avg = total/n
    print("The average is " + str(avg) )

def getReviews2():
    getusdanReview()
    printusdanReviews()

while (True):
    getReviews2()
