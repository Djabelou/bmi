print("------------------------------")
print("| Body Mass Index calculator |")
print("------------------------------")
print("")
adult = input("Are you an adult ? [y/n]")
print("")
if adult == "y":
  print("What is your weight in kilograms ?")
  weight = input()
  weight = float(weight)
  print("What is your height in meters ?")
  height = input()
  height = float(height)
  bmi = weight/( height*height )
  bmi = round(bmi,1) # round the result at the first digit 
  bmistr=str(bmi)
  print("Your BMI is " + bmistr)
  print("")
  print("In accordance with the recommendation from the World Health Organization for adults,")
  print("you are")
  if bmi < 18.5:
    print("underweight")
  elif bmi < 25:
    print("Normal")
  else:
   print("overweight")
elif adult == "n":
  print("Sorry, this program is not meant for you, be healthy!")
else:
  print("sorry I don't understand " + "'" + adult + "'")
print("")
print("goodbye")
