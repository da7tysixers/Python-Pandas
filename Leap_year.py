def is_leap(year):
    leap = False
    a = 4
    b = 100
    c = 400
    result = 0
    # Write your logic here
    if ((year % a) == result): # check if year is divisible by 4
        if (year % b) == result: # check if year is divisible by 100
                leap = False # if year is divisible by 100, it is not a leap year
        elif (year % c) == result: # check if year is divisible by 400
                leap = True # if year is divisible by 400, it is a leap year
        #continue
        print(year%a)

    elif (year % a) == result: #check if year is divisible by 4
        if (year % b) == result: # check if year is divisible by 100
                leap = False # if year is divisible by 100, it is not a leap year
                if (year % c) == result: # check if year is divisible by 400
                    leap = True # if year is divisible by 400, it is a leap year
                    
        #print(year % a)
        
    return leap

year = int(input())
print(is_leap(year))