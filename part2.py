# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.
# Student ID (UoW): w1898954
# Student ID (IIT): 20211381
# Date: 29.04.2021

def Progression_Outcome():
    if credits_at_pass ==120:
        print('\n*******************************Progression Outcome: Progress*******************************')
    elif credits_at_pass ==100:
        print('\n***********************Progression Outcome: Progress (module trailer)***********************')
    elif credits_at_pass ==80 or credits_at_pass ==60:
        print('\n******************Progression Outcome: Do not Progress - module retriever******************')
    elif credits_at_pass ==40 and credits_at_defer ==0:
        print('\n*******************************Progression Outcome: Exclude********************************')
    elif credits_at_pass ==40:
        print('\n******************Progression Outcome: Do not Progress - module retriever******************')
    elif credits_at_pass ==20 and (credits_at_defer ==20 or credits_at_defer ==0):
        print('\n*******************************Progression Outcome: Exclude********************************')
    elif credits_at_pass ==20:
        print('\n******************Progression Outcome: Do not Progress - module retriever******************')
    elif credits_at_fail ==120:
        print('\n*******************************Progression Outcome: Exclude********************************')
    elif credits_at_pass ==0 and (credits_at_defer ==20 or credits_at_defer ==40):
        print('\n*******************************Progression Outcome: Exclude********************************')
    elif credits_at_pass ==0:
        print('\n******************Progression Outcome: Do not Progress - module retriever******************')

def range_check(level):
    range_input = [0,20,40,60,80,100,120]
    if level not in range_input:
        print('Out of range.')
        return True
    else:
        return False

print('----------------------------------------------------------------------------------------------')
loop = True
while loop == True:
    try:
        range_error = False
        credits_at_pass=int(input('\nPlease enter your credits at pass : '))
        range_error = range_check(credits_at_pass)
        if range_error == False:
            credits_at_defer= int(input('Please enter your credits at defer : '))
            range_error = range_check(credits_at_defer)
        if range_error == False:
            credits_at_fail=int(input('Please enter your credits at fail : '))
            range_error = range_check(credits_at_fail)
        if range_error == False:
            total = credits_at_pass + credits_at_defer + credits_at_fail
            if total != 120:
                print('Total incorrect')    
            else:
                Progression_Outcome()
                loop = False  
    except ValueError:
        print('Integer required')
print('\n----------------------------------------------------------------------------------------------')



