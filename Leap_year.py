def is_leap(year):
    leap = False
    
    # Divisible by 4?
    if year % 4 == 0:
        # But if it's divisible by 100...
        if year % 100 == 0:
            # It must also be divisible by 400 to be a leap year
            if year % 400 == 0:
                leap = True
            else:
                leap = False
        else:
            # Divisible by 4 but not 100
            leap = True
            
    return leap


year = int(input())
print(is_leap(year))