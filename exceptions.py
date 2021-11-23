try:
    numb =input("Enter Number: ")
    print(int(numb)*int(numb))
    print(numb*numb)
except ValueError:
   print("Error Type:ValueError -> Invalid Input. Retry")
except TypeError:
    print("Error Type:TypeError -> Invalid Input. Retry")