# function to return the input in list of numbers
def organize_inputs(inpt):
    lst = [int(num) for num in inpt.replace("|", ",").split(",")]
    return lst


# the 3 equations
gleichung1 = input()
I = organize_inputs(gleichung1)
I_copy = I

gleichung2 = input()
II = organize_inputs(gleichung2)


gleichung3 = input()
III = organize_inputs(gleichung3)


# function returns TRUE if the to numbers have the same sign
def Same_Sign_Condition(lst1, lst2, n):                                          
    return (lst1[n] <= 0 and lst2[n] <= 0) or (lst1[n] >= 0 and lst2[n] >= 0)

# function to change the signs of a list of numbers
def Change_Sign(lst1):
    lst2 = [i*(-1) for i in lst1]
    return lst2

# functoin to check if two numbers doesn't have the same sign, so in this case the function will change the sighns of the lists 
def Check_Same_Sign(lst1, lst2, n):
    if Same_Sign_Condition(lst1, lst2, n):
        return lst1
    else:
        return Change_Sign(lst1)


# functoin to see if the numbers are equal or if the second number equal to zero 
def Work_with_numbers(lst1, lst2, n):
    if lst1[n] == lst2[n] or lst2[n] == 0:
        return lst1
    else: 
        return Multi(lst1, lst2, n)


# function to multiply one number with another list of numbers
def Multi(lst1, lst2, n):                    
    lst3 = []
    for i in lst1:
        lst3.append(i*lst2[n])
    return lst3


# function to subtract every number in a list with every other number in another list
def Subtract(lst1, lst2):                    
    return [a - b for a, b in zip(lst1, lst2)]         # index function didn't work here because if we have same two values in a list it will return the index of the first value  


# the function to calculate the variables and to print them
def Calculate_X_Y_Z(lst1, lst2, lst3):   
    if lst3[-1] != 0 and lst3[-2] == 0: 
        print("this LGS has no answer!")
    elif lst3[-1] == 0 and lst3[-2] == 0:
        z = "λ"
        y = f"({lst2[-1]} - {lst2[-2]}λ) / {lst2[-3]}"
        x = f"[ {lst1[-1]} - ((({y}) * {lst1[-3]}) + {lst1[-2]}λ) ] / {lst1[0]}"
        print(f"Z = {z} , Y = {y} , X = {x}")
    else:
        z = lst3[-1] / lst3[-2]
        y = (lst2[-1] - (z*lst2[-2])) / lst2[-3]
        x = (lst1[-1] - ((y*lst1[-3]) + (z*lst1[-2]))) / lst1[0]

        print(f"X = {x} , Y = {y} , Z = {z}")


# from here starts the code
I = Check_Same_Sign(I, II, 0)

I_1 = Multi(I, II, 0)
                                                    # now we have it like this   I    (2 4 6 | 5 )  -------> I    (2 4 6 | 5 )
II_1 = Multi(II, I, 0)                              #                            II   (3 5 7 | 10 )          II'  (0 2 4 | -5 )
                                                    #                            III  (2 1 5 | 15 )          III  (2 1 5 | 15 )
II_Strich = Subtract(I_1, II_1)
                             

I = Check_Same_Sign(I, III, 0)

I_2 = Multi(I, III, 0)
                                                    # now we have it like this I   (2 4 6 | 5 )   ------->  I    (2 4 6 | 5 )
III_1 = Multi(III, I, 0)                            #                          II' (0 2 4 | -5 )            II'  (0 2 4 | -5 )
                                                    #                          III (2 1 5 | 15 )            III' (0 6 2 | -20 )
III_Strich = Subtract(I_2, III_1)


II_Strich_copy = Check_Same_Sign(II_Strich, III_Strich, 1)

II_2 = Multi(II_Strich_copy, III_Strich, 1)
                                                    # now we have it like this    I    (2 4 6 | 5 )     ----->  I     (2 4 6 | 5 )
III_2 = Multi(III_Strich, II_Strich_copy, 1)        #                             II'  (0 2 4 | -5 )            II'   (0 2 4 | -5 )
                                                    #                             III' (0 6 2 | -20 )           III'' (0 0 20 | 10)
III_Strich_Strich = Subtract(II_2, III_2)


                                                             # and here we calculate and print the solutions of X, Y and Z      
Calculate_X_Y_Z(I_copy, II_Strich_copy, III_Strich_Strich)   # in owr case these are the solutions   -->   x = 8  ,  y = -3,5  ,  z = 0,5 
