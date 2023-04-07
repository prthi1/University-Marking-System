# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.
# Student ID (UoW): w1898954
# Student ID (IIT): 20211381
# Date: 29.04.2021

def Progression_Outcome():
    global Progress
    global Trailer
    global Retriever
    global Excluded
    if credits_at_pass ==120:
        print('\n*******************************Progression Outcome: Progress*******************************')
        Progress = Progress + 1
    elif credits_at_pass ==100:
        print('\n***********************Progression Outcome: Progress (module trailer)***********************')
        Trailer = Trailer + 1
    elif credits_at_pass ==80 or credits_at_pass ==60:
        print('\n******************Progression Outcome: Do not Progress - module retriever******************')
        Retriever = Retriever + 1
    elif credits_at_pass ==40 and credits_at_defer ==0:
        print('\n*******************************Progression Outcome: Exclude********************************')
        Excluded = Excluded + 1
    elif credits_at_pass ==40:
        print('\n******************Progression Outcome: Do not Progress - module retriever******************')
        Retriever = Retriever + 1
    elif credits_at_pass ==20 and (credits_at_defer ==20 or credits_at_defer ==0):
        print('\n*******************************Progression Outcome: Exclude********************************')
        Excluded = Excluded + 1
    elif credits_at_pass ==20:
        print('\n******************Progression Outcome: Do not Progress - module retriever******************')
        Retriever = Retriever + 1
    elif credits_at_fail ==120:
        print('\n*******************************Progression Outcome: Exclude********************************')
        Excluded = Excluded + 1
    elif credits_at_pass ==0 and (credits_at_defer ==20 or credits_at_defer ==40):
        print('\n*******************************Progression Outcome: Exclude********************************')
        Excluded = Excluded + 1
    elif credits_at_pass ==0:
        print('\n******************Progression Outcome: Do not Progress - module retriever******************')
        Retriever = Retriever + 1

def range_check(level):
    range_input = [0,20,40,60,80,100,120]
    if level not in range_input:
        print('Out of range.')
        return True 
    else:
        return False

def horizonatal_histogram():
    print('\n---------------------------------------------------------------------------------------------------------')
    print('\n*****************************************Horizontal Histogram******************************************')
    print('\nProgress',Progress,'\t: ','*'*Progress)
    print('Trailer',Trailer,'\t: ','*'*Trailer)
    print('Retriever',Retriever,'\t: ','*'*Retriever)
    print('Excluded',Excluded,'\t: ','*'*Excluded,'\n')
    Outcome = Progress + Trailer + Retriever + Excluded 
    print(Outcome,'outcomes in total.')
    print('---------------------------------------------------------------------------------------------------------')

def vertical_histogram():
    print('\n---------------------------------------------------------------------------------------------------------')
    print('\n******************************************Vertical Histogram*******************************************')
    Asterisk='*'
    blank=''
    greatest=max(Progress,Trailer,Retriever,Excluded)
    print('\nProgress\tTrailer\tRetriever\tExcluded')
    for x in range(greatest):
        if x < Progress:
            print(f'{Asterisk:>8}',end='')
        else:
            print(f'{blank:>5}',end='')
        if x < Trailer:
            print('\t'f'{Asterisk:>5}',end='')
        else:
            print('\t'f'{blank:>8}',end='')
        if x < Retriever:
            print('\t'f'{Asterisk:>8}',end='')
        else:
            print('\t'f'{blank:>8}',end='')
        if x < Excluded:
            print('\t'f'{Asterisk:>8}')
        else:
            print('\t'f'{blank:>8}')
    Outcome = Progress + Trailer + Retriever + Excluded
    print('')
    print(Outcome,'outcomes in total.')
    print('---------------------------------------------------------------------------------------------------------')


Progress = 0
Trailer = 0
Retriever = 0
Excluded = 0

loop = True
while loop == True:
    try:
        range_error = False
        credits_at_pass=int(input('\nPlease enter your credits at pass: '))
        range_error = range_check(credits_at_pass)
        if range_error == False:
            credits_at_defer= int(input('Please enter your credits at defer: '))
            range_error = range_check(credits_at_defer)
        if range_error == False:
            credits_at_fail=int(input('Please enter your credits at fail: '))
            range_error = range_check(credits_at_fail)
        if range_error == False:
            total = credits_at_pass + credits_at_defer + credits_at_fail
            if total != 120:
                print('Total incorrect')    
            else:
                Progression_Outcome()
                print('\nWould you like to enter another set of data?')
                repeat=input("Enter 'y' for yes or 'q' to quit and view results: ").lower()
                while repeat !='q' and repeat !='y':
                    print('Invalid Choice')
                    repeat=input("Enter 'y' for yes or 'q' to quit and view results: ").lower()
                else:
                    if  repeat =='q':
                        loop = False
                    else:
                        loop = True    
    except ValueError:
        print('Integer required')

horizonatal_histogram()
vertical_histogram()

