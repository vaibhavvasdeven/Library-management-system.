def again():
    a=int(input("do you want to continue, 1 for continue, 2 for exit"))
    if(a==1):
        start()
    else:
        print("bye bye")
def start():
    print("press 1 for 101 book information \n press 2 for 102 book information \n press 3 for 103 book information \n press 4 for 104 book information \n press 5 for 105 book information")
    b=int(input("enter no"))
    if (b==1):
        print({"title": "spare",
        "author": "Prince Harry",
        "price": "2600",
        "description": "Services in Afghanistan , strained family relationships",
        "launch_date": "10 janurary 2023"})
    elif(b==2):
        print({"title": "Harry Potter",
    "author": "J.k Rowling",
    "price": "600",
    "description": "Harry confronts the fate of the wizaring world",
    "launch_ date": "21 july 200"})  
    elif(b==3):
            print({"title": "The slient patient",
    "author": "Alex michael",
    "price": "149",
    "description": "Psychological thriller",
    "launch_date": "5 february 2019"})
    elif(b==4):
            print({"title": "The Divine Kumbh",
      "author": "Deepak kumar sen",
      "price": "695",
      "description": "Illustrated exploration of the Kumbh mela",
      "launch_date": "january 2025",})
    elif(b==5):
         print({"title": "Not quite dead yet",
      "author": "Holly Jackson",
      "price": "1200",
      "description": "Adult suspense thriller",
      "launch_date": "july 2025"})
    again()

start()

