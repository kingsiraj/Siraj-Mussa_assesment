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







questions = { 'Question 1 100x56 \n a: 5600\n b: 4500\n c: 5000\n' : '5600' , 'Question 2 78+65\n a: 133\n b: 143\n c: 160\n' :  '143' , 
             'Question 3 0x1\n a: 1\n b: 0.1\n c: 0 \n' : '0' 
                , 'Question 2 400x2-400\n a: 540\n b: 400\n c: 200\n' :  '400' ,}


for key in questions.keys():
    user_answer=input(key)
    if questions.get(key)==user_answer:
        print("Correct!") 
    else:
        print("You're Wrong!")

      

        user_answer = input(key).lower().strip()
