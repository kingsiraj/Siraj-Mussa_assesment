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
             , 'Question 4 400x2-400\n a: 540\n b: 400\n c: 200\n' :  '400',
             'Question 5 800-690\n a: 242\n b: 152\n c: 110\n' :  '110',
             'Question 6 0.98 + 1\n a: 1.98\n b: 0.99\n c: 99\n': '1.98', 'Question 7 1.1 + 0.9?\n a: 1.19\n b: 2\n c: 0.119\n' : '2', 'Question 8 149+120\n a: 249\n b: 269\n c: 280\n': '269', 'Question 9 77+33\n a: 110\n b: 133\n c: 100\n': '110','Question 10 what is the square root of 81?\n a: 91\n b: 9\n c: 19\n': '9',}


for key in questions.keys():
        user_answer=input(key).lower().strip()
        if questions.get(key)==user_answer:
            print("Correct!")
        else:
            print("You're Wrong!")

print("Thank you for taking my quiz I hope you enjoyed it")
          




    
 


        
