print("Hello welcome to my math quizz.")
print("This maths quizz will help learn and enjoy math")
print("I hope you like my quiz")
name=input("what is your name? ")
while True:
    try:
        n = input("Please enter an age: ")
        n = int(n)
        break
    except ValueError:
        print("Not a valid integer! Please try again ...") 
print("hello {},I hope you have fun playing my maths game".format(name))






